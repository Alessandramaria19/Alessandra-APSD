sirul_de_caractere="Exemplu sir de caractere"
print(sirul_de_caractere[0])
for caracter in sirul_de_caractere:
    print(caracter)
#LISTE
lista_de_numere=[10,20,30,40,50]
lista_diversa=[1,'text',3,14,True,[1,2,3]]
#indexarea elementelor din lista
#incepe de la 0
print(lista_diversa[0])
print(lista_diversa[-1])
print(lista_diversa[1][0])
#segmentgare/ slicing liste
sublista=lista_de_numere[1:4:2]
print(sublista)

#operatori + si *
lista_1=[1,2,3]
lista_2=[4,5,6]
print(lista_1+lista_2)
print(lista_1*3)

#functii utile
#len(lista)-lingimea listei
lista=[10,20,30,40,50]
print(len(lista))

#max(lista)
#returneaza valoarea maxima din lista
print(max(lista))

#min(lista)
#returneaza valoarea minima
print(min(lista))


#adaugare element in lista
#append(element) -adauga element la finalul listei
print('-------')
lista=[1,2,3]
lista.append(10)
print (lista)

#insert(index,element)
lista.insert(1,77)
print(lista)

#stergere elemente din lista
#pop (index) - sterge si returneaza elementul de la indexul dat
element_sters=lista.pop(1)
print(lista)
print(element_sters)

#remove(element)- sterge prima aparitie
lista.remove(3)
print(lista)


#sortare lista
#sort()
#modifica sirul initial
print("------")
lista=[5,2,8,1,4]
lista.sort()
print(lista)
lista.sort(reverse=True)
print(lista)

#sorted(lista)
#returneaza o lista noua sortata
print("----------")
lista=[5,2,8,1,4]

lista_sortata=sorted(lista)
print(lista)
print(lista_sortata)

#cautarea elementelor in lista
#index(element) - returneaza indexul primei aparitii a sirului dat
lista=[5,2,8,"8",1,4,8]
index_element=lista.index(8)
print(index_element)

#count(element0
#returneaza de cate ori apare elementul in lista
print (lista.count(8))

# parcurgerea elementelor din lista
print("------")
#for element in lista
#parcurge element cu element, pe valori
lista=[101,220,301,405,50]
for element in lista:
    print(element)

#afisari elemente pare
print("Elemente pare:")
for element in lista:
    if element % 2 == 0:
        print(element)

#parcurgere cu index
#for index in range(len(lista))"
#pozitia elementului la care suntem:index
#valoarea elementului: lista[index]
print("--------")
lista=[101,220,301,405,50,66,772,88,99]
for index in range(len(lista)):
    print(index,lista[index])

#afisati nr pare de pe pozitiile divizibile cu 3
for index in range(len(lista)):
    #pozitia e index
    # valoare e lista[index]
    if lista[index]%2 == 0 and index%3==0:
        print(lista[index])

#parcurgerea cu while
#parcurgem cat timp mai avem elem in lista sau e indeplinita o conditie
#parcurgere tot pe index
print("---------")
lista=[10,20,30,'stop',40,50]
index=0
while index<len(lista) and lista[index]!='stop':
    print(lista[index])
    index+=1