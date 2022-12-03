#Opening and reading txt
with open('liste.txt', 'r') as f:
    liste = [line.rstrip() for line in f if line.strip()]


def day31(input):
    result=0
    for lines in input:
        first, second = lines[:len(lines)//2], lines[len(lines)//2:]
        for sym in first:
            if sym in second:
                if 'a'<=sym<='z':
                    result+= ord(sym)-ord('a') + 1
                    break
                else:
                    result+= ord(sym)-ord('A') + 1 + 26
                    break
    print(result)
day31(liste)
#https://stackoverflow.com/questions/3246262/python-how-do-i-assign-values-to-letters


def day32(input):
    result=0
    for lines in range(0, len(input),3):
        lines1, lines2, lines3= input[lines], input[lines+1], input[lines+2]
        for sym in lines1:
            if sym in lines2 and sym in lines3:
                if 'a'<=sym<='z':
                    result+= ord(sym)-ord('a') + 1
                    break
                else:
                    result+= ord(sym)-ord('A') + 1 + 26
                    break
    print(result)
day32(liste)