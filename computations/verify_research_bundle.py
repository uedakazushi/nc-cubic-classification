"""Check current manuscript references, catalog assets and Python dependencies.

This is a structural check of the research bundle, not a mathematical proof
check and not a replay of the individual algebraic certificates. Run from any
directory; no tracked files are written.
"""

import ast
from collections import Counter
import json
from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parent.parent


def main():
    visited, active = set(), set()
    labels, refs, citations, bibliography = [], [], [], []
    problems = []

    def visit(path):
        if path in active:
            problems.append(f"Cyclic TeX input: {path.relative_to(ROOT)}")
            return
        if path in visited:
            problems.append(f"Repeated TeX input: {path.relative_to(ROOT)}")
            return
        if not path.is_file():
            problems.append(f"Missing TeX input: {path.relative_to(ROOT)}")
            return
        visited.add(path)
        active.add(path)
        source = re.sub(r"(?m)(?<!\\)%.*$", "", path.read_text())
        labels.extend(re.findall(r"\\label\{([^}]+)\}", source))
        refs.extend(re.findall(r"\\(?:ref|eqref|autoref|pageref)\{([^}]+)\}", source))
        for group in re.findall(r"\\cite(?:\[[^\]]*\])*\{([^}]+)\}", source):
            citations.extend(key.strip() for key in group.split(","))
        bibliography.extend(re.findall(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}", source))
        for target in re.findall(r"\\(?:input|include)\{([^}]+)\}", source):
            child = ROOT / target
            if not child.suffix:
                child = child.with_suffix(".tex")
            visit(child)
        active.remove(path)

    visit(ROOT / "papers/weak_cubic_axioms.tex")
    problems.extend(f"Duplicate label: {k}" for k, n in Counter(labels).items() if n > 1)
    problems.extend(f"Undefined reference: {k}" for k in sorted(set(refs) - set(labels)))
    problems.extend(f"Undefined citation: {k}" for k in sorted(set(citations) - set(bibliography)))

    python_files = sorted((ROOT / "computations").rglob("*.py"))
    local_modules = {path.stem for path in python_files}
    external = set()
    for path in python_files:
        for node in ast.walk(ast.parse(path.read_text(), filename=str(path))):
            names = ([entry.name for entry in node.names] if isinstance(node, ast.Import)
                     else [node.module] if isinstance(node, ast.ImportFrom) and node.module else [])
            for name in names:
                name = name.split(".")[0]
                if name not in sys.stdlib_module_names and name not in local_modules and name != "__future__":
                    external.add(name)
    packages = {re.split(r"[<>=!~;\[]", line.strip())[0].lower()
                for line in (ROOT / "requirements.txt").read_text().splitlines()
                if line.strip() and not line.lstrip().startswith("#")}
    package_for = {"flint": "python-flint"}
    for name in sorted(external):
        if package_for.get(name, name).lower() not in packages:
            problems.append(f"Undeclared Python dependency: {name}")

    json_files = sorted((ROOT / "computations").rglob("*.json"))
    json_files += sorted((ROOT / "research").glob("*.json"))
    for path in json_files:
        try:
            json.loads(path.read_text())
        except (UnicodeError, ValueError) as error:
            problems.append(f"Invalid JSON {path.relative_to(ROOT)}: {error}")

    catalog_path = ROOT / "research/cubic_classification_validation.json"
    catalog_source = catalog_path.read_text()
    catalog = json.loads(catalog_source)
    proof_assets = catalog.get("proof_assets", {})
    computation_assets = sorted(set(re.findall(r"computations/[A-Za-z0-9_./-]+", catalog_source)))
    for path in [*proof_assets.values(), *computation_assets]:
        if not (ROOT / path).is_file():
            problems.append(f"Missing catalog asset: {path}")

    result = {
        "status": "FAIL" if problems else "PASS",
        "tex_files": len(visited),
        "unique_labels": len(set(labels)),
        "python_files_parsed": len(python_files),
        "external_python_modules": sorted(external),
        "json_files_parsed": len(json_files),
        "catalog_proof_assets": len(proof_assets),
        "catalog_computation_assets": len(computation_assets),
        "problems": problems,
        "scope": "References, catalog asset existence, syntax, JSON readability and declared imports only; not mathematical verification.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    if problems:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
