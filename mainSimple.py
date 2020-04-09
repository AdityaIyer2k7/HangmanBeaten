from MakerMod.text import *

def wordsIn():
    file=open("words.txt",mode='r')
    fileR=file.read()
    return textFind(fileR,"\n")

l=wordsIn()
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
print(len(l))

#Character elimination function
def charCtrl(pos,charUp,charDown,lm=l,outPrint=True):
    c=[]
    array=l
    for i in array:
        if i[pos-1]==charUp or i[pos-1]==charDown:
            c.append(i)
        else:
            pass
    if outPrint:
        print(str(len(c)),"\n")
    else:
        pass
    return(c)

def charRem(charUp,charDown,lm=l,outPrint=True):
    d=[]
    array=l
    for i in array:
        if not (charUp in i or charDown in i):
            d.append(i)
        else:
            pass
    if outPrint:
        print(str(len(d)),"\n")
    else:
        pass
    return d

while True:
    denyAccept = input("Deny character (dc), accept character (ac), stuck (s), show (sh) or done(d)? ")
    if denyAccept == "dc":
        l=charRem(input("Capital: "),input("Small: "))
    elif denyAccept == "ac":
        l=charCtrl(int(input("Position: ")),input("Capital: "),input("Small: "))
    elif denyAccept == "s":
        print(mList)
        print("")
    elif denyAccept == "sh":
        print(l)
        print("")
    elif denyAccept == "d":
        exit()
    else:
        print("Sorry, bad entry")
