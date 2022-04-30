#Inputs the contents of a single message into a file
from nltk.stem import WordNetLemmatizer
def InputFunction(TextBoxValue = None):
    inputValue = TextBoxValue + '\n'
    EditDatabase = open("Database.txt", 'a')
    EditDatabase.write(inputValue)
    EditDatabase.close()
#string splitter
def StringSplitter(TextBoxValue = None):
    TextBoxValue

#word inserter into SQL spreadsheet
def Language_Spreadsheet():
    pass
#Lemmatizer for each individual word
def Lemmatizer():
    print("rocks :", lemmatizer.lemmatize("rocks"))
    print("corpora :", lemmatizer.lemmatize("corpora"))

    # a denotes adjective in "pos"
    print("better :", lemmatizer.lemmatize("better", pos="a"))

