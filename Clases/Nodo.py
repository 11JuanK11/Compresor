class Nodo:
    def __init__(self, char, cant_ocurrences):
        self.char = char
        self.cant_ocurrences = cant_ocurrences
        self.left = None
        self.right = None
        self.next = None

    def Print_Node(self):
            print(self.char + "|" + str(self.cant_ocurrences) + "-->", end = " ")

    def copy(self):
        new_node = Nodo(self.char, self.cant_ocurrences)
        return new_node
    