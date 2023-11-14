#!/usr/bin/env python3

# Implementation of binary search tree
# bst.py

class BST():

    def __init__(self, val:int, l:'BST'=None, r:'BST'=None):
        self.val = val
        self.left = l
        self.right = r
    
    @staticmethod
    def insert(root: 'BST': new:'BST'):
        node = root
        while node is not None:
            if new.val < node.val:
                if node.left is None:
                    node.left = new
                    return
                node = node.left
            else:
                if node.right is None:
                    node.right = new
                    return 
                node = node.right
    
    @staticmethod
    def BFS(root: "BST"):
        