#Modify this code so that it will reject non-positive inputs for age
name = input('What is your name?')
age  = int(input('What is your age?'))
if age <= 0:
    print('Age must be positive number')
elif name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are not over the hill')

#git commit -m 'updated 01_age_test' and then
#git push.
 