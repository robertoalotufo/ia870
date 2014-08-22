# -*- encoding: utf-8 -*-
# Module iaset2mat

from numpy import *

def iaset2mat(A):
    from iabinary import iabinary
    from ialimits import ialimits

    if len(A) == 2:
        x, v = A
        v = asarray(v)
    elif len(A) == 1:
        x = A[0]
        v = ones((len(x),),bool)
    else:
        raise TypeError, 'Argument must be a tuple of length 1 or 2'
    if len(x) == 0:  return array([0]).astype(v.dtype)
    if len(x.shape) == 1: x = x[newaxis,:]
    dh, dw = abs(x).max(0)
    h,w = (2*dh) + 1, (2*dw) + 1
    M=ones((h, w)) * ialimits(v)[0]
    offset = x[:,0] * w + x[:,1] + (dh*w + dw)
    M.flat[offset] = v
    M = M.astype(v.dtype)

    return M

