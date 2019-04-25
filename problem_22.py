import math
import time
import csv

t = time.time()
print('Problem 22: Names Scores');

#names = open("p022_names.txt","r")
def nameValue(name):
    #ASCII of 'A' is 65
    i = 0
    sum = 0
    letters = list(name)
    numLetters = len(letters)

    while i < numLetters:
        letters[i]
        sum = sum + ord(letters[i]) - 64 #convert to number, A = 1 etc.
        i += 1
    return sum

with open('p022_names.csv') as csvfile: #open file
    nameReader = csv.reader(csvfile, delimiter=',', quotechar='"') #converts to list
    for nameList in nameReader:
        nameList.sort() #sorts the name list alphabetically
        #print(nameList[0]) #returns the value of the name list
        #print(nameList.index('COLIN'))

i = 0
sum = 0
nameScore = 1;
nameAdjusted = 1;
print('Total number of names in this file: ', len(nameList))

while i < len(nameList): #iterate through the entire list of Names
    firstName = nameList[i]
    #print(type(firstName))
    nameScore = nameValue(str(nameList[i]))
    #print(type(nameScore))
    nameAdjusted = nameList.index(str(nameList[i]))
    #print(type(nameAdjusted))
    sum = sum + (nameScore * (nameAdjusted + 1))
    i += 1

print('The value of all the names in this file is: ', sum)

#name = nameValue(nameList[937])
#print (name)

elapsed = time.time() - t
print('Processing time: ', elapsed,'seconds')
