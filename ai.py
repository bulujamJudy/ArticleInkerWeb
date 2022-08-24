
symbols = "! @ # $ % ^ & * ( ) _ - + = { } [ ] ."
symbols=symbols.split()
result = []
article = generated[0]
article = article[:]

for i,c in enumerate(article):
    print(i,c)
    if c.isupper() and article[i-1].islower():
        result.append("\n")
    result.append(c)

print ("".join(result))


'''
    if i==0:
        continue

    prevIsNotSym = True
    for ch in generated[i-1]:
        if ch in symbols:
            prevIsNotSym = False
            break
    
    if type(word) == str and prevIsNotSym:
        char = [i for i in word]
        if char[0].isupper():
            result.append()
    result.append(word)

print(result)
'''

