# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def mesclar(l1, l2):
        dummy = Node(0)
        atual = dummy

        while l1 and l2:
            if l1.value <= l2.value:
                atual.next = l1
                l1 = l1.next
            else:
                atual.next = l2
                l2 = l2.next

            atual = atual.next

        atual.next - l1 if l1 else l2

        return dummy.next