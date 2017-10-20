#Clay Kynor
#10/20/17
#stringUnion.py

def stringIntersect(word1,word2):
    total = " "
    for ch in word2:
        if ch in word1:
            total += ch
    return total
    
var = stringIntersect("Mississippi","Pennsylvania")
print(var)