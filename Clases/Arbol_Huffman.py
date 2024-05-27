from Clases.Nodo import Nodo
import os

class Arbol_Huffman:
    def __init__(self, Lista):
        self.creation(Lista)

    def creation(self, Lista):
        ruta_archivo = "./Archivos/Archivo_Comprimir.txt"  

        tamaño = os.path.getsize(ruta_archivo)
        i = 1
        while Lista.length() != 1:
            nodo_1 = Lista.pop()
            nodo_2 = Lista.pop()
            nodo_huffman = self.construction(nodo_1, nodo_2, i)
            i+=1
            Lista.append(nodo_huffman)
            Lista.sort(False)
        self.raiz = Lista.head
        
    def construction(self, Node_1, Node_2, iteration):
        char = "*"+ str(iteration)
        ocurrences = Node_1.cant_ocurrences + Node_2.cant_ocurrences
        Node_raiz = Nodo(char, ocurrences)
        if Node_1.cant_ocurrences <= Node_2.cant_ocurrences:
            Node_raiz.left = Node_2
            Node_raiz.right = Node_1
        else:
            Node_raiz.left = Node_1
            Node_raiz.right = Node_2
        return Node_raiz
    
    def print_tree(self, node):
        if node is not None:
            print(node.char + "|" + str(node.cant_ocurrences))
            try:
                print("hijo izq de " + node.char + ": "  + node.left.char + "|" + str(node.left.cant_ocurrences))
                print("hijo der de " + node.char + ": "   + node.right.char + "|" + str(node.right.cant_ocurrences))
            except:
                print("null")
            print("\n")
            self.print_tree(node.left)
            self.print_tree(node.right)
        else:
            print("")

    def create_huffman_code(self, node, codigo):
            if node.left is None and node.right is None:
                dict = { node.char: codigo}
                return dict
            else:
                dict1 ={}
                dict2 ={}
                dict1 = (self.create_huffman_code(node.left, codigo + "0"))
                dict2 = (self.create_huffman_code(node.right, codigo + "1"))
                dict1.update(dict2)
                return dict1

                    




