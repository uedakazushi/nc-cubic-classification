#!/usr/bin/env python3
"""Full P exclusion: regenerate and independently replay polynomial lifts.
Requires SymPy, python-flint and (unless --reuse) Singular 4.4.1-compatible CLI.
Generated large logs remain in the work directory, not in Git.
"""
import argparse,hashlib,json,subprocess,sys,time
from pathlib import Path
import sympy as S
from flint import fmpq_mpoly_ctx,fmpq_mpoly,fmpq_poly,fmpq
from sympy.polys.matrices import DomainMatrix
from verify_cubic_as4_P_projections import verify
from verify_cubic_as4_four_simple_p import pvalues
from verify_cubic_as4_four_simple import source_matrix,K as SKEW,IX
from verify_cubic_pym_generic import words


def transport():
    l,r=S.symbols('l r');F=S.QQ_I.frac_field(l,r);q=l+1;a=2*l*l+2*l+1
    lp=-q;rp=(a-q*q*r)/(l*l);R,A=source_matrix(l,pvalues(l,r));T,_=source_matrix(lp,pvalues(lp,rp))
    Z=DomainMatrix.from_Matrix(SKEW.T*R/2).convert_to(F);W=DomainMatrix.from_Matrix(SKEW.T*T/2).convert_to(F)
    diag=[1,-S.Rational(1,64),S.I*l/(8*q),-S.I*q/(8*l)];dd=[F.from_sympy(x) for x in diag]
    pairs=[(0,1),(0,2),(0,3),(1,2),(1,3),(2,3)];perm=[1,0,2,3];pp=[];sg=[];weights=[]
    for x,y in pairs:
        u,v=perm[x],perm[y];pp.append(pairs.index(tuple(sorted((u,v)))));sg.append(1 if u<v else -1);weights.append(dd[u]*dd[v])
    for i in range(6):
        for j in range(6):assert Z[i,j].element*sg[i]*weights[i]==W[pp[i],pp[j]].element*weights[j]
    assert -dd[1]*dd[2]*dd[3]==F.from_sympy(S.Rational(1,4096))
    d=a-(2*l+1)*r;e=q*r-a;f=a*r-2*l*a-1
    identities=[rp-1+q*q*(r-1)/(l*l),a-(2*lp+1)*rp-q*q*d/(l*l),(lp+1)*rp-a-q*e/l,a*rp-2*lp*a-1+q*q*f/(l*l)]
    assert all(not F.from_sympy(x) for x in identities)
    rd=DomainMatrix.from_Matrix(R).convert_to(F);ad=DomainMatrix.from_Matrix(A).convert_to(F);w=(rd*ad*rd.transpose()).to_dok()
    assert any(w.values())
    assert all(not(w.get((IX[v[:2]],IX[v[2:]]),F.zero)+w.get((IX[v[1:3]],IX[(v[3],v[0])]),F.zero)) for v in words(4))
    print('PASS literal P reflection, domain preservation and universal CY tensor',flush=True)
    return {'lambda_prime':str(lp),'r_prime':str(rp),'diagonal_before_ab_swap':list(map(str,diag)),'determinant':'1/4096'}


def source(P,Q,D,scales_path):
    l,r=S.symbols('l r');G=S.QQ_I.poly_ring(l,r);K=P.domain;DG=G.from_sympy(K.to_sympy(D));data={};pd,qd=P.to_dok(),Q.to_dok()
    for ij in pd.keys()|qd.keys():
        co={ex:S.QQ_I(c,0) for ex,c in pd.get(ij,K.zero).to_dict().items()}
        for ex,c in qd.get(ij,K.zero).to_dict().items():co[ex]=co.get(ex,S.QQ_I.zero)+S.QQ_I(0,c)
        data[ij]=G.ring.from_dict(co)
    raw=json.loads(scales_path.read_text());scales={int(c):G.from_sympy(S.sympify(e,locals={'l':l,'r':r})) for c,e in raw.items()}
    assert set(scales)==set(range(140))
    for h in scales.values():assert h and not divmod(DG,h)[1]
    free3=json.loads(Path(__file__).with_name('cubic_as4_P_projection_degree3.json').read_text())['free_columns_zero_based'];assert len(free3)==20
    ix={v:j for j,v in enumerate(words(4))};out={}
    for j,k in enumerate(free3):
        v=words(3)[k]
        for g in range(4):
            leftword,rightword=ix[v+(g,)],ix[(g,)+v]
            for i in range(35):
                c=35*g+i;e=data.get((i,leftword),G.zero)-data.get((i,rightword),G.zero)
                if e:
                    quo,rem=divmod(e,scales[c]);assert not rem;out[j,c]=quo
    return out,G


def replay(path,primitive,G,special=None):
    ctx=fmpq_mpoly_ctx.get(('l','r'));L,R=ctx.gens();zero=ctx.constant(0);A={};t=time.time()
    for (j,c),poly in primitive.items():
        if special is not None:
            value=S.QQ_I(-S.Rational(1,2),special);co={}
            for (lexp,rexp),x in poly.to_dict().items():co[0,rexp]=co.get((0,rexp),S.QQ_I.zero)+x*value**lexp
            poly=G.ring.from_dict(co)
        ar=ctx.from_dict({ex:fmpq(str(x.x)) for ex,x in poly.to_dict().items() if x.x});ai=ctx.from_dict({ex:fmpq(str(x.y)) for ex,x in poly.to_dict().items() if x.y})
        if ar:A[2*j,2*c]=ar;A[2*j+1,2*c+1]=ar
        if ai:A[2*j+1,2*c]=ai;A[2*j,2*c+1]=-ai
    NN={};XX={};piv={};last='';digest=hashlib.sha256()
    with path.open() as stream:
        for line in stream:
            digest.update(line.encode());last=line.strip();assert '?' not in line and 'FAIL' not in line and 'int division' not in line
            if line.startswith('PIV:'):
                _,j,p=line.split(':');piv[int(j)]=int(p)
            elif line.startswith(('N:','X:')):
                kind,i,j,e=line.split(':',3);i,j=int(i),int(j);poly=fmpq_mpoly(e.strip(),ctx);assert poly
                assert 0<=j<40 and 0<=i<(40 if kind=='N' else 280)
                (NN if kind=='N' else XX)[i,j]=poly
    assert last=='DONE' and set(piv)==set(range(40)) and set(piv.values())==set(range(40))
    factors={}
    for j,p in piv.items():
        assert all(not NN.get((i,j),zero) for i in range(p));z=NN[p,j]
        while True:
            q,rem=divmod(z,R-1)
            if rem:break
            z=q
        if special is not None:assert z.total_degree()==0 and z
        else:
            assert z.degrees()[1]<=0
            co=z.to_dict();deg=int(z.degrees()[0]);pp=fmpq_poly([co.get((i,0),0) for i in range(deg+1)])
            for f,k in pp.factor()[1]:
                f=f/f.leading_coefficient();factors[tuple(map(str,f.coeffs()))]=f
    right={}
    for (k,j),x in XX.items():right.setdefault(k,[]).append((j,x))
    out={ij:-x for ij,x in NN.items()}
    for (i,k),a in A.items():
        for j,x in right.get(k,[]):out[i,j]=out.get((i,j),zero)+a*x
    assert not any(out.values()),'nonzero exact polynomial C0*X-N'
    label='generic vertical cover' if special is None else f'lambda=-1/2+({special})i'
    print('PASS independent P lift',label,'seconds',round(time.time()-t,2),flush=True)
    return factors,{'case':label,'raw_sha256':digest.hexdigest(),'N_nonzero_entries':len(NN),'X_nonzero_entries':len(XX),'polynomial_identity':'C0*X=N over QQ[l,r]','triangular_pivots':40}


def main():
    parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--work-dir',type=Path,default=Path('work/P_full_proof'));parser.add_argument('--singular',default='Singular');parser.add_argument('--reuse',action='store_true');parser.add_argument('--timeout',type=int,default=300);args=parser.parse_args();args.work_dir.mkdir(parents=True,exist_ok=True)
    names=[('global',None),('half',0),('plus',1),('minus',-1)]
    if not args.reuse:
        for name,special in names:
            prefix=args.work_dir/name;cmd=[sys.executable,str(Path(__file__).with_name('generate_cubic_as4_P_centre_input.py')),str(prefix)]
            if special is not None:cmd.append(str(special))
            subprocess.run(cmd,check=True)
            with prefix.with_suffix('.log').open('w') as out:subprocess.run([args.singular,'-q',str(prefix.with_suffix('.sing'))],stdout=out,stderr=subprocess.STDOUT,check=True,timeout=args.timeout)
    _,P,Q,D=verify(4);primitive,G=source(P,Q,D,args.work_dir/'global.scales.json');results=[];factors=None
    for name,special in names:
        fs,result=replay(args.work_dir/f'{name}.log',primitive,G,special);results.append(result)
        if special is None:factors=fs
    g=fmpq_poly([1])
    for f in factors.values():g*=f
    reflected=fmpq_poly([0]);h=fmpq_poly([-1,-1])
    for c in reversed(g.coeffs()):reflected=reflected*h+c
    common=g.gcd(reflected);shared=common
    for f in [fmpq_poly([0,1]),fmpq_poly([1,1]),fmpq_poly([1,2,2]),fmpq_poly([1,2]),fmpq_poly([5,4,4])]:
        while True:
            q,rem=divmod(common,f)
            if rem:break
            common=q
    assert common.degree()==0 and common
    tr=transport()
    cert={'version':'classification-v88','source_commit':'as4 a45f834f51a00c47443b51caf66abaf4629546b9','scope':'Every explicit FT2/FT3 P_lambda,r+/- excluded conditional AS4; no full CY/chart coverage or AS4 sufficiency imported.','status':'Independent exact polynomial lift replay executed','dependencies':'SymPy and python-flint; Singular needed only to regenerate logs. Large generated logs are untracked and reproducible from the source-domain input generator.','generic_vertical_factors':[list(x) for x in factors],'generic_polynomial_degree':int(g.degree()),'reflection_gcd_coefficients':list(map(str,shared.coeffs())),'remaining_vertical_values':['-1/2','-1/2+i','-1/2-i'],'reflection':tr,'lift_checks':results,'proof':'papers/sections/cubic_as4_four_simple_exclusions.tex'}
    Path(__file__).with_name('cubic_as4_P_full_certificate.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS every P parameter: vertical cover, reflection and three complete special lines',flush=True)

if __name__=='__main__':main()
