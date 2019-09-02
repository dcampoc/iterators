# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 14:28:51 2019

@author: damian.campo
"""

# Create a list of strings: mutants
mutants = ['charles xavier', 
            'bobby drake', 
            'kurt wagner', 
            'max eisenhardt', 
            'kitty pryde']

# Create a list of tuples: mutant_list
mutant_list = list(enumerate(mutants))

# Print the list of tuples
print(mutant_list)

print('first iterations'.upper())
# Unpack and print the tuple pairs
for index1,value1 in enumerate(mutants):
    print(index1, value1)

print('second iterations'.upper())
# Change the start index
for index2,value2 in enumerate(mutants,1):
    print(index2, value2)