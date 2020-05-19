#to find the valid word without dashes and spaces
def obtain_valid_word(words):
    word=random.choice(words)#will choose randomly a word from a list
    while "-" in word or " " in word:
       word=random.choice(words) 
    return word.upper()

#now we need to keep a track of the letters guessed and out of them which were correctly guessed
def hangman():
    lives=5
    word=obtain_valid_word(words)
    word_letters=set(word)    #letters in the word
    alphabet=set(string.ascii_uppercase)
    used_letters=set()        #to store the letters user has guessed
    while len(word_letters)>0 and lives>0:
        word_list=[letter if letter in used_letters else '-' for letter in word]
        print('current word:',' '.join(word_list))
        #getting user input
        user_ip=input('guess a letter: ').upper()
        
        if user_ip in alphabet-used_letters:
            used_letters.add(user_ip)
            if user_ip in word_letters:
                word_letters.remove(user_ip)
                print('')
            else:
                lives-=1
                print("remaining lives are:",lives)
        elif user_ip in used_letters:
            print("this lettter has already been used")
        #if the user enters invalid characters
        else:
            print("invalid entry")
    if lives==0:
        print('Sorry you lost \n')
        print('Correct word is:',word)
if __name__=='__main__':
    hangman()
