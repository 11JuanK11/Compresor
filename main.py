import os
from Clases.Lista import Lista
from Clases.Nodo import Nodo
from Clases.Arbol_Huffman import Arbol_Huffman as arbol_h

def write_file(content, table_huffman):
    with open ("Archivos/Archivo_Comprimido.juan", "wb") as file:
        i = 0
        acum = ""
        relleno = ""
        while i < len(content):
            if content[i] == '\n':
                code = table_huffman['li']
            else:
                code = table_huffman[content[i]]
            j = i + 1
            if len(code) % 8 != 0:
                while len(code) % 8 != 0:
                        if len(content) > j:
                            if content[j] == '\n':
                                code += table_huffman['li']
                            else:
                                code += table_huffman[content[j]]
                            j += 1
                        else:
                            code = code + "0"
                            relleno += "0"
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
                k+=8
        return relleno

def descomprimir_archivo():
    tabla_huffman = read_huffman_codes()
    list = tabla_huffman.keys()
    relleno = tabla_huffman.pop('re')
    relleno = len(relleno)
    acum = ""
    i = 0
    cadena_binaria = ""
    with open ("Archivos/Archivo_Comprimido.juan", "rb") as file:
        datos_binarios = file.read()
        for byte in datos_binarios:
            cadena_binaria = cadena_binaria + format(byte, '08b') 
        
    with open ("Archivos/Archivo_Comprimir.txt", "w") as file2:
        string = ""
        while i < len(cadena_binaria) - relleno:
            acum = acum + cadena_binaria[i]
            for key in list:
                if acum == tabla_huffman.get(key):
                    if key != 'li':
                        string = string + key
                    else: 
                        string = string + "\n"
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
            if letter != '\n':
                node = Nodo(letter, 1)
            else:
                node = Nodo("li", 1)
            a.append(node)

    a.sort(False)
    b = arbol_h(a.copy())
    table_huffman = b.create_huffman_code(b.raiz, "")
    relleno = write_file(content, table_huffman)

    with open("Archivos/codigo_huffman.txt", "w") as file2:
        texto = f're: {relleno}\n' 
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
    
if os.path.isfile("Archivos/Archivo_Comprimir.txt"):
    tamaño_original = os.path.getsize("Archivos/Archivo_Comprimir.txt")
    comprimir_archivo()
    tamaño_comprimido = os.path.getsize("Archivos/Archivo_Comprimido.juan")
    reduccion_tamaño = (tamaño_original - tamaño_comprimido)/tamaño_original * 100
    print(f"tamaño archivo original: {tamaño_original} bytes")
    print(f"tamaño archivo comprimido: {tamaño_comprimido} bytes")
    print(f"Se redujo el tamaño del archivo original en un {reduccion_tamaño}%")
else:
    descomprimir_archivo()
    print("Se ha descomprimido el archivo")
