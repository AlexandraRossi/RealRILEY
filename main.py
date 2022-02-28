RawInput = str(input("write something"))
RefinedInput = str(RawInput + "\n")

EditDatabase = open("Database.txt", 'a')
EditDatabase.write(str(RefinedInput))
EditDatabase.close()
#executor tab
