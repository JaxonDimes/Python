# Quadratic Formula Program v.1
"""
a = int(input("ax = "))
b = int(input("bx = "))
c = int(input("c = "))
num1 = b*-1
num2 = ((b**2)-(4*a*c))**0.5
num3 = 2*a
add = (num1 + num2)/num3
sub = (num1 - num2)/num3
print(add)
print(sub)
"""


# QFP v.2

a = int(input("ax = "))
b = int(input("bx = "))
c = int(input("c = "))
num1 = b*-1
num2 = ((b**2)-(4*a*c))**0.5
num3 = 2*a

add = (num1 + num2)
if add % num3 == 0:
    addition = add/num3
else:
    addition = f"{add}/{num3}"

sub = (num1 - num2)
if sub % num3 == 0:
    subtraction = sub/num3
else:
    subtraction = f"{sub}/{num3}"
print(addition)
print(subtraction)

