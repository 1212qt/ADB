# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 09:31:34 2020

@author: student216
"""
import math 
import numpy as np
import matplotlib.pyplot as plt

# Exercise 1

k = 1240 * math.sqrt(7)
m = 4467
l = 2j
d = k+ m
c = d+l

# Exercise 2

print(f'{d:.20}')

# Exercise 3

r = 17
h = 33
s = 2 * math.pi * r * r + 2 * math.pi * r * h

# Exercise 4
"""
    comment
"""
#comment

# Exercise 5
x1 = 10
t = 2
r = 5

B = (x1 + r)/(r * math.sin(2*x1) + 3.3456) * math.pow(x1, t*r)
print(B)

# Exercise 6
a = math.sqrt(2)

M = [[a, 1, -a], [0, 1, l], [-a, a, 1]]
Minv = np.linalg.inv(M)
Mt = np.linalg.det(M)

# Exercise 6

P = np.array([np.random.randint(0,10,4),np.random.randint(0,10,4),np.random.randint(0,10,4),np.random.randint(0,10,4)])
print(P[1,1])
print(P[3,3])
print(P[3,2])

# Exercise 7

w = np.poly1d([60, 28, 43, 3, -7, 5])
roots = np.roots(w)

# Exercise 8

taba = np.arange(0, 50, 1.2)
tabl = np.linspace(2.0, 3.0, num=5)


# Exercise 9

def fun1(x):
    return x**2-3*x

x = np.linspace(-1,1)
y = fun1(x)
plt.plot(x, y)

x = np.linspace(-5,5)
plt.plot(x, y)

x = np.linspace(0, 5)
plt.plot(x, y)

# Exercise 10

def Q(m, v):
    return m*v*v/2

resultjoul = Q(2.5, 60000/3600)
resultkcal = Q(2.5, 60000/3600) * 0.000239005736

x = np.linspace(200, 0)
y = Q(3, x)

plt.plot(x, y)


# Exercise 11

class Quaternion:
    def __init__(self, a, i, j, k):
        self.a = a
        self.i = i
        self.j = j
        self.k = k
        
    def __add_(self, other):
        return Quaternion(self.a + other.a,
                          self.i + other.i,
                          self.j + other.j
                          self.k + other.k)
        
    def __sub__(self.other):
        return Quaternion(self.a - other.a,
                          self.i - other.i,
                          self.j - other.j
                          self.k - other.k)
        
    def __mul__(self, other):
        return Quaternion(self.a * other.a,
                          self.i * other.i,
                          self.j * other.j
                          self.k +* other.k)
        
    def __div__(self, other):
        return Quaternion(self.a / other.a,
                          self.i / other.i,
                          self.j / other.j
                          self.k / other.k)
        
    def conjugate(self):
        self.i = -self.i
        self.j = -self.j
        self.k = -self.k
        
    def normalise(self):
        return math.sqrt(self.a**2 + self.i**2 + self.j**2 + self.k**2=
    