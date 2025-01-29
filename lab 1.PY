array=[10,79,9,56,4,80,8]
num=int
largest=smallest=10
for num in array:
    if num> largest:
        largest=num
    elif num< smallest:
        smallest=num
print("largest number is",largest,"smallest number is",smallest)        