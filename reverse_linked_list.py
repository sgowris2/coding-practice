from singly_linked_list import SinglyLinkedList


def reverse_linked_list(head):

    previous = None
    current = head

    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next

    return previous


def reverse_linked_list_recursive(head):

    if head.next is None:
        return head

    temp = reverse_linked_list_recursive(head.next)
    head.next.next = head
    head.next = None

    return temp


if __name__ == '__main__':

    lst = SinglyLinkedList()
    lst.append('0')
    lst.append('1')
    lst.append('2')
    lst.append('3')
    lst.head = reverse_linked_list(lst.head)
    lst.head = reverse_linked_list_recursive(lst.head)

    print(lst)
