#!/usr/bin/env python3 


# Implementation of doubly-linked list


class DoublyLinkedList():

    def __init__(self, val: int, l:'DoublyLinkedList' = None, r:'DoublyLinkedList' = None):
        self.val = val
        self.next = l
        self.prev = r

    @staticmethod
    def insert(root:'DoublyLinkedList', new:'DoublyLinkedList') -> 'DoublyLinkedList':
        # Insert at head
        new.next = root
        root.prev = new
        new.prev = None
        return new

    @staticmethod
    def insertAt(root:'DoublyLinkedList', new:'DoublyLinkedList', index:int):
        node = root
        where = 0
        while node is not None and where <= index:
            if where == index:
                result = DoublyLinkedList.updateNode(new, node, node.next)
                return result
            node = node.next
            where += 1

        return False

    @staticmethod
    def updateNode(node:'DoublyLinkedList', prev_node:'DoublyLinkedList', next_node:'DoublyLinkedList') -> bool:
        if node is None:
            return False

        if prev_node is not None:
            prev_node.next = node
            node.prev = prev_node
        else:
            node.prev = None
        
        if next_node is not None:
            next_node.prev = node
            node.next = next_node
        else:
            node.next = None
        
        return True
    
    @staticmethod
    def print(root:'DoublyLinkedList'):
        node = root
        while node is not None:
            print(node.val)
            node = node.next

    @staticmethod
    def delete_node(root: 'DoublyLinkedList', node_to_delete:int):
        node = root
        while node is not None:
            if node.val == node_to_delete:
                result = DoublyLinkedList.updateNode(node.prev, node.prev, node.next)
                return result
            node = node.next
        return False


if __name__ == "__main__":
    node = DoublyLinkedList(1)
    node = DoublyLinkedList.insert(node, DoublyLinkedList(2))
    node = DoublyLinkedList.insert(node, DoublyLinkedList(3))

    DoublyLinkedList.insertAt(node, DoublyLinkedList(4), 1)
    DoublyLinkedList.print(node)
    print("----")
    DoublyLinkedList.delete_node(node, 2)
    DoublyLinkedList.print(node)
    print("----")


    

