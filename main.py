word="aaaabbbdd"
e=""
for i in range(0,len(word)):
    count=1
    for j in range(i+1,len(word)):
        if word[i]==word[j]:
            count=count+1
            word=word[:j]+"0"+word[j+1:]
            print(word)

    if(count>1 and word[i]!="0"):
        g=str(count)
        d=g+word[i]
        e=e+d
print(e)


