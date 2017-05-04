def anti_vowel(text):
    word = list(text)

    #checking each letter in word
    count = 0
    while count < len(word):
        if word[count] in "aeiouAEIOU":
            word.remove(word[count])
        else:
            count += 1

    return "".join(word)

print(anti_vowel('Hey look Words!'))
