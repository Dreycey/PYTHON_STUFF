# -*- coding: utf-8 -*-
"""
Created on Tue May 08 20:00:17 2018

@author: Dreycey
"""

import tellurium as te
import roadrunner

r = te.loada("""

""")

print("I will now count my chickens:")

print("Hens", 25 + 30 / 6)
print("Roosters", 100 - 25 * 3 % 4)

print("Now I will count the eggs:")

g = float(1.00/4)

n = float((1 - g))

print (g)
print (n)
print(n+ 6)

print("Is it true that 3 + 2 < 5 - 7?")

print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)
print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)
print("Is it greater or equal?", 5 >= -2)
print("Is it less or equal?", 5 <= -2)