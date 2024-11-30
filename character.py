def matching_words(words):
    ctr = 0
    
    lst = []
    
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
            
    print("list of words with first and last character in \n",lst)
        
    return ctr
    
count = matching_words(["abc","cfc","xyc","aba","1221"])

print("Numbers of words in first and last character same: ",count)
        