#Jesus Hurtado, CS 2302 - Data Structures, Lab #4 Option B, Fall 2018
# Create a Hash Table to insert all elements from the english words file from
# Lab 3 Option B, and then perform operations, such as, search, print anagrams,
# count anagrams, calculate average of comparisons, and load factor of HT.

import time

# HashTable class using chaining.
class HashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    def __init__(self, initial_capacity):
        # initialize the hash table with empty bucket list entries.
        self.initial_capacity = initial_capacity
        self.table = []
        for i in range(self.initial_capacity):
            self.table.append([])
      
    # Inserts a new item into the hash table.
    def insert(self, word):
        item = self.create_number_from_word(word)
        # get the bucket list where this item will go.
        bucket = hash(item) % len(self.table)
        bucket_list = self.table[bucket]

        # insert the item to the end of the bucket list.
        bucket_list.append(word)
        #print("Bucket: {} and bucket list so far: {}".format(bucket,bucket_list))
    
    # Method to create a number from a word entered by user, using base-26 approach    
    def create_number_from_word(self,strr):
        count=0    # Will keep track of the sum so far to calculate base-26 number
        length = len(strr)  #Number of letters in a word
        for letter in strr:
            length-=1   #Will subtract one and then that will be used as the exponent
            
            #In base-26, a = 1, b = 2......z = 26
            #Depending on the location of each digit, it will be raised to that
            #power starting from length-1
            if letter == 'a' or letter =='A':
                count+=((26**length)*1)
            elif letter =='b' or letter == 'B':
                count+=((26**length)*2)
            elif letter == 'c' or letter == 'C':
                count+=((26**length)*3)
            elif letter == 'd' or letter == 'D':
                count+=((26**length)*4)
            elif letter == 'e' or letter == 'E':
                count+=((26**length)*5)
            elif letter == 'f' or letter == 'F':
                count+=((26**length)*6)
            elif letter == 'g' or letter == 'G':
                count+=((26**length)*7)
            elif letter == 'h' or letter == 'H':
                count+=((26**length)*8)
            elif letter == 'i' or letter == 'I':
                count+=((26**length)*9)
            elif letter == 'j' or letter == 'J':
                count+=((26**length)*10)
            elif letter == 'k' or letter == 'K':
                count+=((26**length)*11)
            elif letter == 'l' or letter == 'L':
                count+=((26**length)*12)
            elif letter == 'm' or letter == 'M':
                count+=((26**length)*13)
            elif letter == 'n' or letter == 'N':
                count+=((26**length)*14)
            elif letter == 'o' or letter == 'O':
                count+=((26**length)*15)
            elif letter == 'p' or letter == 'P':
                count+=((26**length)*16)
            elif letter == 'q' or letter == 'Q':
                count+=((26**length)*17)
            elif letter == 'r' or letter == 'R':
                count+=((26**length)*18)
            elif letter == 's' or letter == 'S':
                count+=((26**length)*19)
            elif letter == 't' or letter == 'T':
                count+=((26**length)*20)
            elif letter == 'u' or letter == 'U':
                count+=((26**length)*21)
            elif letter == 'v' or letter == 'V':
                count+=((26**length)*22)
            elif letter == 'w' or letter == 'W':
                count+=((26**length)*23)
            elif letter == 'x' or letter == 'X':
                count+=((26**length)*24)
            elif letter == 'y' or letter == 'Y':
                count+=((26**length)*25)
            else:
                if letter == 'z' or letter == 'Z':
                    count+=((26**length)*26)
        return count    #Return the number obtained from making the calculations
    
    def get_average(self): #Method to get average number of comparisons to retrieve element in HT
        average_row=0
        for i in range(self.initial_capacity):
            average_row += len(self.table[i])
        average = average_row //self.initial_capacity
        return average
    
    def load_factor(self):  #Method to calculate load factor = #keys/#buckets
        number_of_keys=0
        buckets = self.initial_capacity
        for i in range(buckets):
            number_of_keys += len(self.table[i])
        lf = number_of_keys // buckets
        return lf
    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, word):
        key = self.create_number_from_word(word)
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # search for the key in the bucket list
        if word in bucket_list:
            # find the item's index and return the item that is in the bucket list.
            #return True
            
            item_index = bucket_list.index(word)
            return bucket_list[item_index]
        else:
            # the key is not found.
            return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        if key in bucket_list:
            bucket_list.remove(key)
            
            
def print_anagrams(word, engish_words, prefix=""): #Print anagrams method
    if len(word) <= 1:
        strr = prefix + word
        if engish_words.search(strr):##str in engish_words: 
            print(prefix + word)
            
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            
            if cur not in before: # Check if permutations of cur have not been generated. 
                print_anagrams(before + after, engish_words, prefix + cur)
               

def count_anagrams(counter,ht,word,prefix=""): #Count anagrams method
    if len(word) <= 1:
        strr = prefix + word
        if ht.search(strr): ##str in engish_words: 
            counter +=1
    else:
        for i in range(len(word)):
            cur = word[i: i + 1]
            before = word[0: i] # letters before cur 
            after = word[i + 1:] # letters after cur
            if cur not in before: # Check if permutations of cur have not been generated.   
                counter = count_anagrams(counter,ht,before + after, prefix + cur) 
    return counter                 


def number_words_inlist(file): # Method to know how many words are there in the file
    f1= open(file)
    words_inlist = f1.readlines()
    return len(words_inlist)
        
    
def words_into_ht(file,ht): #Method to insert each word from the file into HT
    f2 = open(file)
    words = f2.readlines()
    for word in words:
        word = word.replace('\n','')
        ht.insert(word)
    return ht
        
def main():     #Main method 
    print()
    print("Creating a Hash Table from the file containing the words in english language.....................")
    number_of_words = number_words_inlist("words.txt") #Get number of words in file
    #print(number_of_words)
    #hashT = HashTable(7)
    hashT = HashTable(number_of_words)  #Create an object of HashTable class
    english_words = words_into_ht("words.txt",hashT)
    
    #User is prompted to enter a word    
    get_word = input("Enter a word to create anagrams: ")
    print("------------------------------------------------------------------")
    #print anagrams found
    print_anagrams(get_word, english_words)
    get_count = count_anagrams(0,english_words, get_word)
    #print count of anagrams found
    print("Number of anagrams: {}".format(get_count))
    print("------------------------------------------------------------------")
    #Calculate average and call method to do so
    ave = english_words.get_average()
    print("Average number of comparisons to retrieve an element in this Hash Table: {}".format(ave))
    print()
    #Calculate load factor and print the result
    load = english_words.load_factor()
    print("Load Factor: {}".format(load))
    
    
     
    
main()       