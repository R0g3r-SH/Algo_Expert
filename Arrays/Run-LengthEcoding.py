
def runLengh (string):

    encode =[]
    curlen = 1

    for i in range(1,len(string)):
        currchar = string[i]
        prevchar = string[i-1]

        if currchar != prevchar  or curlen ==9:
            encode.append(str(curlen))
            encode.append(prevchar)
            curlen =0
        curlen +=1


    #handle the last run

    encode.append(str(curlen))
    encode.append(string[len(string)-1])

    print(encode)

    return "".join(encode)


print(runLengh('BBAAAAAAAAA'))

