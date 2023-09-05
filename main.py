#get an input from the user then return an off brand version of the sentence. do this by replacing each word with a synonym of it. 
print("Starting...")
import json
import os
import random
import time
import webbrowser
from glob import glob
from http.client import responses
from multiprocessing.connection import wait
import requests
from nltk.corpus import wordnet

current_year = time.strftime("%Y")
app_id = "Your App ID"
app_key = "Your App Key"
endpoint = "thesaurus"
language_code = "en-us"
synonyms = []
antonyms = []
loaded_key = False
wrongkey = True
eck = 1
common_words = ["the", "and", "if", "or", "to", "of", "why", "you", "so", "it", "up", "we", "what", "this", "they", "them", "for"]
#get synonyms of a word and print them

def check_json_file():
        if glob("unoff_brandable_words.json"):
            return True
        else:
            #make a new json file
            return False
def unoff_brandable_words(string):
    #make a json file that contains the string.add()
    #first check if the file already exists
    json_file_exists = check_json_file()
    if json_file_exists == True:

        if string not in common_words:
            with open('unoff_brandable_words.json', 'r') as f:
                unoff_brandable_words = json.load(f)
                unoff_brandable_words.append(string)
                with open('unoff_brandable_words.json', 'w') as f:
                    json.dump(unoff_brandable_words, f)
                    print("unoff_brandable_words.json updated.")
    else:
        print("2")   
        with open('unoff_brandable_words.json', 'w') as f:
            json.dump([string], f)

def check_word_in_json_file(word):
    jsonfileexists2 = check_json_file()
    if jsonfileexists2 == True:
        with open('unoff_brandable_words.json', 'r') as f:
            unoff_brandable_words = json.load(f)
            if word in unoff_brandable_words:
                return True
            else:
                return False
    elif jsonfileexists2 == False:
        return False
    else:
        print("Catastrophic error saving error.")
        print("Error Info: " + str(jsonfileexists2) + " " + str(word) + " " + str(unoff_brandable_words))
        print("Please Submit this to the github issue tracker. At https://github.com/trevor050/OffBrandify/issues")
        openlink = input("Do you want to open the issue tracker? (Y/N) ")
        openlink.lower()
        if openlink == "y":
            webbrowser.open("https://github.com/trevor050/OffBrandify/issues")
        print("Attemping to continue, this may cause crash due to an unsable environment.")
        time.sleep(2)
        return False


def save_key_to_json(app_id, app_key):
    with open('key.json', 'w') as f:
        json.dump({"app_id": app_id, "app_key": app_key}, f)
    print("Key saved.")
    #load variable from json file
def load_key():
    global app_id
    global app_key
    #check to see if key.json exists
    def check_key_json():
        if glob("key.json"):
            return True
        else:
            print("saved key not found.")
            return False
    json_key_exists = check_key_json()
    if json_key_exists == True:
        with open('key.json', 'r') as f:
            key = json.load(f)
            app_id = key['app_id']
            app_key = key['app_key']
            endpoint = "thesaurus"
            fields = 'synonyms'
            strictMatch = 'false'
            word_id = "test"
            print("Key loaded.")
            #check to see if the key is valid
            url = "https://od-api.oxforddictionaries.com/api/v2/"+ endpoint+"/"+language_code+"/"+word_id  + '?fields=' + fields + '&strictMatch=' + strictMatch;
            headers = {"app_id": app_id, "app_key": app_key,"word_id":word_id, 'units': 'imperial'}
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                print("Key is valid.")
                return True
            elif response.status_code == 403:
                print("Key is saved, but invalid.")
                print("Deleting saved key...")
                #delete the key.json file
                os.remove('key.json')
                return False
    else:
        print("Saved key not found.")
        return False



def get_ninja_synonyms(word_id):
    api_url = 'https://api.api-ninjas.com/v1/thesaurus?word=' + str(word_id)
    headers = {
       #fake headers to look like a real browser
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                        'AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
    }
    response = requests.get(api_url, headers=headers)
    if response.status_code == 200:
        parsed_data = json.loads(response.text)
        synonyms = parsed_data.get('synonyms', 'No synonyms found')
        return synonyms
    else:
        print("Error: " + str(response.status_code))
        print(response.text)

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
        oneword = False
        #make a new array to hold the synonyms of the word
        synonyms_array = []
        ninja_synonyms = get_ninja_synonyms(word)
        if ninja_synonyms == None:
            ...
        else:
            synonyms_array.extend(ninja_synonyms)
            
        #remove all 1 character words from the array 
        for word in synonyms_array:
             for word in synonyms_array:
                if len(word) == 1 and word != "a" and word.isalpha() == True:
                    synonyms_array.remove(word)
        if len(synonyms_array) == 1:
            oneword = True
        elif len(synonyms_array) == 0:
            synonyms_array.append(word)
        #print every word in the array and its lenth

        random_synonym = random.choice(synonyms_array)
        synonyms.append(random_synonym)
        #if the synonym is the same as the word, pick a different synonym try up to 10 times
        if random_synonym == word and oneword == False:
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
                    print("Adding to unoff-brandable word list...")
                    time.sleep(0.3)
                    unoff_brandable_words(word.lower())
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
    Celeb_Prefixes = ["Will Ferrell", "Joe Biden", "Dwayne Johnson", "Michael Jordan", "Abe Lincoln", "Pope Francis", "Joseph Stalin", "Pablo Picasso", "Ellen DeGeneres", "Her Majesty Queen Elizabeth", "Dra'nakyuek, Destroyer of Worlds"]
    Celeb_Suffixes_2 = ["Jr", "Grandson", "Great Grandson", "The IV", "The V"]
    Celeb_Prefixes_Common = ["'s", " Presents", "'s All New"]
    Celeb_Prefixes_Rare = ["Foundation of Amrerica Presents:", "Inc. Presents:", "Assocation Presents:", "'s Leftover Sushi Presents:"]
    suffixs = ["Simulator", "Battle Royal", "Super", "Ultimate", current_year, "Offcial"]
    Suffixs2 = [ "The Game", "The Book", "The Movie", "The Netflix Adaptation", "Playing Cards", "The Broadway Musical", "Flavored Chips", "Makeup Palette"]
    Gamesuffixs = ["Wii U Edition", "Xbox 360 Edition", "Gamecube Edition", "Atari Edition", "Edcuation Edition", "Founders Edition", "Game Of The Year Edition"]
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
