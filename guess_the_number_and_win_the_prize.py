
import random
def guess_the_number_and_win_the_prize():
	x=random.randint(11,20)
	n=int(input("Enter the number:"))		
	if x==n:
		return "Congratulations!"
	else:
		return "You loss"

print(guess_the_number_and_win_the_prize())
