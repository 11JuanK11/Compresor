from Clases import Nodo
class Lista:

    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            iterator = self.head
            while iterator is not None:
                if iterator.char == node.char:
                    iterator.cant_ocurrences += 1
                    break
                else:
                    if iterator.next is None:
                        iterator.next = node
                        break
                    else:
                        iterator = iterator.next

    def print_list(self):  
        iterator = self.head
        while iterator is not None:
            print(iterator.char + "|" + str(iterator.cant_ocurrences) + "-->", end = " ")
            iterator = iterator.next

    def length(self):  
        length = 0
        iterator = self.head
        while iterator is not None:
            length += 1
            iterator = iterator.next
        return length
    
    def sort(self, reverse): 
        #reverse es una variable booleana que indica si se ordena de mayor a menor o viceversa
        list = []
        j = 0
        while j < self.length():
            Node = self.get_value(j).copy()
            Node.left = self.get_value(j).left
            Node.right = self.get_value(j).right
            list.append(Node)
            j+=1
        self.clear_list()
        if not reverse:
            #menor a mayor
            list.sort(key=lambda Node: Node.cant_ocurrences, reverse = False)
        else:
            list.sort(key=lambda Node: Node.cant_ocurrences, reverse = True)
        for i in list:
            self.append(i)


    def clear_list(Self):
        Self.head = None
                     
    def get_value(Self, indice):
        i = 0
        Node = Self.head
        while i < indice:
            Node = Node.next
            i+=1
        return Node
    
    def copy(self):
        new_list = Lista()
        i = self.head
        while i != None:
            new_node = i.copy()
            new_list.append(new_node)
            i = i.next
        return new_list
    
    def pop(self):
        nodo = self.head
        nodo_aux = self.head
        nodo = nodo.copy()

        nodo.right = nodo_aux.right
        nodo.left = nodo_aux.left
        
        self.head = self.head.next
        return nodo

    



