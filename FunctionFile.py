#Inputs the contents of a single message into a file
def InputFunction(TextBoxValue = None):
    inputValue = TextBoxValue + '\n'
    EditDatabase = open("Database.txt", 'a')
    EditDatabase.write(inputValue)
    EditDatabase.close()
#string splitter
def StringSplitter(TextBoxValue = None):
    TextBoxValue

#Lemmatizer for each individual word
