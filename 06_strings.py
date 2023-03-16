import re

# value = input("enter a number: ")

# print(value + ' is my favourite number!')
# print('when you miltiply it by ten, this is what you get: ', int(value)*10 )

first_name = 'tanawal'
last_name = 'ameer'

note = 'a remarkable, leader, he was.'

first_name_cap = first_name.capitalize()
last_name_cap = last_name.capitalize()

print(first_name_cap)
print(last_name_cap)

leader_location = note.find('leader')
print(leader_location)

print(note[leader_location:])


five_digit_zip = '98101'
nine_digit_zip = '98101-0003'
phone_number = '234-567-8901'
five_digit_expression = r'\d{5}'

print(re.search(five_digit_expression, five_digit_zip))
print(re.search(five_digit_expression, nine_digit_zip))
print(re.search(five_digit_expression, phone_number))


miles = input('distance in miless, ')
print('Kilometers: ', float(miles) * 1.6093)