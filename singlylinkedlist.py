class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

def insert(head, data):
    cur = head
    while cur.next != None:
        cur = cur.next
    cur.next = Node(data)

def delete(head, data):
    cur = head
    prev = None
    while cur != None:
        if cur.data == data:
            if prev != None:
                prev.next = cur.next
                break
            else:
                print('error: you tried to delete HEAD.')
                print('use delete_head function.')
                break
        else:
            prev = cur
        cur = cur.next

def delete_head(head):
    return head.next

head = Node('node_0')
insert(head, 'node_1')
insert(head, 'node_2')
insert(head, 'node_3')

cur = head
while cur != None:
    print(cur.data)
    cur = cur.next

head = delete_head(head)
print('HEAD deleted')
cur = head
while cur != None:
    print(cur.data)
    cur = cur.next

