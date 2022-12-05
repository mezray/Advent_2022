#Opening and reading txt
with open('liste.txt', 'r') as f:
    liste = [line.rstrip().split(',') for line in f if line.strip()]


def test(liste):
    res=0
    for i in range(len(liste)):
        ab,bb = liste[i][0].split("-")
        ae,be = liste[i][1].split("-")
        if (int(ae) <=int(ab) and int(bb) <= int(be) or int(ae) >=int(ab) and int(bb) >= int(be)):
            res+=1
    print(res)
test(liste)

def test2(liste):
    res=0
    for i in range(len(liste)):
        ab,bb = liste[i][0].split("-")
        ae,be = liste[i][1].split("-")
        if (int(ae) <=int(ab) and int(bb) <= int(be) 
        or int(ae) >=int(ab) and int(bb) >= int(be)
        or int(ab) in range(int(ae),int(be))
        or int(bb) in range(int(ae),int(be))
        or int(ae) in range(int(ab),int(bb))
        or int(be) in range(int(ab),int(bb))):
            res+=1
    print(res)

test2(liste)