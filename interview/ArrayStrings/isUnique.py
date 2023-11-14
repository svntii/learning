#!/usr/bin/env python3

 # Implement an algorithm to determine if a string has all unique characters.

def isUnique(s: str) -> bool:
    '''
        args:
            s - str
        
        returns:
            bool

        Runtime O(N)
        uses the hashing from a set to keep track of unique chars in string
        if there is a colision return False
        if makes it the end of the String, return True

        considerations:
        is this algorithm case sensitive
    
    '''
    
    track = set()
    for c in s:
        if c in track:
            return False
        track.add(c)
    
    return True


def test1():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    '''expected is true'''
    return isUnique(s) == True

def test2():
    s = "Lopidfgcbshl"
    '''expected is true'''
    return isUnique(s) == True

def test3():
    s = "ABCDEFGHIJKLMNOPQRSTUVWXYZA"
    '''expected is false'''
    return isUnique(s) == False


def main():
    print(test1())
    print(test2())
    print(test3())



if __name__ == "__main__":
    main()