# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tem_clico(head):

    lento = head
    rapido = head

    while rapido and rapido.next:
        lento = lento.next
        rapido = rapido.next.next

        if lento is rapido:
            return True

    return False
