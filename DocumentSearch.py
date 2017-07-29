# CS61002: Algorithms and Programming 1 
# Name: Manga Srinivas Rao Baipalli    
# Date: 11/03/2016
# Lab05.py

# Python program to build search engine using Files and Dictionary.

import string

# Variable Initialization
flag=1
fileName = "ap_docs.txt" 

# Function for Try again.
def TryAgain():
    yesOrno= input("Do you want to try again(Y/N)?:")
    if(yesOrno=="Y" or yesOrno=="y"):
        print("==================================================")
        flag=1
    elif(yesOrno=="N" or yesOrno=="n"):
        exit()
    else:
        print("Invalid choice.")
        TryAgain()
    #-----------------------------------------------------------------

# Function to search words and storing them into dictionary.
def searchOption():   
    try:
        eachWord_dict={} #Dictionary 1 for each word in a file.
        eachSentence_dict={} #Dictionary 2 for each sentence in a file.
        print("\n******* SEARCH FOR DOCUMENT ********")
        searchWord =  input("Enter search word:")
        documentFile = open(fileName,'r')
        docKey=0
        textString=''
        for newLine in documentFile:
            if '<NEW DOCUMENT>' in newLine:
                eachSentence_dict[str(docKey)]=textString #adding each sentence in a dictionary.
                textString=''
                docKey+=1
            else:
                word_list=newLine.lower().split()
                textString+=newLine
                for word in word_list:
                    word=word.strip(string.punctuation) #Removing puctuations from text file.
                    if (word==''):
                        continue
                    if word in eachWord_dict:
                        eachWord_dict[word].add(docKey) #adding each word in a dictionary.
                    else:
                        newSet=set() #Set initialization 
                        newSet.add(docKey)
                        eachWord_dict[word]=newSet
        searchWordList = searchWord.split() #Splitting each word.
        listofsearch = []
        Found_count = 0
        for eachWord in searchWordList:
            for key, value in eachWord_dict.items():
                if (eachWord==key):
                    listofsearch.append(value) #apending found values to list.
                    Found_count+=1     
        if (Found_count>0):
            result  = set.intersection(*listofsearch) #Intersection operation on sets from list.      
            print("Documents fitting search:", *result,end=" ")
            print()
        else:
            print("Documents fitting search: Not found!")
            print()
        documentFile.close() #Closing the file
    except IOError as e:
        print("ERROR: File Not Found.") 
        exit()
    #-----------------------------------------------------------------        

# Function for read operation.    
def readOption():
    try: #Try block to handle file error.
        try: #Try block to handle value error.
            print("\n******* READ DOCUMENT ********")
            docNumber = int(input("Enter document number:"))
            documentFile = open(fileName,"r")     
            readWords = documentFile.read().split('<NEW DOCUMENT>') 
            myDictionary = {key: value for key, value in enumerate(readWords, 1)}
            if(docNumber<len(myDictionary)):
                print("Document #%s"%docNumber)
                for key, value in myDictionary.items():
                    if key == docNumber:
                        searchWord= value
                print("------------------------")
                print(searchWord)
                print("------------------------")
            else:
                print("ERROR: Invalid number.")
                TryAgain()
            documentFile.close() #Closing the file.
        except ValueError:
            print("ERROR: Invalid input.")
            TryAgain()
    except IOError as e:
        print("ERROR: File Not Found.")
        exit()
    #-----------------------------------------------------------------
    
# Main function of the program.
def mainFunction():
    global flag
    while flag:
        print("\nWhat would you like to do?")
        print("--------------------------")
        print("1.Search for documents \n2.Read Document \n3.Quit Program")
        print("--------------------------")
        choice = input("Enter your choice:")
        if (choice=="1"):
            searchOption() # Calling searchOption function to do search operation.
        elif(choice=="2"):
            readOption() # Calling readOption function to do read operation.
        elif(choice=="3"):
            exit() # Exiting program.
        else:
            print("Invalid choice.")
            TryAgain()

# Calling mainFucntion to run the program.    
mainFunction()  