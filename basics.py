print("Hello, World!")

my_name = "Jullie"
print("Hello " + my_name + "!")


coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)


# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)

# The modulo operator is indicated by % and gives the remainder of a division calculation

# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)

greeting_text = "Hey there! "
question_text = "How are you doing?"
full_text = greeting_text + question_text
print(full_text)


birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"

# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
print(full_birthday_string)
print(birthday_string, age, birthday_string_2)


total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
nice_sweater = 39.00
fun_books = 20.00

# Update total_price here:
total_price += nice_sweater + fun_books

print("The total price is", str(total_price))

