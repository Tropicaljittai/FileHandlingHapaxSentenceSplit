myFile1 = open('D:\download/2602116964\hi.txt', 'r')
readAll = myFile1.readlines()
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
words = []
for i in range(len(readAll)):
    word = readAll[i].split()
    for i in word:
        if i[-1] in punctuations:
            w = i.rstrip(i[-1])
            if w not in words:
                words.append(w)
        else:
            if i not in words:
                words.append(i)
print(words)