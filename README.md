# OffBrandify
A Simple Python Script to make funny off-branded versions of any text input

## Get API key
Go to https://developer.oxforddictionaries.com/, and get a free api key.

## Version History

### Full Release 1.0 - Aug 10 2022
- Added Oxford Thesaurus API\n
- Remove NLTK API due to lack of results and unrelated words being given
- Sometimes the algorthm accidentally chooses the orginal word, this is now prevented
- Speed up loading time through optimization
- Better error handling should allow an output for hypothetically any input to produce a valid output.
- Changes to the final output better keeps the orginal string intact while still changing a lot
- Fixed a bug were gibberish was given

### Beta 1.1 Aug 9 2022
- Fixed a bug with punctuation not working

### Beta 1.0 Aug 8 2022
- Off-Brandify using NLTK Wordnet.
- Gets Lemmas from Wordnet and uses those to make off branded names for strings

