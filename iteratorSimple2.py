# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:12:40 2019

@author: damian.campo
"""

# Create an iterator for range(3): small_value
small_value = iter(range(3))

# Print the values in small_value
print(next(small_value))
print(next(small_value))
print(next(small_value))

# Loop over range(3) and print the values
for num in range(3):
    print(num)

# Create an iterator for range(10 ** 100): googol
googol = iter(range(10 ** 100))

# Print the first 5 values from googol
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print(next(googol))
print('it can continue until:'.upper() + str((10 ** 100) - 1))