# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def tamanho(head):
    contador = 0
    atual = head

    while atual:
        contador += 1
        atual = atual.next

    return contador