class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.value)
            current = current.next
        return result

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def sort_linked_list(head):
    sorted_head = None
    current = head
    while current:
        next_node = current.next
        sorted_head = sorted_insert(sorted_head, current)
        current = next_node
    return sorted_head

def sorted_insert(head, node):
    if not head or node.value < head.value:
        node.next = head
        return node
    else:
        current = head
        while current.next and current.next.value < node.value:
            current = current.next
        node.next = current.next
        current.next = node
    return head

def merge_sorted_lists(head1, head2):
    dummy = Node()
    tail = dummy
    while head1 and head2:
        if head1.value < head2.value:
            tail.next, head1 = head1, head1.next
        else:
            tail.next, head2 = head2, head2.next
        tail = tail.next
    tail.next = head1 if head1 else head2
    return dummy.next

# Reverse
ll = LinkedList()
for val in [1, 2, 3, 4, 5]:
    ll.append(val)
reversed_head = reverse_linked_list(ll.head)
reversed_list = LinkedList()
reversed_list.head = reversed_head
print("Reversed list:", reversed_list.to_list())  # [5, 4, 3, 2, 1]

# Sort
ll2 = LinkedList()
for val in [5, 1, 3, 2, 4]:
    ll2.append(val)
sorted_head = sort_linked_list(ll2.head)
sorted_list = LinkedList()
sorted_list.head = sorted_head
print("Sorted list:", sorted_list.to_list())  # [1, 2, 3, 4, 5]

# Merge
ll3 = LinkedList()
ll4 = LinkedList()
for val in [1, 3, 5]:
    ll3.append(val)
for val in [2, 4, 6]:
    ll4.append(val)
merged_head = merge_sorted_lists(ll3.head, ll4.head)
merged_list = LinkedList()
merged_list.head = merged_head
print("Merged list:", merged_list.to_list())  # [1, 2, 3, 4, 5, 6]
