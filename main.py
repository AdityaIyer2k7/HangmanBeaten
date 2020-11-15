from MakerMod.text import *

file=open("words.txt",mode='r')
fileR=file.read()

l = textFind(fileR,"\n")

print(l)

mlist=open("masterletters.txt")
mList=textFind(mlist.read(),"\n")

#Takes only correct length words
wLen=int(input("Length: "))
b=[]
for i in l:
    if len(i) == wLen:
        b.append(i)
    else:
        pass
l=b
print(l)

#Character elimination function
def charCtrl(pos,char):
    c=[]
    array=l
    for i in array:
        if i[pos-1]==char.upper() or i[pos-1]==char.lower():
            c.append(i)
        else:
            pass
    print(c)
    return(c)

def charRem(char):
    d=[]
    array=l
    for i in array:
        if not (char.upper() in i or char.lower() in i):
            d.append(i)
        else:
            pass
    print(d)
    return d

while True:
    denyAccept = input("Deny character (dc), accept character (ac), stuck (s) or done(d)? ")
    if denyAccept == "dc":
        l=charRem(input("Letter: "))
    elif denyAccept == "ac":
        l=charCtrl(int(input("Position: ")),input("Letter: "))
    elif denyAccept == "s":
        print(mList)
    elif denyAccept == "d":
        exit()
    else:
        print("Sorry, bad entry")
