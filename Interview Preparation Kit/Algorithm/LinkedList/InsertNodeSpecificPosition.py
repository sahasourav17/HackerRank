def insertNodeAtPosition(llist, data, position):
    # Write your code here
    newNode = SinglyLinkedListNode(data)
    k = 0
    curNode = llist
    while k != position-1:
        curNode = curNode.next
        k += 1
    temp = curNode.next
    curNode.next = newNode
    newNode.next = temp
    return llist