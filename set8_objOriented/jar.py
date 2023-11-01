"""implement a class called Jar with these methods:

    * __init__ should initialize a cookie jar with the given capacity, 
    which represents the maximum number of cookies that can fit in 
    the cookie jar. If capacity is not a non-negative int, though, 

    * __init__ should instead raise a ValueError.
    
    * __str__ should return a str with n a, where n is the number of 
    cookies in the cookie jar. For instance, if there are 3 cookies 
    in the cookie jar, then str should return "aaa"

    * deposit should add n cookies to the cookie jar. If adding that 
    many would exceed the cookie jar's capacity, though, deposit 
    should instead raise a ValueError.
    withdraw should remove n cookies from the cookie jar. Nom nom 
    nom. If there aren't that many cookies in the cookie jar, though, 
    
    * withdraw should instead raise a ValueError.

    * capacity should return the cookie jar's capacity.

    * size should return the number of cookies actually in the cookie 
    jar, initially 0.

Structure your class per the below. You may not alter these 
methods' parameters, but you may add your own methods."""

import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            return "Capacity must be a non-negative int"
        self.capacity = capacity
        self.cookies = 0

    def __str__(self):
        return self.cookies * "a"

    def deposit(self, n):
        self.cookies = self.cookies + n
        self.capacity =- 1

    def withdraw(self, n):
        if self.cookies < n:
            return "Not enough cookies in the jar"
        elif n < 0:
            return "Withdraw amount must be a non-negative int"
        else:
            self.cookies = self.cookies - n
            self.capacity =+ 1
        

    @property
    def capacity(self):
        return self.capacity

    @property
    def size(self):
        return self.cookies
    
    