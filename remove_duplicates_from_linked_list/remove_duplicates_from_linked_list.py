class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return str(self.data)

class Linked_list:
    def __init__(self):
        self.head = None
    def listprint(self):
        head = self.head
        while(head is not None):
            print(head.data)
            head = head.next
    def remove_duplicates(self):
        head = self.head
        array = [head.data]
        prev_node = head
        head = head.next
        while (head is not None):
            if head.data in array:
                prev_node.next = head.next
            else:
                array.append(head.data)
                prev_node = head
            head = head.next

def compare_lists(list1, list2):
    head_1 = list1.head 
    head_2 = list2.head
    while(head_1 is not None and head_2 is not None):
        if(head_1.data != head_2.data):
            return False
        head_1 = head_1.next
        head_2 = head_2.next

    if head_1 is not None or head_2 is not None:
        return False
    return True

