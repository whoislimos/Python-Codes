# A Function that concatantes strings

def join_strings(words):
    result = ""
    for i in range(len(words)):
        result = result + words[i]
        print result
    return result
