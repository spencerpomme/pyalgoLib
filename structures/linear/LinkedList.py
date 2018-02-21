"""
The linked list data structure
"""

class ListNode:
    def __init__(self, val: object) -> None:
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self, ls: list=None):
        if ls:
            self.head = self.link(ls)
        self.size = len(ls) if ls else 0

    def gen_node(ls: list):
        if ls:
            for i in ls:
                yield ListNode(i)
        else:
            return None

    def link(self, ls) -> ListNode:
        curr = head = ListNode(None)
        for node in LinkedList.gen_node(ls):
            curr.next = node
            curr = curr.next
        return head.next

    def traverse(self):
        """
        Traverse a linked list
        :return: None
        """
        curr = self.head
        while curr:
            print("{} ->".format(curr.val), end=" ")
            curr = curr.next
        print("Null")

    def sethead(self, head):
        """
        Set head of a linked list to a given head.
        A roundabout way to give another constructor
        :return: ListNode
        """
        self.head = head


if __name__ == "__main__":
    l1 = LinkedList([1, 2, 3, 4, 5, 6])
    l1.traverse()
    l2 = LinkedList()
    l2.sethead(l1.head)
    l2.traverse()
