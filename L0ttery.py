import math
import random
def num_possible_points(k, n, m):
	combinaton = math.factorial(n) / ((math.factorial(k) * math.factorial(n - k)))
	
	return combinaton * m

def get_player_number(k, n): # n = range of number and k = num of tickets
	i = 1
	list_user_num = []
	while i != k + 1:
		user_num = int(input(f'Enter number {i} must be (1 - {n}, cannot repeat) ')) #'(must be 1-',{n}','cannot repeat'):'))
		while user_num < 1 or user_num > n:
		 	user_num = int(input(f'Error - number must be between 1 and {n}. Try again: '))
		while user_num in list_user_num:
		 	user_num = int(input(f'Error - you’ve already entered {user_num}. Try again: '))
		list_user_num.append(user_num)
		i = i + 1
	
	return list_user_num

def get_player_bonus(m): # gets players bonus number
	bonus_num = int(input(f'\nNow enter your bonus number (must be between 1 - {m}): '))
	while bonus_num < 1 or bonus_num > n:
		bonus_num = int(input(f'Error - bonus number must be between 1 and {m}. Try again: '))

	return bonus_num


def get_drawn_num(k, n): # gets random generated nums
	ran_drawn_num = []
	for i in range(k):
		x = random.randint(1,n)
		ran_drawn_num.append(x)
	
	return ran_drawn_num

def get_drawn_bonus(m): # gets random bonus
	return random.randint(1,m)

def print_tickets(list_distinct, bonus): # prints the tickets when called
	for i in range(len(list_distinct)):
		x = list_distinct[i]
		for q in range(len(x)):
			print(x[q], end = ' ')
		print(f'|| Bonus {bonus[i]}')


def count_matches(list_A, List_b): # counts match with the winning ticket
	count = 0
	for i in range(len(list_A)):
		if list_A[i] in List_b:
			count += 1
	
	return count
print('DESIGN-A-LOTTO v1.0')
print('---------')
print('\n******')#Start of the game

print('it was said First Let\'s set up the game!')
k = int(input('\nHow many distinct numbers should the player pick? '))
while k < 1:
	k = int(input('How many distinct numbers should the player pick? '))

n = int(input(f'\nOK. Each of those {k} numbers should range from 1 to what? '))
while n < k:
	n = int(input(f'Error - range must be at least 1 to {k} to have a valid game. Try again: '))
m = int(input('\nOK. And finally, the bonus number should range from 1 to what? '))
while m > n:
	m = int(input('\nOK. And finally, the bonus number should range from 1 to what? '))
print('\n******')

print(f'There are {num_possible_points(k, n ,m)} possible ticket in this game.')
print(f'Each Ticket has a {1/num_possible_points(k, n ,m)} percent chance of winning the jackpot. Let\'s play good luck!')
num_tickets = int(input('\nHow mant tickets would you like to buy? '))
while num_tickets < 1:
	num_tickets = int(input('Error must enter at least 1 number! '))

i = 1
tot_user_tickets = []
tot_user_bonus = [] 
while i <= num_tickets:
	print(f'\n * Ticket #{i} of {num_tickets} *') # gets user numbers and adds them to the list. same for the bonus
	print(f'\nPick your {k} distinct numbers')

	x = get_player_number(k ,n)
	tot_user_tickets.append(x)
	y = get_player_bonus(m)
	tot_user_bonus.append(y)
	
	print('Your ticket so far:')
	print('--------')
	
	print_tickets(tot_user_tickets, tot_user_bonus)
	i += 1
	

print('\n*******')
print(f'The moment of truth has arrived! Here are the drawn numbers: it was said') # shows the winning number
winning_num = get_drawn_num(k,n)
for i in range(len(winning_num)):
	print(winning_num[i], end = ' ')
rand_gen_bonus = get_drawn_bonus(m)
print(f'|| Bonus: {rand_gen_bonus}')
best_ticket = 0 
most_matches = []


for i in range(len(tot_user_tickets)): # goes to index 0, 1 . etc...(also counts the matching numbers)
	nums = (tot_user_tickets[i]) # gets each list in 2D list
	matching_num = count_matches(nums, winning_num) # gets matching num with winning number and current list
	if best_ticket == matching_num:
		most_matches.append(nums)
	if matching_num > best_ticket:
		most_matches = []
		most_matches.append(nums)
		best_ticket = matching_num


if best_ticket > 0: # gets the tickets that have the most matching numbers
	include_bonus = []
	print('\nYour best ticket(s) ')
	for i in range(len(most_matches)): # goes through each list in 2D
		each_match = most_matches[i] 
		
		for char in range(len(each_match)):
			if tot_user_bonus[i] == rand_gen_bonus:
				print(each_match[char], end = ' ')
			else:
				print(each_match[char], end = ' ')
		
		print(f'|| Bonus: {tot_user_bonus[i]}')
	
	print(f'\nYou matched {matching_num}/{k} drawn numbers')

	
	if matching_num == len(winning_num):
		if rand_gen_bonus in tot_user_bonus:
			print('JACKPOT')
		else:
			print('You did not match the bonus')
			print('No JackPot this time. What did you expect')
	else:
		if rand_gen_bonus in tot_user_bonus:
			print('You did match the bonus though')
		else:
			print('You did not match the bonus')
		print('No JackPot this time. What did you expect')

else:
	print(f'\nYou matched 0/{k} drawn numbers')
	if rand_gen_bonus in tot_user_bonus:
		print('You did match the bonus though')
	else:
		print('You did not match the bonus')
	print('No JackPot this time. What did you really expect?')




