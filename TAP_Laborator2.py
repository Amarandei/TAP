from array import array
from http.client import OK
from pickle import FALSE, TRUE

nr_el=input ('Introdu nr de elemente al sirului')
list=[]
for i in range (0, nr_el):
    el=input('introdu elementul')
list.append(el)
print(list)
cautare_nr=input('introdu nr pe care il cauti')
list.sort()
OK=FALSE
def find_array(list, nr_el):
    for i in range(0, nr_el):
        if(list[i]==cautare_nr):
            print('nr cautat se afla pe pozitia', i)
            OK=TRUE
            break
        if(OK==FALSE):
            print('nr cautat nu se afla in sir')
            find_array(list, nr_el)
            print('lista sortata este:', list)
            