"""
The linked list data structure
"""

class ListNode:
    def __init__(self, val: object) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, ls: list):
        self.head = self.link(ls)
        self.size = len(ls)

    def gen_node(ls: list):
        for i in ls:
            yield ListNode(i)

    def link(self, ls) -> ListNode:
        curr = head = ListNode(None)
        for node in LinkedList.gen_node(ls):
            curr.next = node
            curr = curr.next
        return head.next

    def traverse(self):
        curr = self.head
        while curr:
            print("{} ->".format(curr.val), end=" ")
            curr = curr.next
        print("Null")


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4, 5, 6])
    ll.traverse()
