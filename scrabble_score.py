score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}       

#print score.keys() --- prints all the score keys
#print score.values() --- prints all the score values

def scrabble_score(word):
    
    word = str.lower(word) #convert string to lowercase
    total = 0
    
    for char in word:       #iterate through given word
        if char in score:   # if character is in dictionary score
            total = total + score[char] #sum up values
                    
    return total        
               
        
scrabble_score("Two") # Test case
    
