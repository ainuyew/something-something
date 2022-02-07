import numpy as np
from scipy import interpolate

def test(ys):
    x=[.55, .6, 65, .7, .75, .8, .85, .9, .95, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.7, 2]
    xout=np.linspace(.55, 2, 7)
    f=lambda y: interpolate(interp1d(x, ys)(xout)
    return np.apply_along_axis(f, axis=1, arr=r.zema_grouped_series)
