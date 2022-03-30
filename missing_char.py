#Given a non-empty string and an int n, return a new string where the character at index n has been removed. 
# The value of n will be a valid index of a character in the original string


def missing_char(word, n):
    if n >=0 and n < len(word)-1 :
        return word[:int(n)] + word[int(n+1):]
