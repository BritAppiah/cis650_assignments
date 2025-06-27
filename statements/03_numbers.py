# Print all the numbers between 1 and 100 that are evenly divisible an integer that is input by the user.
# Print how many numbers were printed
# for example, if the user inputs 17, the system would print
# 17, 34, 51, 68,.. 
# Write your code below
divisor = int(input('Enter a positive integer to find multiples between 1 and 100: '))
count = 0
print(f'Numbers between 1 and 100 that are evenly divisible by {divisor}:')
for number in range(1, 101):
    if number % divisor == 0:
        print(number, end=' ')
        count += 1 
print(f'\nTotal numbers divisible by {divisor}: {count}') 

# git push the changes with message '03_numbers'