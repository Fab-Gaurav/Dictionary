#Importing the important Libraries
import json
from difflib import get_close_matches

#Loadinging data file
data = json.load(open("data.json"))


#Searching and Returning the value of word
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0 :
        print("Did you mean '%s' insterd" %get_close_matches(word, data.keys())[0])
        decide = input("Press Y for Yes and N for No : ")
        if decide == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif decide == "N":
            return("Try for other word.")
        elif decide == "n":
            return("Try for other word.")
        else:
            return("Wrong choice... Please select Y or N ")
    else:
        print("OOPS!!\nTry for other word.")


#Getting and Printing the word and it meaning resp.
word = input("Enter the word you want to search : ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(" ->",item)
else:
    print(output)