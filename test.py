# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:36:10 2020

@author: Server_LASER
"""

for num1 in range(2, 10, 1):
    print()
    print(num1, '단')
    for num2 in range(2,10):
        print('{} * {} = '. format(num1, num2), num1*num2)