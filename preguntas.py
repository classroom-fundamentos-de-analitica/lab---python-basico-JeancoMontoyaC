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



def pregunta_08():

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
            if p==t[1] and t[0] not in co:
                co+=[t[0]]
        tu+=[(int(p),sorted(co))]
    return sorted(tu)



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
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    for y in x:
        h=y[4].split(",")
        i=y[3].split(",")
        
        tu=(y[0],len(i),len(h))
        m+=[tu]

    return m



def pregunta_11():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    lis=[]
    for y in x:
        u=y[3].split(",")
        for uu in u:
            if uu not in m:
                m+=[uu]
    for mm in m:
        count=0
        for y in x:
            if mm in y[3]:
                count+=int(y[1])
        tu=(mm,count)
        lis+=[tu]


    return dict(sorted(lis))



def pregunta_12():
    x = open("data.csv", "r")
    x = [z.replace("\n", "") for z in x]
    x = [z.split("\t") for z in x]
    m=[]
    for y in x:
        if y[0] not in m:
            m+=[y[0]]
    
    lis=[]
    for mm in m:
        count=0
        for t in x:
            count2=0
            h=t[4].split(",")
            for y in h:
                po=(int(y.replace(y[0:4],"")))
                count2+=po
            
            if mm==t[0]:
                count+=count2
        tu=(mm,count)
        lis+=[tu]  
     
    return dict(sorted(lis))
print(pregunta_12())
