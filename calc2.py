def power_method_simple():
    A = [
        [2, 1],
        [1, 2]
    ]

    x = [1, 1]

    for _ in range(5):
        y = [
            A[0][0] * x[0] + A[0][1] * x[1],
            A[1][0] * x[0] + A[1][1] * x[1]
        ]

        max_val = max(abs(y[0]), abs(y[1]))
        x = [y[0] / max_val, y[1] / max_val]
        print(f"x = {x}")

    eigenvalue = (A[0][0]*x[0] + A[0][1]*x[1]) / x[0]
    print("Eigenvalue:", eigenvalue)

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

power_method_simple()
print("Factorial of 5:", factorial(5))

def absolute(num_1):
    if num_1 < 0:
        return -num_1
    else:
        return num_1


print(absolute(-10)) 
print(absolute(7))    

def bitwise_or(a, b):
    return a | b

# تجربة
num1 = 6   # 0110
num2 = 3   # 0011

result = bitwise_or(num1, num2)  # الناتج بيكون 0111 = 7

print("Bitwise OR:", result)
