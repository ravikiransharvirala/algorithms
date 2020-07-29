#-*- coding: utf-8 -*-
"""
Question : Minimum number of steps to reduce the number to 1. 
Allowed operation:
sub by 1
add by 1
div by 2

Example:
input = 18
1. 18/2 = 9
2. 9+1 = 10 or 9-1 = 8
3. 10/2 = 5 or 8/2 = 4
4. 5+1 = 6 or 5-1 = 4 or 4/2 = 2
5. 6/2 = 3 or 4/2 = 2 or 2/2 = 1 (Bingo!)


Atleast 5 steps are required to reduce the given number to 1.

Identifying different possible cases

case 1: The first thing we check when we get the input is to make sure
the number is greater than 1. example: if num in [0,1] or if num > 1

case 2: If the number is logrithmic base of 2. for example: if the given
is 16 then the min number of steps that are required are math.log(num, 2)

case 3: If the number is even. We always divide the number by 2

case 4: If the number is odd. We either add 1 and sub 1.

"""
import math

def minSteps(num):
    if num in [0,1]:
        return 0
    elif math.log(num, 2).is_integer():
        return int(math.log(num, 2))
    elif num%2 == 0:
        return 1 + minSteps(num//2)
    return min(1 + minSteps(num - 1), 1+minSteps(num + 1))

print(minSteps(180))