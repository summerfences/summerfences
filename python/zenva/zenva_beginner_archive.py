print('Hello world!')

# Variables

x_example = 15
print(x_example)
print(type(x_example))

x_example = 15.0
print(x_example)
print(type(x_example)) 

# Boolean
is_game_over = True
is_game_not_over = False

print(is_game_over)
print(type(is_game_over))
print(is_game_not_over)

# boolean can convert to other data types

is_game_over = 1
print(type(is_game_over))
print(is_game_over)

# Strings
name = "Frank"
print(name)
print(type(name))
instructor_name = "Nimish"

# DIFFERENT FROM BOOLEAN
is_game_over = "True"

# IS NOT THE SAME AS INTEGER 
age_as_a_string = "23"
age = 23

name_and_age = "Frank: {}".format(age)
print(name_and_age)

# praticing with .format
taffy = 5
suzy = 11

taffy_and_suzy = "{} and {}".format(taffy, suzy)
print(taffy_and_suzy)

taffy_text = "Taffy"
suzy_text = "Suzy"
and_word = "and"
taffy_suzy_text = "{} {} {}".format(taffy_text, and_word, suzy_text)
print(taffy_suzy_text)

# arithmetic and assignment operators
# + / - * = % // **

# shorthand can be used for all operators

one = 1
three = 3
one += three
print(one)

two = 8
two %= 3
print(two)

two = 1
two += 1
print(two)

two = 3
two -= 1
print(two)

two = 4
two /= 2
print(two)

two = 5
two //= 2
print(two)

x_position = 10
forward = x_position + 1
backward = x_position - 1

# x_position = x_position + 1
x_position += 1

print('five and two')

# floor division throws out remainder
floor_division = 5 // 2
print(floor_division)

remainder = 5 % 2
print(remainder)

exponent = 5 ** 2 
print(exponent)

first_name = 'Konstantinos '
last_name = "Palaiologos"
print(first_name + last_name)

# can add strings too 
first_name += last_name
print(first_name)


# floor division, remainder ditched
vegeta = 18003 // 2
print(vegeta)

two = 5 // 2
print(two)

# comparision and logical operators
# > >= < <= == != not or and

x_position = 1
end_position = 10

is_at_end = x_position == end_position
print(is_at_end)

is_at_halfway = x_position >= 5
print(is_at_halfway)

is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

x_position = 10
end_position = 10

is_at_end = x_position == end_position
print(is_at_end)

is_at_halfway = x_position >= 5
print(is_at_halfway)

is_at_halfway = x_position >= end_position / 2
print(is_at_halfway)

print(is_at_end)
print(not is_at_end)

not_is_at_end = not is_at_end

# is at end means is_at_end == True
score = 10
# will set to true if both conditoins are true 
is_game_over = score >= 10 and is_at_end
print(is_game_over)

# is at end means is_at_end == True
score = 9
# will set to true if one condition is true
is_game_over = score >= 10 or is_at_end
print(is_game_over)

first_name = 'haley '
last_name = 'julie'

full_name = first_name == 'haley ' and last_name == 'julie'
print(full_name)

#multple statements per line with ; 
print('one'); print(two)

# making a list
list = [3, True, "String"]
print(list)
list = [3, True, "String", "Extra"]
print(list)

# print one Value (zero is index)
print(list[1])

# print list length
print(len(list))

# change element
list[0] = 6
print(list[0])

# select a range with :
# STOPS at last value, doesnt include
print(list[0:3])

# add element to end of list
list.append(25)
print(list)

# insert element in specified position
# position , value
list.insert(1,"Insert")
print(list)

# remove a value from list
list.remove(6)
print(list)

# remove element based on position
del(list[2])
print(list)