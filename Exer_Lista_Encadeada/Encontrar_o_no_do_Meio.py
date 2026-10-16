# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def meio(head):
        lento = head
        rapido = head

        while rapido and rapido.next:
            lento = lento.next
            rapido = rapido.next.next

        return lento.value