# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def inserir_final(head, valor):
    novo = Node(valor)

    if head is None:
        return novo

    atual = head

    while atual.next:
        atual = atual.next

    atual.next = novo
    return head