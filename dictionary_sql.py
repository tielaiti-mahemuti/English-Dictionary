import mysql.connector
from difflib import get_close_matches

connection = mysql.connector.connect(
    user = "ardit700_student",
    password = "ardit700_student",
    host = "108.167.140.122",
    database = "ardit700_pm1database"
)

while True:
    word = input("Enter word: ")

    cursor = connection.cursor()
    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    results = cursor.fetchall()

    if len(results) > 1:
        print(f"The defition for the word '{word}' is:")
        for i in range(len(results)):
            print(f"{i+1}: {results[i][1]}")
    elif len(results) == 1:
        print(f"The defition for the word '{word}' is:")
        print(f"1: {results[0][1]}")
    else:
        query = cursor.execute("SELECT Expression FROM Dictionary")
        results = cursor.fetchall()
        list_results = [''.join(i) for i in results]
        list_results = list(set(list_results))
        if get_close_matches(word, list_results):
            list_close_match = get_close_matches(word, list_results)
            print("Cound not find the word you searched for\nHere are some close matches:")
            for i in range(len(list_close_match)):
                print(f"Did you mean {list_close_match[i]}?")
                response = input("Yes (y) or No (n): ")
                if response.lower() == 'y':
                    query = cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{list_close_match[i]}'")
                    results = cursor.fetchall()
                    if len(results) > 1:
                        print(f"The defition for the word '{list_close_match[i]}' is:")
                        for i in range(len(results)):
                            print(f"{i+1}: {results[i][1]}")
                        break
                    else:
                        print(f"The defition for the word '{list_close_match[i]}' is:")
                        print(f"1: {results[0][1]}")
                        break
        else:
            print("Sorry could not find close match.")

    search_again = input("Do you wish to search for another word? ")
    if(search_again.lower() == 'y'):
        continue
    else:
        print("Hope you learned something new!")
        break