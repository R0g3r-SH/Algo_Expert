import string


def reverseWordsInString(string):
    # Write your code here.
    out = ""
    temp = ""
    for l in  string:
        if l == " ":
            out = " " + temp + out 
            temp  = ""
            continue
        temp += l
    
    out = temp + out
    return out


string ="AlgoExpert is the best!"
print(reverseWordsInString(string))