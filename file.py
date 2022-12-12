myFile1 = open('D:\download/2602116964\hi.txt', 'r')
readAll = myFile1.readlines()
myFile1 = open('D:\download/2602116964\hi.txt', 'a')
marks = ".?1"
exceptions = ["mr.", "mrs", "jr.", "i.e.", "ms."]
for i in range(len(readAll)):
    word = readAll[i].split()
    for i in word:
        if i.lower() in exceptions:
            myFile1.write(i + " ")
        elif i[-1] in marks:
            myFile1.write(i + "\n")
        else:
            myFile1.write(i + " ")
myFile1.close()