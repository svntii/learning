#!/usr/bin/env python3


'''
    implementation of linked list in python
'''

class Node():
    
    def __init__(self, val:int, n:'Node'=None):
        self.val = val
        self.next = n

    @staticmethod
    def search(root:'Node', val:int) -> bool:
        # O(n) search time
        node = root.copy()
        while node is not None:
            if node.val == val:
                return True
            node = root.next

        return False

    @staticmethod
    def insert(root: 'Node', new:'Node') -> 'Node':
        # O(1) insert at head stack
        new.next = root

        return new
    
    @staticmethod
    def pop(root: 'Node') -> 'Node':
        return root.next

    @staticmethod
    def delete(root:'Node', val:int) -> bool:
        # O(n) search and delete
        
        if root.val == val:
            return root.next

        prev = root
        node = root.next
        while node is not None:
            if node.val == val:
                prev.next = node.next
                return True
            prev = node
            node = node.next
        
        return False

    @staticmethod
    def print(root:'Node'):
        node = root
        while node is not None:
            print(node.val)
            node = node.next

if __name__ == "__main__":
    node = Node(1)
    node = Node.insert(node, Node(2))
    node = Node.insert(node, Node(3))
    Node.print(node)
    print("----")
    Node.delete(node, 2)
    Node.print(node)

