#lambda, map
print("Using lambda function")
add=lambda a,b:a+b
print(add(5,6))
print("Using Map function")
#map(function,iteratble)
numbers=[1,2,3,4,5]
result=map(lambda x:x*2,numbers)
print(list(result))