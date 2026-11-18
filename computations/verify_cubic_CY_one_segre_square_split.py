"""Central cubics in the external and upper-cross square-split charts."""
import sympy as s
from verify_cubic_CY_one_segre_cross import PivotAlgebra, centre_calculation, p, h
from verify_cubic_CY_one_segre_shared import CUBICS, pbw_rows
from verify_cubic_CY_one_segre_square import Q, comm, word
from verify_cubic_CY_one_segre_shared_squares import factors
from verify_cubic_as4_four_simple_second import central_data
from verify_cubic_pym_generic import words

from pathlib import Path
import json

PARAMETERS = (p, h)
sym=lambda a,b:(word(a,b)+word(b,a))/2
U=s.Matrix.hstack(*(sym(i,j) for i,j in [(0,2),(0,3),(1,2),(1,3)]))
K=s.Matrix.hstack(*(comm(i,j) for i in range(4) for j in range(i+1,4)))
q=word(0,0)+sym(2,3)
A=s.zeros(4)
A[0,3]=A[3,0]=Q(1,2)
A[1,2]=A[2,1]=-Q(1,2)
C=s.zeros(6)
C[1,4]=C[4,1]=Q(1,8)
C[2,3]=C[3,2]=-Q(1,8)
J=s.zeros(6)
J[0,5]=J[5,0]=1
J[1,4]=J[4,1]=-1
J[2,3]=J[3,2]=1

def outer(H,b1,v):
    B=s.zeros(4,1).row_join(H).row_join(s.zeros(4,1))
    return s.Matrix.hstack(U+K*B.T*A.inv(),K[:,b1],q+v*K[:,5-b1])

def cross(x,gamma,index,linear_columns=False):
    N=s.Matrix([[-2*x[12],x[0],x[1]+2*x[14],x[3],x[5]-x[9],-x[10]],
                [-2*x[13],x[1],x[2],x[5]-x[9],x[6],x[11]],
                [0,x[3],x[5],x[4],x[7],-x[12]],
                [0,x[5],x[6],x[7],x[8],x[13]]])
    b=s.Matrix(x[9:15])
    if linear_columns:
        return s.Matrix.hstack(U*A+K*N.T, K*b,
                               q+(U*N[:,index]+K*(C+gamma*J)[:,index])/b[index])
    D=C+gamma*J-N.T*A.inv()*N
    return s.Matrix.hstack(U+K*N.T*A.inv(), K*b,q+K*D[:,index]/b[index])

def charts():
    for name,params,units in [
        ('A0',{1:h-1},[]),('A1',{0:1,1:h-1},[]),('A2',{0:1,1:h-1,2:p},[p]),
        ('Bc2',{0:h,4:1},[]),('Bc1',{3:1},[]),
        ('Bn2',{0:h-1,1:h-1,2:h+1,4:p,7:p,8:p},[p]),
        ('Bn1',{0:-1,1:-1,2:1,3:h,5:h,6:h},[h])]:
        x=[params.get(i,0) for i in range(9)]
        H=s.Matrix([[x[0],x[1]+2,x[3],x[5]],
                    [x[1],x[2],x[5],x[6]],
                    [x[3],x[5],x[4],x[7]],
                    [x[5],x[6],x[7],x[8]]])
        yield name,outer(H,5,Q(1,8)),units
    for name,a,b,c,d,units in [
        ('C',p,h/2,1,p,[]),('L',0,p+h/2,0,-p*p,[p]),
        ('N',1,h/2,0,0,[]),('Z',0,h/2,0,0,[])]:
        gamma=Q(1,8)-2*b*(b-h)+2*a*c
        H=s.Matrix([[0,a,0,b-h],[a,0,b-h,0],[0,b,0,c],[b,0,c,0]])
        if name != 'L':
            if name == 'C':
                H = H.subs(p, 0)
                name = 'C_p0'
            parameters = [unit.subs(p, 0) for unit in [h, d+h*h/4, 4*gamma**2-h*h, *units]]
            yield name, outer(H, 0, (gamma/h).subs(p, 0)), parameters
    for x,name,H in [(0,'a',(0,0,0)),(1,'a',(1,0,0)),(2,'a',(1,0,1)),
                     (0,'b',(0,0,0)),(1,'b',(1,0,0)),(2,'b',(1,0,1)),
                     (3,'b',(0,1,0)),(4,'b',(1,1,0)),(5,'b',(1,1,p))]:
        aa,bb,cc=H
        Ha=s.Matrix([[aa,bb,0,-h],[bb,cc,-h,0],[0,0,0,0],[0,0,0,0]])
        Hb=s.Matrix([[0,0,0,0],[0,0,0,0],[0,h,aa,bb],[h,0,bb,cc]])
        yield f'{name}{x}',outer(Ha if name=='a' else Hb,0,Q(1,8)/h),[h,4*h-1,4*h+1]+([p] if x==5 else [])
    x=[0]*15
    for i,v in [(4,h),(5,Q(1,4)),(7,-h),(8,h),(9,Q(1,4)),(10,1),(11,1)]:
        x[i]=v
    yield 'CT',cross(x,Q(1,8),0),[h]


def generic(source, units):
    field = s.QQ.frac_field(*PARAMETERS)
    algebra, rank = centre_calculation(source, (0, 1, 2, 3), field, field.from_sympy)
    assert rank == 20
    minor = algebra.pivot_product
    denominators = {value.denom.as_expr()
                    for n in (2, 3, 4) for image in algebra.right[n].values()
                    for value in image.values()}
    required = factors([minor.numer.as_expr(), minor.denom.as_expr(), *denominators])
    remaining = required - factors(units)
    return {"minor": str(field.to_sympy(minor)), "rank": rank,
            "exception_factors": sorted(map(str, remaining))}, remaining


def fixed(name, relations, field):
    matrix, rows, (projection, _) = central_data(relations, field)
    rank = len(rows)
    if rank == 20:
        minor = matrix.extract(rows, range(20)).det()
        return {"rank": rank, "minor": str(field.to_sympy(minor))}
    assert name in {"N", "Z", "C_p0", "a0", "a1", "a2", "b0", "b1", "b2", "b3", "b4"}, name
    candidates = [(0, 0, 0), (0, 0, 1), (0, 1, 1), (1, 1, 1)]
    if name == "Z":
        candidates += [(2, 2, 2), (3, 3, 3)]
    span = projection.extract(range(20), [words(3).index(w) for w in candidates])
    kernel = matrix.nullspace().transpose()
    assert span.hstack(kernel).rank() == span.rank()
    if name == "Z":
        assert kernel.shape[1] == span.rank() == 6
    return {"rank": rank, "supported": ["".join("abcd"[i] for i in w) for w in candidates]}


def line(name, relations, units, parameter):
    record, exceptions = generic(relations, units)
    specialized = []
    for f in sorted(exceptions, key=str):
        polynomial = s.Poly(f, parameter, domain=s.QQ)
        assert polynomial.degree() in (1, 2) and polynomial.is_irreducible
        root = s.solve(f, parameter)[0]
        assert s.Poly(s.minpoly(root, parameter), parameter).monic() == polynomial
        field = s.QQ if root.is_Rational else s.QQ.algebraic_field(root)
        result = fixed(name, relations.subs(parameter, root), field)
        if name == "Z" and result["rank"] != 20:
            assert f == h*h+Q(1, 12)
        specialized.append({"factor": str(f), **result})
    return {**record, "specializations": specialized}


def binary_containment(relations, units):
    """Force the sixteen nonbinary coordinates of any central cubic to vanish."""
    binary_columns = {i for i, cubic in enumerate(CUBICS) if max(cubic) < 2}

    def check(source, field):
        rows, determinant, coefficients = pbw_rows(source, field, field.from_sympy)
        rows = [row for row in rows if binary_columns.isdisjoint(row)]
        elimination = PivotAlgebra(field, 4, [], [0]*4)
        elimination.pivot_product = field.one
        assert len(elimination.echelon(rows)) == 16
        return elimination.pivot_product, determinant, coefficients

    field = s.QQ.frac_field(*PARAMETERS)
    minor, determinant, coefficients = check(relations, field)
    required = factors([minor.numer.as_expr(), minor.denom.as_expr(),
                        determinant.numer.as_expr(), determinant.denom.as_expr(),
                        *[value.denom.as_expr() for value in coefficients]])
    resonance = h*h+Q(1, 48)
    remaining = required - factors(units)
    assert remaining == {resonance}
    root = s.I*s.sqrt(3)/12
    assert s.Poly(s.minpoly(root, h), h).monic().as_expr() == resonance
    special_field = s.QQ.algebraic_field(s.I, s.sqrt(3)).frac_field(p)
    special_minor, special_determinant, special_coefficients = check(relations.subs(h, root), special_field)
    assert special_minor.numer.is_ground and special_minor.denom.is_ground
    assert special_determinant.numer.is_ground and special_determinant.denom.is_ground
    assert all(value.denom.is_ground for value in special_coefficients)
    return {
        "restricted_rank": 16, "minor": str(s.factor(field.to_sympy(minor))),
        "required_factors": sorted(map(str, required)),
        "resonance": str(resonance), "resonance_minor": str(special_field.to_sympy(special_minor)),
        "centre_contained_in": ["aaa", "aab", "abb", "bbb"],
    }


def main():
    records = []
    for name, relations, units in charts():
        if name == "b5":
            result = binary_containment(relations, units)
        elif name == "A2":
            result, exceptions = generic(relations, units)
            assert not exceptions
        elif name == "Bn2":
            result, exceptions = generic(relations, units)
            substitutions = [
                (h-1, {h: 1}, p), (h+1, {h: -1}, p),
                (p+Q(1, 32), {p: -Q(1, 32)}, h),
                (p+h/32-Q(1, 32), {p: (1-h)/32}, h),
            ]
            assert exceptions == {factor for factor, _, _ in substitutions}
            result["exceptional_curves"] = [
                {"factor": str(factor),
                 **line(name, relations.subs(subs), [unit.subs(subs) for unit in units], parameter)}
                for factor, subs, parameter in substitutions
            ]
        else:
            result = line(name, relations, units, h)
        records.append({"name": name, **result})
        print("PASS", name, flush=True)
    Path(__file__).with_name("cubic_CY_one_segre_square_split_certificate.json").write_text(
        json.dumps(records, indent=2)+"\n"
    )


if __name__ == "__main__":
    main()
