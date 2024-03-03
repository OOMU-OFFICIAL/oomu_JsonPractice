import json

# Quick Python Practice. 
# Goal: Take user answers, store them in json file under certain Block.
# 1: Create a json file with data [Problem: format is incorrect!]
# 2: ON exit data is read back to user [user will be promopted for corrcet filename]
# 3: format json correctly. Will create a function to handle formatting sepeartely [will fix the format problem in #1]


print('''
     1 = take notes
     2 = Exit & Read Json (eg: filename = example.json, you enter example)
     3 = Coming soon
''')

menuAsk = input('Enter > ')

note_Data = {}
def takeNote():

        askUser = input("Add note: [y/n] ")
        classNote = input("Note Title (File Name): ")

        if askUser == 'Y' or askUser == 'y':
            
            note_Data[classNote] = {
                "Article-Title" : input("Article Title:"),
                ''
                "Sub-Section" : input("SubSection:  "),
                ''
                "Main-Points" : input(f"Main Points (3-5):"),
                '' 
                "Summary" : input("Broad Summary:  ")
            }

            filt_data = {key: value for key, value in note_Data.items() if value}
  

            with open (f'{classNote}.json', 'a') as outfile:
                if outfile.tell() == 0:
                    json.dump(filt_data, outfile, indent= 4)
                else:
                    outfile.write(",\n")
                    json.dump(filt_data, outfile, indent= 4,separators=(",",":"))

                print()
                againT = input('Read for another note? [y/n]')

                if againT == 'y':
                    takeNote()
                else:
                    exit()
        
        else:
            print()
            print('Shuttin down')
            exit()

def readJson(usrjson):
    with open(f'{usrjson}.json', 'r') as infile:
        try:
            data = json.load(infile)
            print(data)
        except FileNotFoundError:
            print("Error: File not found.")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format.")


if menuAsk == str(1):
    takeNote()
elif menuAsk == str(2):
    madeFile = input('Json File name (case-sensitive): ')
    readJson(madeFile)
    exit()

