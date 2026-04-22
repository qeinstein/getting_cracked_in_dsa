# Reverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(8)
node2 = Node(10)
node3 = Node(12)
node4 = Node(14)
node5 = Node(16)
node1.next = node2
node4.next = node3
node3.next = node5
node2.next = node4  
#traversing the linkedlist
head = node1
current = head
print("Original linked list:")
while current:
    print(current.data, end=' -> ')
    current = current.next
print('None')

head = node1
current = head

#  reverse the linked list
prev = None
while current:
    next_node = current.next  # Store the next node
    current.next = prev       # Reverse the current node's pointer
    prev = current            # Move prev to the current node
    current = next_node       # Move to the next node
    
"""
None <- 1 <- 2 -> 3 -> 4 -> None
prev = None
current = 1

next_node = 2
current.next = None
prev = 1
current = 2

next_node = 3
current.next = 1
prev = 2
current = 3

next_node = 4
current.next = 2
prev = 3
current = 4

next_node = None
current.next = 3
prev = 4
current = None
"""

# Now prev is the new head of the reversed linked list
reversed_head = prev
# traversing the reversed linked list
current = reversed_head
print("Reversed linked list:")
while current:
    print(current.data, end=' -> ')
    current = current.next
print('None')