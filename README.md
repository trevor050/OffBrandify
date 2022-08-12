# OffBrandify
A Simple Python Script to make funny off-branded versions of any text input

## Get API key
Go to https://developer.oxforddictionaries.com/, and get a free api key.

## Version History

### Alpha Relase 2.0 - Aug 12 2022
- In Reference to "Tom Clancy's Rainbow Sig Siege" your off-brandifys can now be packed by celebrites there children, grandchildren, great grandchildren, there organizations, and more!
- Added Suffix that go on the end such as Simulator, Battle Royal, Ultimate and more
- Added Types like "____ the game" or "_____ the netflix adaptation, and more!
- Added Game Version like "Wii U edition" or "Education Edition", and more
- Each has a random chance of being added to your offbrandify. In future version's this feature will be optional.
- Sped up loading times


### Alpha Release 1.0 - Aug 10 2022
- Added Oxford Thesaurus API\n
- Remove NLTK API due to lack of results and unrelated words being given
- Sometimes the algorthm accidentally chooses the orginal word, this is now prevented
- Speed up loading time through optimization
- Better error handling should allow an output for hypothetically any input to produce a valid output.
- Changes to the final output better keeps the orginal string intact while still changing a lot
- Sped up strings with punctuation by allowing them to pass through much faster
- Fixed a bug were gibberish was given

### Pre-Alpha 1.1 Aug 9 2022
- Fixed a bug with punctuation causing error

### Pre-Alpha 1.0 Aug 8 2022
- Off-Brandify using NLTK Wordnet.
- Gets Lemmas from Wordnet and uses those to make off branded names for strings
- Takes each word, finds a lemma and returns it to the user creating an off branded name
- Added replayability without restarting
- Added Basic Error Handling to avoid python error
