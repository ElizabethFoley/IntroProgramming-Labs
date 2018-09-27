# Intro to Programming
# Fibonacci Sequence
# 9/20/18

def main():

    n = int(input("Enter a value to find the Fibonacci number: "))
    curr, prev = 1, 1
    for i in range(n-2):
        curr, prev = curr+prev, curr

    print()
    print("The Fibonacci number is: ", curr)

main()
