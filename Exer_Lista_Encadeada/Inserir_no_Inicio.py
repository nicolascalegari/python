# Classe base
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def inserir_inicio(head, valor):
    novo = Node(valor)
    novo.next = head

    return novo