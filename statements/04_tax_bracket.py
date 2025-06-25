# Consider the tax bracket guide at https://thecollegeinvestor.com/wp-content/uploads/2023/11/TCI_-_2024_Federal_Tax_Brackets_1600x974.png
# It shows the tax bracket based on the income and filing status.  For example, a 'Single' with and 
# income $50000 will be in the 22% tax bracket
# Write a script that will prompt the user for an income, and filing status and then print the appropriate tax bracket 
# The user should be allowed to try this code upto 5 times.
# your code should use only if and while statements.  Do not use any
# data structures including lists, dictionaries, tuples, etc,
# Do not use advanced topics including class, or lambda or comprehension 
# or generators to complete this
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    
        income = float(input('Enter your income: $'))
        if income < 0:
            print('Income must be a non-negative number.')
            continue
        
        status = input('Enter your filing status (Single, Married Filing Jointly, Head Of Household): ').lower()
        
        if status not in ['single', 'married filing jointly', 'head of household']:
            print('Invalid filing status. Please enter one of the following: Single, Married Filing Jointly, Head Of Household')
            continue

        tax_bracket = 0

        if status == 'single':
            if income <= 11600:
                tax_bracket = '10%'
            elif income <= 47150:
                tax_bracket = '12%'
            elif income <= 100525:
                tax_bracket = '22%'
            elif income <= 191950:
                tax_bracket = '24%'
            elif income <= 243725:
                tax_bracket = '32%'
            elif income <= 609350:
                tax_bracket = '35%'
            else:
                tax_bracket = '37%'
        
        elif status == 'married filing jointly':
            if income <= 23200:
                tax_bracket = '10%'
            elif income <= 94300:
                tax_bracket = '12%'
            elif income <= 201050:
                tax_bracket = '22%'
            elif income <= 383900:
                tax_bracket = '24%'
            elif income <= 487450:
                tax_bracket = '32%'
            elif income <= 731200:
                tax_bracket = '35%'
            else:
                tax_bracket = '37%'

        elif status == 'head of household':
            if income <= 16550:
                tax_bracket = '10%'
            elif income <= 63100:
                tax_bracket = '12%'
            elif income <= 100500:
                tax_bracket = '22%'
            elif income <= 191950:
                tax_bracket = '24%'
            elif income <= 243700:
                tax_bracket = '32%'
            elif income <= 609350:
                tax_bracket = '35%'
            else:
                tax_bracket = '37%'

        else: 
            print('Invalid filing status. Please enter one of the following: Single, Married Filing Jointly, Head Of Household')
            attempts += 1
            continue

        print(f'Your tax bracket is: {tax_bracket}%')

        try_again = input('Do you want to try again? (yes/no): ').lower()
        if try_again != 'yes':
            print('Thank you for using the tax bracket calculator.')
            break

        attempts += 1
        print('Thank you for using the tax bracket calculator!')
       

#git commit -m 'updated 04_tax_brackets' and then
#git push

