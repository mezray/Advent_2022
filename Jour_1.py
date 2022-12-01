#Opening and reading txt
with open('liste.txt', 'r') as f:
    liste = f.read().splitlines()   

#Replacing '' to '0'           
i=-1
for lines in liste: 
    i+=1
    if lines == "":
        liste[i]='0'
liste.append('0')

#Finding max value based on addition
def day11(input):
    res = 0
    Result=[]
    i=-1
    for elem in input:
        i+=1
        if input[i]!='0':
            res+=int(input[i])
        else:
            Result.append(res)
            res=0
    #print(max(Result)) #If Max Needed remove first #
    return(Result)
    

day11(liste)

#Finding 3 max values based on addition
def day12(input):
    Result=day11(input)
    FindMax(Result)
    
def FindMax(input):
    sortedList=(sorted(input))
    resultFinal=sortedList[len(sortedList)-1]+sortedList[len(sortedList)-2]+sortedList[len(sortedList)-3]
    print(resultFinal)
    
day12(liste)