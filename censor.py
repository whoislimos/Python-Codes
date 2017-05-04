def censor(text, word):
    
    mylist = text.split() #splits the string of words into a list of words
    
    for i in range(0, len(mylist)): 
        
        if mylist[i] == word: #if we found the word to be censored
            mylist[i] = "*" * (len(word)) # found word will be replaced by asterisks
            i = i + 1
            
    return " ".join(mylist) # join back the list of words into a string
        
    
censor("this hack is wack hack", "hacker") 


