with open('liste.txt', 'r') as f:
    liste = f.read().strip()



i=0
while len(set(liste[:4])) != 4:
    liste = liste[1:]
    i+=1
print('1st res=',i+4)

while len(set(liste[:14])) != 14:
    liste = liste[1:]
    i+=1
print('2nd res=',i+14)