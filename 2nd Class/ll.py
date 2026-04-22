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

head = node1
current = head

# traversing the linkedlist
while current:
    print(current.data, end=' -> ')
    current = current.next
print('None')

