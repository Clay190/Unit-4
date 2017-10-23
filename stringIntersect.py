#Clay Kynor
#10/20/17
#stringUnion.py

def stringIntersect(word_1,word_2):
    total = " "
    word1 = word_1.lower()
    word2 = word_2.lower()
    for ch in word2:
        if ch in word1:
            total += ch
    return total
    
total = stringIntersect("Mississippi","Pennsylvania")
print(total)