#!/usr/bin/python
# este es mi primer python_file en git
n = int(input("Enter an integer: "))
k = 0
pi = 0
while k <= n:
# the next one line is for the formula
    ls = 4*((((-1)**k)/(2*k + 1.0)))
    pi = pi + ls
    print("%d: %.25f" %(k, pi))
    k = k + 1

n_terms = n + 1

if n == 0:
    print("The result above is the first value of pi (with 15 decimal places) calculated with the Leibniz Series for the integer given by user.")
else:
    print("These are the first %d values of pi (with 15 decimal places) calculated with the Leibnitz Series for the integer given by user." %(n_terms))
