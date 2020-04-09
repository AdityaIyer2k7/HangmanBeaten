import time

def wordSegro(word, sleeptm,cma=3,slash=3,spc=1,fs=7,ex=7,qm=7):
    for letter in word:
        print(letter, end='')
        if letter == ",":
            time.sleep(cma * sleeptm)
        elif letter == "/":
            time.sleep(slash * sleeptm)
        elif letter == " ":
            time.sleep(sleeptm)
        elif letter == ".":
            time.sleep(fs * sleeptm)
        elif letter == "!":
            time.sleep(ex * sleeptm)
        elif letter == "?":
            time.sleep(qm * sleeptm)
        else:
            pass
        time.sleep(sleeptm)
    print("")

def textFind (string,sep):
    words=[]
    word=""
    for i in string:
        if i!=sep:
            word = word+i
        else:
            words.append(word)
            word=""
    return words

def timer(totalTime):
    startTm = time.time()
    while True:
        now = time.time()
        diff = now - startTm
        if diff >= totalTime:
            return True
