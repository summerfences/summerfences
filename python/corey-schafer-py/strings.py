
# strings can be with single or double quotes
# \ is escape key
message = 'Frank\'s Hello to the World'
message2 = "I said \"Hello to the World"
# prints over multiple lines
message3 = """Bobby's World was a good
cartoon in the 1990s"""
message4 = "hey"

# Print Welcome Message
print(message)

# prints length of string
print(len(message3))

# access character of string (length - 1)
print(message4[0])

# print characters up to BUT NOT INCLUDING index 5
print(message[0:5])
# or
print(message[:5])

# inversely, leaving the stop index blank goes to the end
print(message[7:])

# method = function that belongs to an object

# run lower method - make all characters lowercase
print(message2.lower())
# and uppercase
print(message2.lower())

# Counts how many times 'Hello' appears in the string
print(message2.count('Hello'))

# Find index of world in variable, returns -1 when doesn't exist
print(message3.find('World'))

# Replace first string in variable with the second
# needs new variable to return new variable strings
new_message = message.replace('World', 'Universe')
# or you can edit the variable itself
message = message.replace('World', 'Universe')

print(new_message)
print(message)

greeting = 'Hello'
name = 'Haley'

# printing string variables via direct call
message = '{}, {}. Welcome!'.format(greeting, name)
# fstring way of doing this. New, better, not widely used yet
# methods work like this too
message = f'{greeting}, {name.upper()}. Welcome!'

# tells you a list of methods that you can use with a variable
# print(dir(name))

# to see more info about how a method can affect a type of variable
# checking string variables
# print(help(str))

# directly passing a specific method to help works too
print(help(str.lower))
