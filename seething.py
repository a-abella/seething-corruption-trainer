import os
from random import randint
import time

os.system('clear')

print '#################################'
print '#  SEETHING CORRUPTION TRAINER  #'
print '#################################\n\n\n'
print 'Instructions:'
print '-------------\n'
print 'This tool will display one of four ASCII representation of the Seething Corruption \nfloor patterns. It will only display the first pulse per pattern. Your objective \nis to determine the three spots the raid should stand in, starting with the first pulse. Your \nanswer should be in the format "xyz" to register correctly.\n\nYou may enter "exit" at any point to exit the trainer.\n\n\n'
raw_input("Press Enter to begin...")

pattern_one = 'llr'
pattern_two = 'rlp'
pattern_three = 'lrl'
pattern_four = 'rlb'

previous_num = 0

correct_count = 0
highest_streak = 0

on_switch = True

while on_switch:
	os.system('clear')
	
	while True:
		new_rand = randint(1,4)
		if new_rand != previous_num:
			pattern_num = new_rand
			break

	previous_num = pattern_num

	print 'Correct raid call streak: ' + str(correct_count)
	if correct_count > highest_streak:
		highest_streak = correct_count
	print 'Highest streak: ' + str(highest_streak) + '\n'

	pattern_file = 'patterns/pattern' + str(pattern_num) + '.txt'

	os.system('cat ' + pattern_file)

	kb = raw_input("\n\nCall the spots, then press Enter: ")

	if (pattern_num == 1 and kb == 'llr') or (pattern_num == 2 and kb == 'rlp') or (pattern_num == 3 and kb == 'lrl') or (pattern_num == 4 and kb == 'rlb'):
		correct_count += 1
		print '\nGood call!'
		time.sleep(1)
	else:
		correct_count = 0
		print '\nYou fucked up, Tore!'
		time.sleep(2)

