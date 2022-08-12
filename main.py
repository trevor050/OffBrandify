#get an input from the user then return an off brand version of the sentence. do this by replacing each word with a synonym of it. 
print("Starting...")
from glob import glob
from multiprocessing.connection import wait
from tkinter import W
import requests
import json
import requests
import nltk
from nltk.corpus import wordnet
import random
import time
from unittest import result
import demjson
app_id = "Your App ID"
app_key = "Your App Key"
endpoint = "thesaurus"
language_code = "en-us"
synonyms = []
antonyms = []
eck = 1
w = 0
#get synonyms of a word and print them
def get_oxford_synonyms(word_id):
    global endpoint
    endpoint = "thesaurus"
    fields = 'synonyms'
    strictMatch = 'false'
    url = "https://od-api.oxforddictionaries.com/api/v2/"+ endpoint+"/"+language_code+"/"+word_id  + '?fields=' + fields + '&strictMatch=' + strictMatch;
    headers = {"app_id": app_id, "app_key": app_key,"word_id":word_id, 'units': 'imperial'}
    response = requests.get(url, headers=headers)
    lookup = response.json()
    try:
        errorcheck = lookup['error']
        if errorcheck == "No entries were found for a given word":
            return "Error"
        
    except:
        ...
    #check if word is not a letter in the alphabet
    if word_id.isalpha() == False:
        return "Error"
    #check if there is an error given
    
        #return "No Synonyms Found"
    synonyms = lookup['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['synonyms']
    synonyms_list = []
    for synonym in range(len(synonyms)):
        synonyms_list.append(synonyms[synonym]['text'])
    return synonyms_list



def get_input():
    global split_game_name
    game_name = input("Please enter the name of something to off-brandify it. Make sure to only use real words: ")
    split_game_name = game_name.split()
    return split_game_name

#get synonyms of each word in the array, pick a random one, return only one synonym for each word in the array
def get_synonyms():
    global synonyms
    global split_game_name
    global eck
    global w
    w += 1
        
    print("Off-Brandifying...")
    #wait 1.2 seconds to make it look like the program is doing something
    time.sleep(1.2)
    for word in split_game_name:
        #make a new array to hold the synonyms of the word
        synonyms_array = []
        oxford_synonyms = get_oxford_synonyms(word)
        if oxford_synonyms == "Error":
            ...
        else:
            synonyms_array.extend(oxford_synonyms)

        #remove all 1 character words from the array 
        for word in synonyms_array:
             for word in synonyms_array:
                if len(word) == 1 and word != "a" and word.isalpha() == True:
                    synonyms_array.remove(word)
        
        if len(synonyms_array) == 0:
            synonyms_array.append(word)
        #print every word in the array and its lenth

        random_synonym = random.choice(synonyms_array)
        synonyms.append(random_synonym)
        #if the synonym is the same as the word, pick a different synonym try up to 10 times
        if random_synonym == word:
            for i in range(10):
                random_synonym = random.choice(synonyms_array)
                #if have tried 5 times print loading message
                if i == 1:
                    print("Still Loading...")
                    time.sleep(0.4)
                if i == 4:
                    print("This is a tricky one...")
                    time.sleep(1)
                #if reached 10 tries and still the same word, print error message
                if i == 9:
                    print("We Couldn't find a off-brandify for " + word)
                    break
                if random_synonym != word:
                    synonyms.append(random_synonym)
                    break
        #if word in synonyms is 1 letter, in the alphabet, and not "a", replace it with orginal word)
        if len(random_synonym) == 1 and random_synonym.isalpha() == True and random_synonym != "a":
            synonyms.remove(random_synonym)
            synonyms.append(word)


    return synonyms

#turn array into a string and return it
def get_synonyms_string():
    global synonyms
    global split_game_name
    synonyms_string = " ".join(synonyms)
    return synonyms_string

#make function that does all of these, allow user to input a sentence, get synonyms, get string, print string. allow them to do it as many times as they want.
def main():
    get_input()
    get_synonyms()
    if eck == 1:
        print(get_synonyms_string())
    #ask if they want to do it again
    def playagain():
        again = input("Do you want to do it again? (Y/N) ")
        again.lower()
        if again == "y":
            #clear arrays
            synonyms.clear()
            split_game_name.clear()
            main()
        elif again == "n":
            print("Thanks for using the off-brandifier!")
            exit()
        else:
            print("Invalid input")
            playagain()
    playagain()
        

if __name__ == "__main__":
    main()
    #print(synonyms)







