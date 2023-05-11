'''
*              *
* *          * *
* * *      * * *
* * * *  * * * *
* * * *  * * * *
* * *      * * *
* *          * *
*              *
'''

n = int(input("Enter Number: "))

# Upper half of the diamond
for i in range(n):
    for j in range(2 * n):
        if i >= j:
            print("*", end="")
        else:
            print(" ", end="")
        if i >= (2 * n - 1) - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half of the diamond
for i in range(n):
    for j in range(2 * n):
        if i + j <= n - 1:
            print("*", end="")
        else:
            print(" ", end="")
        if (i + n) <= j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
