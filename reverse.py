def reverse(text):
    
    #create new list to store reversed characters
    reversedWord = []
    
    #loop through the range of the given word
    for i in range(len(text)-1, -1, -1):
        
        #append each character of the given word to the new word
        reversedWord.append(text[i])
        
    return "".join(reversedWord)
