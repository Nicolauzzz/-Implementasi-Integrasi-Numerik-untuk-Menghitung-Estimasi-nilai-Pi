import time

def f(x):
    return 4 / (1 + x**2)

def trapezoid_integration(a, b, N):
    h = (b - a) / N
    integral = 0.5 * (f(a) + f(b))
    for i in range(1, N):
        integral += f(a + i * h)
    return integral * h

def main():
    a = 0  # Lower limit of integration
    b = 1  # Upper limit of integration
    N_values = [10, 100, 1000, 10000]  # Variation of N values
    pi_reference = 3.14159265358979323846  # Reference value of pi
    
    for N in N_values:
        start_time = time.time()  # Start time of integration
        integral_value = trapezoid_integration(a, b, N)
        end_time = time.time()  # End time of integration
        execution_time = end_time - start_time
        
        error = abs(integral_value - pi_reference)
        print(f"For N = {N}:")
        print(f"  Calculated Pi: {integral_value}")
        print(f"  Error: {error}")
        print(f"  Execution Time: {execution_time} seconds\n")

if __name__ == "__main__":
    main()
