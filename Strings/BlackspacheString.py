
def backspaceCompare(s,t):
    out1 = ""
    out2 = ""

    for i in s:
        if i == "#":
            out1 = out1[:-1]
        
        else:
            out1+= i
    for i in t:
        if i == "#":
            out2 = out2[:-1]
        
        else:
            out2+= i
    return out1 == out2
        


s = "ab##"
t = "c#d#"
print(backspaceCompare(s,t))
