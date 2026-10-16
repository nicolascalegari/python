# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def remover(head, valor):
    if head is None:
        return None

    if head.value == valor:
        return head.next


    while atual:
        if atual.value == valor:
            anterior.next = atual.next
            return head

        anterior = atual
        atual = atual.next

    return head