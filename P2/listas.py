# print("\033c")

# # #Ejemplo 1 Crear una lista de numeros e imprimir el contenido
# numeros=[23,33,45,8,24,0,100]
# print(numeros)

# lista=""
# for i in numeros:
#     # lista=lista+str(i)+", "
#     lista+=f"{i}, "
# print(f"[{lista}]")


# lista=""
# for i in range(0,len(numeros)):
#     lista+=f"{numeros[i]}, "
# print(f"[{lista}]")

# lista=""
# i=0
# while i<len(numeros):
#     lista+=f"{numeros[i]}, "
#     i+=1
# print(f"[{lista}]")

# #Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
# #1er FORMA
# palabras=["utd","tercer","cuatrimestre","TI"]
# palabra=input("Dame la palabra a buscar: ").strip()

# if palabra in palabras:
#     print(f"Encontre la palabra {palabra} en la lista")
# else:
#     print(f"No encontre la palabra {palabra} en la lista")

# #2DA FORMA
# palabras=["utd","tercer","cuatrimestre","TI"]
# palabra=input("Dame la palabra a buscar: ").strip()

# encontro=False
# for i in palabras:
#     if i==palabra:
#         encontro=True
# if encontro:
#     print(f"Encontre la palabra {palabra} en la lista")
# else:
#     print(f"No encontre la palabra {palabra} en la lista")
# #3er FORMA con len
# palabras=["utd","tercer","cuatrimestre","TI"]
# palabra=input("Dame la palabra a buscar: ").strip()

# encontro=False
# i=0
# while i<len(palabras):
#     if palabra[i]==palabra:
#         encontro=True
#     i+=1
# if encontro:
#     print(f"Encontro la palabra {palabra} en la lista")
# else: 
#     print(f"No encontro la palabra.")

# #4ta while
# palabras=["utd","tercer","cuatrimestre","TI"]
# palabra=input("Dame la palabra a buscar: ").strip()

# encontro=False

# #Ejemplo 3 Añadir elementos a la lista
# lista=[""]

# true=True
# while true:
#     valor=input("Dame un valor: ").strip()
#     lista.append(valor)
#     true=input("Ingresa True/False para continuar: ").strip()
#     if true=="False":
#         true=False

#2
# true="true"
# while true=="true":
#     valor=input("Dame un valor: ").strip()
#     lista.append(valor)
#     true=input("Ingresa True/False para continuar: ").strip().lower()
#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
agenda=[
        ["Carlos","6181234567"],
        ["Adrian","6182332456"],
        ["Luis","6182223444"]
    ]
# print(agenda)

# for i in agenda:
#     print(i)

# for r in range(0,3):
#     for c in range(0,2):
#         print(agenda[r] [c])

lista=""
for r in range(0,3):
    for c in range(0,2):
        lista+=f"[{agenda[r] [c]}, ]"
    lista+="\n"
print(lista)