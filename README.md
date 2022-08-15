# OffBrandify
A Simple Python Script to make funny off-branded versions of any text input

## Get API key
When opening application user is guided on where to get API key and where to enter it. If 1000 calls limit is reached, make a new api with a different email, you can use a fake email.
## Version History

### Alpha Release 3.0 [Full Stack Update] - Aug 14 2022
- Added New Celebs
- Reworked All Celeb Suffixs (Jr, The V, Grandson, Etc)
- Added New Rare Celeb Suffixs ("X Assocation Presents", "Inc. Presents:", Etc)
- Added New Suffixs ("Battle Royal", "Offical", Etc)
- Added New Types ("The Book", "The Game", "The Netflix Adaptation"
- Added New Game Suffixs ("Wii U Edition", "Education Edition")
- All New API Key System
- When Opening Application For The First Time User Now Guided Through How To Get API Key. Auto Opens Websites Needed
- Saves API Key In Json File And Loads It Every Time Application Is Started
- Added Advanced Python Error Handling
- When Error Is Encountered User Is Now Given An Error Report With Information Useful To The Devs
- User Guided To Use Github Issues Page To Allow Devs To Hotfix Bugs Faster
- All New Key System Has Complex Error Handling So The User Has Minimal Issues
- Common Word List Of Words Without Synonyms So Limited API Calls Arent Wasted.
- For Every Word That The User Enters If It Has No Synonyms It Will Be Skipped Next Time
- Prevented An Issue Incase Of JSON Files Moved Or Deleted While Code Is Running. 
- When API Limit Is Reached New System Is In Place To Wait (In Case Words Per Minute Maxed) Or Guides User To Get A New API Key
- Fixed A Bug With Long Strings And Peroids
- Fixed All Known Bugs
- Sped Up Start Time
- Set Application Speed To Most Efficent Language 



### Alpha Release 2.0 [FrontEnd Update] - Aug 12 2022
- In Reference to "Tom Clancy's Rainbow Six Siege" your off-brandifys can now be backed by celebrites there children, grandchildren, great grandchildren, there organizations, and more!
- Added Suffix that go on the end such as Simulator, Battle Royal, Ultimate and more
- Added Types like "____ the game" or "_____ the netflix adaptation, and more!
- Added Game Version like "Wii U edition" or "Education Edition", and more
- Each has a random chance of being added to your offbrandify. In future version's this feature will be optional.
- Sped up loading times


### Alpha Release 1.0 [Backend Update] - Aug 10 2022
- Added Oxford Thesaurus API
- Remove NLTK API due to lack of results and unrelated words being given
- Sometimes the algorthm accidentally chooses the orginal word, this is now prevented
- Speed up loading time through optimization
- Better error handling should allow an output for hypothetically any input to produce a valid output.
- Changes to the final output better keeps the orginal string intact while still changing a lot
- Sped up strings with punctuation by allowing them to pass through much faster
- Fixed a bug were gibberish was given

### Pre-Alpha 1.1 [Backend Update] Aug 9 2022
- Fixed a bug with punctuation causing error

### Pre-Alpha 1.0 [Full Stack Update] Aug 8 2022
- Off-Brandify using NLTK Wordnet.
- Gets Lemmas from Wordnet and uses those to make off branded names for strings
- Takes each word, finds a lemma and returns it to the user creating an off branded name
- Added replayability without restarting
- Added Basic Error Handling to avoid python error
