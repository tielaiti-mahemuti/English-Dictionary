import json
from difflib import get_close_matches

eng_dict = json.load(open("data.json")) #Import .json file
new_dict = dict((keys.lower(), values) for keys, values in eng_dict.items()) #Convert the .json file into dictionary with keywords and list of defintion for each keyword.

def translate(w):
    '''
    Function to take in user input
    Run the user input through .json keys
    Return definition of False if word does not exist
    Also checks for similar words in the case of a typo.
    '''
    word = w.lower()
    if word in new_dict.keys(): #If the word matches the list of keys, return definition
        return(new_dict[word])
    elif get_close_matches(word, new_dict.keys()): #If the word does not match, but has a close enough match
        list_words = get_close_matches(word, new_dict.keys()) #Find list of words that match user input
        print("We did not find the word you entered\nDid you mean any of the following possible words?")
        for i in range(len(list_words)): #Start showing words one by one
            print(f"{i+1}: {list_words[i]}")
            response = input("Yes (y) or No (n): ") #Ask for user input to see if this was the word they meant
            if(response.lower() == 'y'):
                return(new_dict[list_words[i]]) #If yes, return the word
                break
            else: #If not, keep going until the we reach the end of for loop
                continue
        print("Sorry, those were the closest matches we could find.") #If the end of for loop reached, say that was the closest matches found
        return(False)
    else:
        return(False)

while True:
    word = input("Enter word: ")
    word_def = translate(word)
    if(word_def != False):
        if(len(word_def) >= 1):
            for i in range(len(word_def)):
                print(f"{i+1}: {word_def[i]}")
        else:
            print(word_def)
    else:
        print("Word could not find the word in our dictionary.")
    go_again = input("Would you like to search for another word?\nYes (y) or No (n): ")
    if(go_again.lower() == 'y'):
        continue
    else:
        print("Thank for you using the dictionary!\nHope you learned some new defintions!!")
        break