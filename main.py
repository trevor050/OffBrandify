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
                    time.sleep(0.3)
                if i == 4:
                    print("This is a tricky one...")
                    time.sleep(0.8)
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
        #a list of celebrities.
    for i in range(len(synonyms)):
        synonyms[i] = synonyms[i].title()
    Celeb_Prefixes = ["Will Ferrell", "Joe Biden", "Dwayne Johnson", "Michael Jordan", "Abe Lincoln", "Pope Francis", "Joseph Stalin", "Pablo Picasso", "Ellen DeGeneres"]
    Celeb_Suffixes_2 = ["Jr", "II", "III", "IV", "V"]
    Celeb_Prefixes_Common = ["'s", " Presents", "'s All New"]
    Celeb_Prefixes_Rare = ["Foundation of Amrerica Presents:", "Inc. Presents:", "Assocation Presents:"]
    suffixs = ["Simulator", "Battle Royal", "Super", "Mega", "Ultimate"]
    Suffixs2 = [ "The Game", "The Book", "The Movie", "The Netflix Adaptation", "Playing Cards", "The Broadway Musical"]
    Gamesuffixs = ["Wii U Edition", "Xbox 360 Edition", "Gamecube Edition", "Atari Edition", "Edcuation Edition"]
    gamesuffixs = False
    #a 50% chance of getting everything except celeb prefix rare, the chance for celeb prefix common is 75%
    celeb_prefix = False
    celeb_prefix_2 = False
    celeb_prefixs_common = False
    celeb_prefix_rare = False
    suffix = False
    suffixs2_bool = False
    isgame = False
    if random.randint(1,2) == 1:
        celeb_prefix = True
        if random.randint(1,2) == 1:
            celeb_prefix_2 = True
            #one in 3 chance of getting celeb prefix rare
        if random.randint(1,3) == 1:
            celeb_prefix_rare = True
        else:
            celeb_prefixs_common = True
    if random.randint(1,2) == 1:
        suffix = True
    if random.randint(1,2) == 1:
            suffixs2_bool = True
                
    if celeb_prefix_rare == True:
        #pick random prefix from the celeb prefix array
        celeb_prefix = random.choice(Celeb_Prefixes)
        if celeb_prefix_2 == True:
            celeb_prefix = celeb_prefix + " " + random.choice(Celeb_Suffixes_2)
        random_prefix = random.choice(Celeb_Prefixes_Rare)
        random_prefix2 = celeb_prefix + " " + random_prefix
        synonyms.insert(0, random_prefix2)
    elif celeb_prefixs_common == True:
        #pick random prefix from the celeb prefix array
        celeb_prefix = random.choice(Celeb_Prefixes)
        if celeb_prefix_2 == True:
            celeb_prefix = celeb_prefix + " " +  random.choice(Celeb_Suffixes_2)
        random_prefix = random.choice(Celeb_Prefixes_Common)
        random_prefix2 = celeb_prefix + random_prefix
        synonyms.insert(0, random_prefix2)    
    if suffix == True:
        #pick random suffix from the suffix array
        if random.randint(1,4) == 1:
            random_suffix = random.choice(suffixs)
            random_suffix2 = random_suffix + " " + random.choice(suffixs)
        else:
            random_suffix = random.choice(suffixs)
            random_suffix2 = random_suffix
        synonyms.append(random_suffix2)
    if suffixs2_bool == True:
        #pick random suffix from the suffix array
        random_suffix = random.choice(Suffixs2)
        if random_suffix == Suffixs2[0]:
            isgame = True
            game_suffix = random.choice(Gamesuffixs)
            synonyms.append(random_suffix + " " + game_suffix)
        else:
            isgame = False
            random_suffix2 = random_suffix + " "
            synonyms.append(random_suffix2)  
                
    #make the first letter of every word upper case
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
            print("Invalid input, please enter Y or N")
            playagain()
    playagain()
        

if __name__ == "__main__":
    main()
    #print(synonyms)
