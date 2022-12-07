with open('liste.txt', 'r') as f:
    liste = [line.rstrip().split('\n') for line in f if line.strip()]


liste2=[['Z','N'],['M','C','D'],['P']]
liste1=[['H','C','R'], 
        ['B','J','H','L','S','F'],
        ['R','M','D','H','J','T','Q'], 
        ['S','G','R','H','Z','B','J'],
        ['R','P','F','Z','T','D','C','B'],
        ['T','H','C','G'],
        ['S','N','V','Z','B','P','W','L'],
        ['R','J','Q','G','C'], 
        ['L','D','T','R','H','P','F','S']]


def test(liste):
    for i in range(len(liste)):
        toAdd=[]
        listing,b =liste[i][0].split(' from ')
        listingNum = listing[5:]
        listeDepart, listeArrive = b.split(' to ')
        
        toAdd = liste1[int(listeDepart)-1][-int(listingNum):]
        
        for j in range(len(toAdd)):
            liste1[int(listeDepart)-1].pop()  

        toAdd.reverse()

        for p in range(len(toAdd)):
            res=toAdd[p]
            
            liste1[int(listeArrive)-1].append(res)
                        
    for u in range(len(liste1)):
       print(liste1[u][-1:],"\n")
        
#test(liste)

    

def test2(liste):
    for i in range(len(liste)):
        print(liste1)
        toAdd=[]
        listing,b =liste[i][0].split(' from ')
        listingNum = listing[5:]
        listeDepart, listeArrive = b.split(' to ')
        
        
        
        toAdd = liste1[int(listeDepart)-1][-int(listingNum):]
        


        for j in range(len(toAdd)):          
            liste1[int(listeDepart)-1].pop()
            

        

        for p in range(len(toAdd)):
            res=toAdd[p]
            
            liste1[int(listeArrive)-1].append(res)
            
        
    for u in range(len(liste1)):
       print(liste1[u][-1:],"\n")
        
test2(liste)