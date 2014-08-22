# -*- encoding: utf-8 -*-
# Module iaimg2se

from numpy import *
from string import upper

def iaimg2se(fd, FLAT="FLAT", f=None):
    from iaisbinary import iaisbinary
    from iaseshow import iaseshow
    from ialimits import ialimits

    fd = (fd > 0)
    #assert iaisbinary(fd),'First parameter must be binary'
    FLAT = upper(FLAT)
    if FLAT == 'FLAT':
        return iaseshow(fd)
    else:
        B = choose(fd, ( ialimits(int32([0]))[0]*ones(fd.shape),f) )
    B = iaseshow(int32(B),'NON-FLAT')

    return B

