def code(list):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            r1="jkl"
            r2="qnj"
            stnew = r1 + word[1:] + word[0] + r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    return(nwords)

def decode(list):
    nwords=[]
    for word in words:
        if(len(word)>=3):
            stnew =word[-4] + word[3:-4]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    return(nwords)

text = input("enter the text you want to code and decode : ")
words = text.split(" ")
choose = int(input("choose 0 for code and 1 for decode "))

if(choose==0):
    mytext = code(words)
    print(" ".join(mytext))
elif(choose==1):
    mytext = decode(words)
    print(" ".join(mytext))
else:
    print("choose correct option")
