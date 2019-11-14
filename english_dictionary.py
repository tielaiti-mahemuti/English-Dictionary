import json
from difflib import get_close_matches

eng_dict = json.load(open("data.json")) #Import .json file in the form of a dictionary type
new_dict = dict((keys.lower(), values) for keys, values in eng_dict.items()) #Convert the keys into lowercase letters, this was the user has the freedom to enter inputs in both uppercase of lowercase.

while True:
	word = raw_input("Enter word: ") #Ask user for input (The computer I am using now is running Python 2.7 so I needed to use 'raw_input')
	if word.lower() in new_dict.keys(): #Convert the user input into lowercase before checking dictionary keys
		word_def = new_dict[word.lower()]
		if word_def > 0:
			for i in range(len(word_def)):
				print word_def[i]
		else:
			print word_def
	elif word[:3].lower() in new_dict.keys():
		close_match = difflib.get_close_matches(word.lower(), new_dict.keys(), 1)
		print "We were not able to find the word you are looking for.\nBut we did find some close matches!"
		response = raw_input("Did you mean this word? {}. Y or N? ", close_match)
		if response.lower() == 'y':
			word_def = new_dict[close_match.lower()]
			if word_def > 0:
				for i in range(len(word_def)):
					print word_def[i]
			else:
				print word_def[close_match]
		else:
			print "Sorry looks like we couldn't find a close match."
	elif word.lower() not in new_dict.keys(): #If the user input does not exits, print messege accordingly.
		print "Word does not exist.\nPlease double check it."
