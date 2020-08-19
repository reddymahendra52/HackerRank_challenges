

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    x = head  
    y = head  
    while True:  
        if (x == None or x.next == None): 
            return 0 
        x = x.next.next
        
        y = y.next 
        if (x == y): 
            return 1

