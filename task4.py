def listToString(s):
    str1 = ''
    return (str1.join(s))
def remove (string, number):
    new_string = list(string)
    del new_string[0:number]
    print (listToString(new_string))
read = str(input())
number = int(input())
remove(read, number)        