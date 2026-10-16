# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def inverter(head):
    anterior = None
    atual = head

    while atual:
        proximo = atual.next
        atual.next = anterior
        anterior = atual
        atual = proximo

    return anterior