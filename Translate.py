import sys

mode = 0
if(sys.argv[1]=="1"):
    mode = 1
input = sys.argv[2]
input = input.lower()
words = input.split(' ')

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def GetIndexString(i):
    outString = ''
    while(i >= 0):
        remainder = i % 26
        outString = alphabet[remainder] + outString
        i = i // 26
        i -= 1
    return outString

def GetStringIndex(name):
    outIndex = 0
    power = 0
    while(len(name) > 0):
        search = alphabet.index(name[len(name) - 1])
        if(power>0):
            search += 1
        outIndex += search * 26**power
        name = name[:-1]
        power += 1
    return outIndex

with open("Dataset100k.txt",encoding="utf-8") as dataset:
    if(mode==1):
        for i in range(0,len(words)):
            #print("(" + words[i] + ")=",end="")
            out = "NaN"
            index = GetStringIndex(words[i])
            count = 0
            dataset.seek(0)
            for line in dataset:
                if(count==index):
                    out = line[:-1]
                    break
                count += 1
            print(out,end="")
            if(i < len(words) - 1):
                print(" ",end="")
    else:
        for i in range(0,len(words)):
            #print("(" + words[i] + ")=",end="")
            out = "NaN"
            index = 0
            dataset.seek(0)
            for line in dataset:
                if(line[:-1]==words[i]):
                    out = GetIndexString(index)
                    break
                index += 1
            print(out,end="")
            if(i < len(words) - 1):
                print(" ",end="")