#Opening and reading txt
with open('liste2.txt', 'r') as f:
    liste = [line.rstrip() for line in f if line.strip()]

#B/Y paper
#A/X rock
#C/Z scissors

def day21(input):
    res = 0
    for i in range(len(input)):
        if input[i][0]=='A':
            #Rock against Paper = Win
            if input[i][2]=='Y':
                res+=6+2
            #Rock against Rock = Draw
            if input[i][2]=='X':
                res+=3+1
            #Rock against Scissors = Loose    
            if input[i][2]=='Z':
                res+=3
                  
        if input[i][0]=='B':
            #Paper against Paper = Draw
            if input[i][2]=='Y':
                res+=3+2
            #Paper against Rock = Loose 
            if input[i][2]=='X':
                res+=1
            #Paper against Scissors = Win
            if input[i][2]=='Z':
                res+=6+3
        
        if input[i][0]=='C':
            #Scissors against Paper = Loose
            if input[i][2]=='Y':
                res+=2
            #Scissors against Rock = Win 
            if input[i][2]=='X':
                res+=6+1
            #Scissors against Scissors = Draw
            if input[i][2]=='Z':
                res+=3+3
    #print(res)


def day22(input):
    res = 0
    for i in range(len(input)):
        if input[i][2]=='Y':
            if input[i][0]=='A':
                res+=3+1
            if input[i][0]=='B':
                res+=3+2   
            if input[i][0]=='C':
                res+=3+3

                  
        if input[i][2]=='X':
            if input[i][0]=='A':
                res+=3
            if input[i][0]=='B':
                res+=1
            if input[i][0]=='C':
                res+=2
        
        if input[i][2]=='Z':
            #Scissors against Paper = Loose
            if input[i][0]=='A':
                res+=6+2
            #Scissors against Rock = Win 
            if input[i][0]=='B':
                res+=6+3
            #Scissors against Scissors = Draw
            if input[i][0]=='C':
                res+=6+1
    print(res)

day22(liste)