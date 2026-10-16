# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def buscar(head, valor):
    atual = head

    while atual:
        if atual.value == valor:
            return True

        atual = atual.next

    return False