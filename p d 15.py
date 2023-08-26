def non_repeated(i):
    count = {}

    for char in i:
        if char in count:
            count[char] +=1 
        else:
            count[char] = 1

    for char in i:
        if count == 1:
            return char
        
    return '$'


#example 
word = print(str(input("enter a string")))
result = non_repeated(word)
print(result)