import random

def random_int():
	random_n = random.randint(000, 1000)
	return random_n

def list_num(n):
	list_n = [value for value in str(n)]
	return list_n

def user_guess(n):
	n_len = len(str(n))
	maxrounds = (2**n_len) + n_len
	print("Let's play the mimsmind1 game. You have {} guesses.".format(maxrounds))
	count = 0
	# User types in first guess.
	user_n = input("Guess a {}-digit number: ".format(n_len))
	while count < maxrounds:
		# Checks if user input is an integer.
		try:
			user_n = int(user_n)
		except:
			user_n = input("Invalid input. Try again: ")
			continue
		count += 1
		if n == user_n:
			print("Congratulations. You guessed the correct number in {} times.".format(count))
			break
		# Ends the game if user guesses maximum amount.
		if count == maxrounds:
			print("Sorry you did not guess the number in {} tries. The correct number is {}.".format(maxrounds, n))
			break
		cow = 0
		bull = 0
		# Translates user input and random number into a list in order to check individual digit. 
		random_list = list_num(n)
		user_list = list_num(user_n)
		for index, value in enumerate(user_list):
			if value in random_list:
			# Bull: Checks if the same value is in the same location and 
			# replaces the value so it does not get checked again.
				if index == random_list.index(value):
					bull += 1
					user_list[index] = 'B'
		for index, value in enumerate(user_list):
			# Cow: Checks if the value is in the list with remaining numbers.
			if value in random_list:
				cow += 1
		user_n = (input("{} bull(s), {} cow(s). Try again: ".format(bull, cow)))


def main():
	user_guess(random_int())

if __name__ == '__main__':
	main()