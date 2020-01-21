import random

winnner='';

random_choice=random.randint(0,2)
if random_choice==0:
	computer_choice='rock'
elif random_choice==1:
	computer_choice='paper'
else:
	computer_choice='scissor'
user_choice=''

while (user_choice != 'rock' and
	   user_choice != 'paper' and
	   user_choice != 'scissor'):
	user_choice=input('rock, paper, scissor? ')
	

if computer_choice==user_choice:
	winnner='Tie'
elif computer_choice=='paper' and user_choice=='rock':
    winnner='Computer'
elif computer_choice=='scissor' and user_choice=='paper':
	winnner='Computer'
elif computer_choice=='rock' and user_choice=='scissor':
	winnner='Computer'
else:
	winnner='User'

if winnner=='Tie':
	print('We both chose', computer_choice + ', play again.')
else:
	print(winnner, 'won, I chose', computer_choice)