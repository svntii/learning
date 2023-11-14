#!/usr/bin/env python3

# Given two strings,write a method to decide if one is a permutation of the other.



def isPermuation(s1: str, s2: str) -> bool:
    '''
    O(N)

    ignores white spaces, not case sensitivity
    '''
    d1 = {}
    d2 = {}

    for c in s1:
        if not c.isalnum():
            print(c)
            continue
        a = c.lower()
        d1[a] = d1.get(a, 0) + 1
    
    for c in s2:
        if not c.isalnum():
            continue
        a = c.lower()
        d2[a] = d2.get(a, 0) + 1

    if len(d1) != len(d2):
        return False
    

    return d1 == d2


def test1():
    s1 = "racecar"
    s2 = "carrace"
    return isPermuation(s1, s2) == True

def test2():
    s1 = "God"
    s2 = "dog    "
    return isPermuation(s1, s2) == True

def test3():
    s1 = "12323A"
    s2 = "alsxdf"
    return isPermuation(s1, s2) == False



def main():
    print(test1())
    print(test2())
    print(test3())

if __name__ == "__main__":
    main()

