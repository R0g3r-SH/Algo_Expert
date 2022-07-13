def key(s1, s2):

    k = 0

    for i in range(len(s2)):
        if s1[k] == s2[i]:
            k+=1
            if (k== len(s1)):
                return True
    
    return False

print(key("AABBCCAABBCC","AABBCC"))