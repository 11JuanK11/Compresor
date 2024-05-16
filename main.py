import os
from Clases.Lista import Lista
from Clases.Nodo import Nodo
from Clases.Arbol_Huffman import Arbol_Huffman as arbol_h

def write_file(content, table_huffman):
    with open ("Archivos/Archivo_Comprimido.juan", "wb") as file:
        i = 0
        acum = ""
        while i < len(content):
            code = table_huffman[content[i]]
            j = i + 1
            if len(code) % 8 != 0:
                while len(code) % 8 != 0:
                        if len(content) > j:
                            code = code + table_huffman[content[j]]
                            j += 1
                        else:
                            code = code + "0"
                     #else:
                     #   i = j
                acum += code
                code = ""
                i = j
            else:
                acum += code
                code = ""
                i += 1
        numero_decimal = int(acum, 2)
        try:
            file.write(numero_decimal.to_bytes(len(acum)//8, 'big'))
        except:
            k = 0
            while k < len(acum):
                sub_acum = acum[k:(k+7)]
                numero_decimal1 = int(sub_acum, 2)
                file.write(numero_decimal1.to_bytes(len(sub_acum)//8, 'big'), end = "")
                k+=1

def descomprimir_archivo():
    tabla_huffman = read_huffman_codes()
    list = tabla_huffman.keys()
    acum = ""
    i = 0
    cadena_binaria = ""
    with open ("Archivos/Archivo_Comprimido.juan", "rb") as file:
        datos_binarios = file.read()
        for byte in datos_binarios:
            cadena_binaria = cadena_binaria + format(byte, '08b') 
        
    with open ("Archivos/Archivo_Comprimir.txt", "w") as file2:
        string = ""
        while i < len(cadena_binaria):
            acum = acum + cadena_binaria[i]
            for key in list:
                if acum == tabla_huffman.get(key):
                    string = string + key
                    acum = ""
                    break
            i+=1
        file2.write(string)
    os.remove("Archivos/Archivo_Comprimido.juan")
    os.remove("Archivos/codigo_huffman.txt")

                
            
                    
def comprimir_archivo():       
    a = Lista()
    content = ""
    with open ("Archivos/Archivo_Comprimir.txt", "r") as file:
        content = file.read()
        for letter in content:
            node = Nodo(letter, 1)
            a.append(node)

    a.sort(False)
    b = arbol_h(a.copy())
    table_huffman = b.create_huffman_code(b.raiz, "")
    write_file(content, table_huffman)

    with open("Archivos/codigo_huffman.txt", "w") as file2:
        texto = ''
        for clave, valor in table_huffman.items():
            texto += f"{clave}: {valor}\n"
        file2.write(texto)
        os.remove("Archivos/Archivo_Comprimir.txt")

def read_huffman_codes():
    table_huffman = {}
    with open("Archivos/codigo_huffman.txt", "r") as file:
        for line in file:
            list = line.split(":")
            caracteres_a_eliminar = " \n"
            for char in caracteres_a_eliminar:
                list[1] = list[1].replace(char, "")
            table_huffman[list[0]] = list[1]
    return table_huffman
    
descomprimir_archivo()

