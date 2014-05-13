
import numpy as np

def trapz(func, a, b, N):
    """This function finds the integral of (area under) the function
    passed, on the interval passed from a to b, with N subdivisions
    of equal length. The total area is thus the sum of the areas
    of N - 1 trapezoidal subdivisions.
    """
    h = (b-a)/N
    k = np.arange(1,N)
    I = h*(0.5*func(a) + 0.5*func(b) + func(a+k*h).sum())

    return I

def simps(func, a, b, N):
    """This function computes the integral of the function passed
    on the interval passed (from a to b) with N subdivisions. 
    This method of integration involves representing the area of
    each subdivision by it's 'height', given by the passed function's
    output at each subdivision's bound on the domain.
    """
    h = (b-a)/N
    k1 = np.arange(1,N/2+1)
    k2 = np.arange(1,N/2)
    I = (1./3.)*h*(func(a) + func(b) + 4.*func(a+(2*k1-1)*h).sum() + 2.*func(a+2*k2*h).sum())
    
    return I
    

