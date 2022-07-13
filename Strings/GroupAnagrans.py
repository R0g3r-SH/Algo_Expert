def groupAnagrams(words):
    # Write your code here.

    
    anagrams = {}
    for word in words:
        
        wordsort  = "".join(sorted(word))
        if wordsort in anagrams:
           anagrams[wordsort].append(word)
        else:
            anagrams[wordsort] = [word]
            
    return list(anagrams.values())
            
    pass
