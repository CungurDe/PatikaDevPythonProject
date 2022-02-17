# 1- Bir listeyi düzleştiren (flatten) fonksiyon yazın. Elemanları birden çok katmanlı listelerden
# ([[3],2] gibi) oluşabileceği gibi, non-scalar verilerden de oluşabilir.

emptyList = []
def flat(l):
    for i in l:
        if type(i) == list or type(i) == tuple:
            flat(i)
        else:
            emptyList.append(i)
flat([[1,'a',['cat'],2],[[[3]],'dog'],4,5])
print(emptyList)

'''
2- Verilen listenin içindeki elemanları tersine döndüren bir fonksiyon yazın. 
Eğer listenin içindeki elemanlar da liste içeriyorsa onların elemanlarını da tersine döndürün. 
'''

exampleInput= [[1, 2], [3, 4], [5, 6, 7]]


def Reverse(l):
    temporaryList= exampleInput[::-1]
    for i in temporaryList:
        if type(i) == list:
            i=i.reverse()
    print(temporaryList)
Reverse(exampleInput)
