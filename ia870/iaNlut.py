# -*- encoding: utf-8 -*-
# Module iaNlut

import numpy as np
def iaNlut(s,offset):
    '''Precompute array of neighbors. Optimized by broadcast.

    s - image shape
    offset - offset matrix, 2 columns (dh,dw) by n. of neighbors rows
    '''
    H,W = s
    n = H*W
    hi = np.arange(H).reshape(-1,1)
    wi = np.arange(W).reshape(1,-1)
    hoff = offset[:,0]
    woff = offset[:,1]
    h = hi + hoff.reshape(-1,1,1)
    w = wi + woff.reshape(-1,1,1)
    h[(h<0) | (h>=H)] = n
    w[(w<0) | (w>=W)] = n
    Nlut = np.clip(h * W + w,0,n)
    return Nlut.reshape(offset.shape[0],-1).transpose()

