# Rewrite this script to using case statements 
import random
def getAnswer(answerNumber):
    match answerNumber:
        case 1:
            return 'It is certain'
        case 2:
            return 'It is decidedly so'
        case 3:
            return 'Yes'
        case 4:
            return 'Reply hazy try again'
        case 5:
            return 'Ask again later'
        case 6:
            return 'Concentrate and ask again'
        case 7:
            return 'My reply is no'
        case 8:
            return 'Outlook not so good'
        case 9:
            return 'Very doubtful'


question=  input('What do you want to know about the future?')
r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

#git commit -m 'updated 02_magic' and then
#git push
