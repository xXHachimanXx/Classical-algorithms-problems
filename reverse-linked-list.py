class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data,end=" ")
            temp = temp.next

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr != None: # O(n)
        next = curr.next	
        curr.next = prev # reverse pointer
        prev = curr
        curr = next
    head = prev
    
    return head


linkList = LinkedList()
linkList.push(20)
linkList.push(4)
linkList.push(15)
linkList.push(85)
linkList.head = reverse_linked_list(linkList.head)

linkList.printList()
"""
Time complexity: O(n)
Space complexity: O(1)
"""

