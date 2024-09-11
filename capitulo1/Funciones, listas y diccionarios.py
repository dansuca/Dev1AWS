#Defining functions

def square_number():
    # function code here


#The following example declares the square_number function and adds a parameter called number.
def square_number(number):    
    # function code here 

#The following example is the code snippet from the video lesson. The snippet shows simple functions and commands in Python:

def say_hello():
    print("Hello, world!")
    
say_hello()
say_hello()
say_hello()

def square_number(number):
    return number**2
    
squared_number = square_number(2)
print(squared_number)

#Lists
# constructing a list
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
capacities = [10000, 12000, 9000, 8000, 10000, 11000, 9000]


#Python provides various methods to manipulate lists, including the following:

append(): Add an element to the end.
insert(): Insert an element at a specific index.
remove(): Remove the first occurrence of a specific element.
pop(): Remove and return an element by index.
len(): Get the number of elements in the list.
sort(): Sort the list in place.
reverse(): Reverse the order of elements.
index(): Find the index of the first occurrence of an element.
count(): Count the occurrences of an element.

#The following code snippet from the video lesson shows an example of using lists in Python:

# constructing a list
colors = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
capacities = [10000, 12000, 9000, 8000, 10000, 11000, 9000]

# operations on a list
print(sum(capacities) / len(capacities))
capacities.append(12000)
capacities.insert(0, 1000)
capacities.remove(9000)
print(colors.index('Blue'))
print('Red' in colors)
print('Red' not in colors)

# accessing items in a list
colors[0] = "Bright Red"
print(colors[0])
print(capacities[1])

# slice: list[from:to:step]
print(colors[:])        # ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(colors[2:])       # ['Yellow', 'Green', 'Blue', 'Indigo', 'Violet']
print(colors[:3])       # ['Red', 'Orange', 'Yellow']
print(colors[-4:])      # ['Green', 'Blue', 'Indigo', 'Violet']

print(colors[::-1])     # ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red']
print(colors[::2])      # ['Red', 'Yellow', 'Blue', 'Violet']

#To access the value that’s associated with a specific key, use the key name by putting it inside square brackets ([]). For example, see the following code:
info['ExtraInfo'] = 'This is extra info'
print(info['ImageId'])

#The following code snippet from the video lesson shows an example of using dictionaries in Python.

info = {
    'ImageId': 'ami-069eb5ebcbc6b0f91',
    'InstanceId': 'i-0c5c2bb0a41ef1b29',
    'InstanceType': 'm5.large'
}

info['ExtraInfo'] = 'This is extra info'
print(info['ImageId'])

del info['InstanceType']
print('ExtraInfo' in info) # True
print('ExtraInfo' not in info) # False

results = [
    { 'ImageId': 'ami-069eb5ebcbc6b0f91', 'InstanceId': 'i-0c5c2bb0a41ef1b29', 'ProductCodes': [] }
    { 'ImageId': 'ami-0a8cfe4ebc0397f86', 'InstanceId': 'i-0cf366ef0da64960c', 'ProductCodes': [] }
]