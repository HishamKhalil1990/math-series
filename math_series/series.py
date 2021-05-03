def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)       

def lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return lucas(n-1) + lucas(n-2) 

def sum_series(n,first_opt_value = 0,second_opt_value = 1):
    if n == 0:
        return first_opt_value
    elif n == 1:
        return second_opt_value
    else:
        return sum_series(n-1,first_opt_value,second_opt_value) + sum_series(n-2,first_opt_value,second_opt_value) 