import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:    #converts first letter into Uppercase and then checks.
        return data[w.title()]
    elif w.upper() in data:    #converts into uppercase and then checks
        return data[w.upper()]
    elif (get_close_matches(w, data.keys())) != []:
        yn = input("Did you mean %s instead? Enter 'Y' if yes, or 'N' if no: " %get_close_matches(w, data.keys())[0])
        if yn == 'Y':
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == 'N':
            return "The word doesn't exist!"
        else:
            return "We didn't understand your entry!"
    else:
        return "Word doesn't exist!"

word = input("Enter the word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
    
