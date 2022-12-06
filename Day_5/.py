with open('liste.txt', 'r') as f:
    liste = [line.rstrip().split('\n') for line in f if line.strip()]



liste1=[['H','C','R'], ['B','J','H','L','S','F'],['R','M','D','H','J','T','Q',], ['S','G','R','H','Z','B','J'],
['R','P','F','Z','T','D','C','B'],['T','H','C','G'],['S','N','V','Z','B','P','W','L'],['R','J','Q','G','C'], ['L','D','T','R','H','P','F','S']]


def test(liste):
    res=0
    for i in range(len(liste)):
        #move 8 from 7 to 1
        toAdd=[]
        toAdd.clear()
        listing,b =liste[i][0].split('from')
        listingNum = listing.removeprefix('move ')
        listeDepart, listeArrive = b.split(' to ')
        print(liste1[int(listeDepart)][-int(listingNum):])
        toAdd = liste1[int(listeDepart)][-int(listingNum):]
        print(toAdd)
        liste1[int(listeDepart)][-int(listingNum):].pop()
        print(liste1[int(listeDepart)][-int(listingNum):])
        print('res' ,liste1[0])
        for i in range(len(toAdd)):
            liste1[int(listeArrive)].append(toAdd[i])
    for i in range(len(liste1)):
        print(liste1[i][-1:])
        
test(liste)
        

        


test(liste)


    

