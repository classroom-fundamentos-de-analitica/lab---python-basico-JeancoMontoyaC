"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():

    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    
    d=0
    for w in x:
        d+=int(w[1])

    return d




def pregunta_02():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    for y in x:
        if y[0] not in m:
            m+=[y[0]]
    tu=()
    n=[]
    for q in m:
        u=0
        for t in x:
            if q==t[0]:
                u+=1
        tu=(q,u)
        n+=[tu]
    return sorted(n)



def pregunta_03():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    for y in x:
        if y[0] not in m:
            m+=[y[0]]
    tu=()
    n=[]
    for q in m:
        u=0
        for t in x:
            if q==t[0]:
                u+=int(t[1])
        tu=(q,u)
        n+=[tu]
    return sorted(n)


def pregunta_04():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    for i in x:
        m+=[i[2].split("-")]
   
    lista=[]
    lista2=[]
    for w in m:
        if w[1] not in lista:
            lista.append(w[1])
    for r in lista:
        cont=0
        for t in m:
            if r==t[1]:
                cont+=1
        tu=(r,cont)
        lista2+=[tu]
                

    return sorted(lista2)



def pregunta_05():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    lis=[]
    for y in x:
        del y[2:5]
    for y in x:
        if y[0] not in m:
            m+=[y[0]]
    for mm in m:
        lista=[]
        for xx in x:
            if xx[0]==mm:
                lista+=[int(xx[1])]
       
        tu=(mm,max(lista),min(lista))
        lis+=[tu]
    return sorted(lis)



def pregunta_06():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    lis=[]
    count=[]
    tu=[]
  
    for y in x:
        del y[0:4]
       
    for j in x:
        m+=j[0].split(",")

    for u in m:
        if u[0:3] not in lis:
            lis+=[u[0:3]]
    for t in lis:
        count=[]
        for i in m:
            if t==i[0:3]:
                count+=[int((i[4:]))]
        tu+=[(t,min(count),max(count))]
    return sorted(tu)




def pregunta_07():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    tu=[]
    for y in x:
        del y[2:]
        if y[1] not in m:
            m+=[y[1]]
    
    for p in m:
        co=[]
        for t in x:
            if p==t[1]:
                co+=[t[0]]
        tu+=[(int(p),co)]




    return sorted(tu)
print(pregunta_07())


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    return


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    return


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    return


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    return


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    return
