class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def add_linked_lists(l1, l2):
    dummy_head = ListNode()
    current = dummy_head
    carry = 0

    while l1 or l2 or carry:
        sum_val = carry
        if l1:
            sum_val += l1.value
            l1 = l1.next
        if l2:
            sum_val += l2.value
            l2 = l2.next

        carry, val = divmod(sum_val, 10)
        current.next = ListNode(val)
        current = current.next

    return dummy_head.next

def print_linked_list(node):
    result = []
    while node:
        result.append(node.value)
        node = node.next
    return result

# Input lists
input1 = ListNode(2, ListNode(4, ListNode(3)))
input2 = ListNode(5, ListNode(6, ListNode(4)))

# Add the linked lists
output = add_linked_lists(input1, input2)

# Print the output in reversed order
reversed_output = print_linked_list(output)
print("Input1 =>", print_linked_list(input1))
print("Input2 =>", print_linked_list(input2))
print("Output =>", reversed_output)
