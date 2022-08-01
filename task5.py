string = "Emma is good developer. Emma is a writer and Emma is an artist"
splited = string.split()
x = 0
Emma = 0
for i in range (0, len(splited)):
    if splited[x] == "Emma":
        Emma += 1
    else:    
        pass
    x += 1
print("Emma appeared %d times" % (Emma) )