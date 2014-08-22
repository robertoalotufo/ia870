# -*- encoding: utf-8 -*-
# Module iastats

from numpy import *
from string import upper

def iastats(f, measurement):

    measurement = upper(measurement)
    if measurement == 'MAX':
        y = max(ravel(f))
    elif measurement == 'MIN':
        y = min(ravel(f))
    elif measurement == 'MEAN':
        y = mean(ravel(f))
    elif measurement == 'MEDIAN':
        y = median(ravel(f))
    elif measurement == 'STD':
        y = std(ravel(f),ddof=1)
    elif measurement == 'STD1':
        y = std(ravel(f))
    elif measurement == 'SUM':
        y = sum(ravel(f))
    else:
        assert 0,'Not a valid measurement'


    return y

