import sys, random

# Usage:
# stdin stream will be used. 
# The program will look for words in the similarWords "dictionary" 
# and might replace them with one of the similar words
#

# Change that a word is replaced if found in similarWords
REPLACE_CHANCE = 1

# Correct the style of the similar word
def matchWordStyle(word, similarWord):
	if len(word) > 1 & len(similarWord) > 1:
		# Capitalize new word if needed
		if word[0].isupper():
			similarWord[0] = similarWord[0].upper()

	return similarWord

# Choose a similar word based on a random float
def chooseSimilarWord(searchWord, similarWordsList):
	if random.random() <= REPLACE_CHANCE:
		# Choose a random word from the list
		retWord = random.randint(1, len(similarWordsList)-1)
		return matchWordStyle(searchWord, similarWordsList[retWord])
	# Return the original word
	return searchWord

# Search if searchWord is in similar words
def searchSimilarWords(searchWord):
	file = open("similarwords", 'r', encoding="utf-8")
	for line in file:
		lowerLine = line.rstrip().lower()
		# Check if a line matches with the searchWord
		if lowerLine.startswith((searchWord.lower())):
			similarWordsList = line.split("#")
			file.close()
			return chooseSimilarWord(searchWord, similarWordsList)

	file.close()
	return searchWord

def main(argv):
	for line in sys.stdin:
		line = line.rstrip()
		words = line.split(' ')
		printString = ""

		for word in words:
			printString += searchSimilarWords(word) + " "

		print(printString + '\n')


if __name__ == "__main__":
  main(sys.argv)
