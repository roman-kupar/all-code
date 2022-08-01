string = str(input())
lenght = len(string)
x = lenght
result = ''
for x in range(0, lenght):
    x = lenght - 1
    result = result + string[x]
    lenght -= 1
print(result)
# def reverse (string, x):
#     new_string = list(string)
#     lenght = len(new_string) 
#     x = lenght - 1
#     print(string[x])
# string = str(input())
# lenght = len(string)

