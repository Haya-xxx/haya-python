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

power_method_simple()