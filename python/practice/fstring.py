''' practicing f strings
username = 'Alan'
print(f"Hello, {username}.") '''

import random as rnd
patient_num = rnd.randint(1, 6)

print("""Welcome to Booch industries.
To check-in, press 1.
To schedule an appointment, press 2.
To check out, press 3.""")

choice = input('Enter your selection:')

if int(choice) == 1:
    first_name = input('Enter your first name:')
    last_name = input('Enter your Last name:')
    print(f"Thank you,{first_name} {last_name}.")
    print(f"You are number {patient_num} in line.")
    print('A representative will see you shortly.')

elif int(choice) == 2:
    first_name = input('Enter your first name:')
    last_name = input('Enter your last name:')

elif int(choice) == 3:
