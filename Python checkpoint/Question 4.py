# Given a non-empty string and an integral n, return a new string where the
# char at index n has been removed. The value of n will be a valid index of
# a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive). 

# missing_char('kitten', 1) → 'ktten'    for example here we remove "i" which is located in the index 1

# missing_char('kitten', 0) → 'itten'   here we remove "k" which is in the index 0

# missing_char('kitten', 4) → 'kittn'   here we remove "e" which is in the index 4

def missing_char(word, num):
    if (num >= 0) and (num <= len(word)-1):
        temp = ""
        for i in range(0, len(word), 1):
            if i != num:
                temp+=word[i]
        return temp
    return "index out of range!"

text = missing_char("kitten", 0)
print(text)