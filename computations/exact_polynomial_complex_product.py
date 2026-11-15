"""Exact sparse polynomial complex-product identity, optional FLINT acceleration."""


def assert_complex_product(A,B,C,D,E=None,F=None):
    """Verify (A+iB)(C+iD)=E+iF over the rational polynomial domain.
    The fallback uses SymPy directly. FLINT checks the same polynomial
    coefficients exactly; this is not modular sampling or numeric tolerance.
    """
    assert A.shape==B.shape and C.shape==D.shape and A.shape[1]==C.shape[0]
    shape=(A.shape[0],C.shape[1]);K=A.domain
    assert all(m.domain==K for m in [B,C,D])
    try:
        from flint import fmpq_mpoly_ctx,fmpq
    except ImportError:
        real=A*C-B*D;imag=A*D+B*C
        assert (real-E).is_zero_matrix if E is not None else real.is_zero_matrix
        assert (imag-F).is_zero_matrix if F is not None else imag.is_zero_matrix
        return 'SymPy'
    ctx=fmpq_mpoly_ctx.get(tuple(map(str,K.symbols)));zero=ctx.constant(0)
    def convert(m):
        if m is None:return {}
        assert m.domain==K
        return {ij:ctx.from_dict({ex:fmpq(str(c)) for ex,c in p.to_dict().items()}) for ij,p in m.to_dok().items()}
    ar,ai,br,bi=map(convert,[A,B,C,D]);er,ei=convert(E),convert(F)
    rr={ij:-x for ij,x in er.items()};ri={ij:-x for ij,x in ei.items()};right={}
    for k,j in br.keys()|bi.keys():right.setdefault(k,[]).append((j,br.get((k,j),zero),bi.get((k,j),zero)))
    for i,k in ar.keys()|ai.keys():
        a,b=ar.get((i,k),zero),ai.get((i,k),zero)
        for j,c,d in right.get(k,[]):
            if a:
                if c:rr[i,j]=rr.get((i,j),zero)+a*c
                if d:ri[i,j]=ri.get((i,j),zero)+a*d
            if b:
                if c:ri[i,j]=ri.get((i,j),zero)+b*c
                if d:rr[i,j]=rr.get((i,j),zero)-b*d
    assert not any(rr.values()) and not any(ri.values()),'nonzero exact polynomial product remainder'
    return 'FLINT rational multivariate polynomials'
