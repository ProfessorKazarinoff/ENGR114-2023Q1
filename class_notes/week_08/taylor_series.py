# taylor_series.py

from math import factorial

# the exp() function
def exp_taylor(x, n_terms):
    exp_t = 0
    for n in range(n_terms):
        term = x**n/factorial(n)
        exp_t += term
        
    return exp_t

# the sin() function
def sin_taylor(x, n_terms):
    sin_t = 0
    for n in range(n_terms):
        term = (-1)**n * x**(2*n+1)/factorial(2*n+1)
        sin_t += term
        
    return sin_t

# the "main" function
def taylor(func, x, terms=10):
    # don't forget to add the doc string in the lab instructions
    if terms>50:
        raise Exception('number of terms should not exceed 50')
    elif terms<1:
        raise Exception('number of terms should be 1 or greater')
    if func == 'sin':
        ans = sin_taylor(x,terms)
    elif func == 'exp':
        ans = exp_taylor(x,terms)
    else:
        raise Exception('not one of the functions, use sin or exp only')
        return None
        
    return ans
