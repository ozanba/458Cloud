def binomial_coeff(n, k):
    res = 1
    if k > n - k:
        k = n - k
    for i in range(k):
        res *= (n - i)
        res //= (i + 1)
    return res

def print_pascals_triangle(rows):
    for i in range(rows):
        print(" " * (rows - i), end="")
        for j in range(i + 1):
            num_stars = binomial_coeff(i, j)
            print("*" * num_stars, end=" ")
        print()

if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    print_pascals_triangle(n)
