# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def para_lista(head):
    valores = []
    atual = head

    while atual:
        valores.append(atual.value)
        atual = atual.next

    return valores