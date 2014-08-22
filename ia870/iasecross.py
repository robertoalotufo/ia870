# -*- encoding: utf-8 -*-
# Module iasecross

from numpy import *

def iasecross(r=1):
    from iasesum import iasesum
    from iabinary import iabinary

    B = iasesum( iabinary([[0,1,0],
                           [1,1,1],
                           [0,1,0]]),r)
    return B

