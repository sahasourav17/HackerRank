def insertNodeAtTail(head, data):
    temp = head
    new_node = SinglyLinkedListNode(data)
    
    if temp is None:
        return new_node
    while temp.next:
        temp = temp.next
    temp.next = new_node
    return head