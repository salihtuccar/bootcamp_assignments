''' Assignment : Letter Count '''

#Task:

#Count the number of each letter in a sentence.
#Write a Python program that;
#takes a sentence from the user,
#counts the number of each letter/chars of the sentence,
#collects the letters/chars as a key and the counted numbers as a value in a dictionary.


string= input("Type a sentence to see hoy many times each letter occur in it")               

word_dict = {}              # We create an empty dict to expand it later with our letter counts

for i in string :           # We use for loop to check and count every letter in the sentence one by one

    if i in word_dict:        #We check if the letter already exists in the word_dict which we made previously to contain the counts of the letter
        word_dict[i] +=1       #If it already is in that dict, we change the value by adding 1
    else:
        word_dict[i] = 1      #if not we create a key by naming it 'i' each time for word_dict and assign it it's occurance which is 1