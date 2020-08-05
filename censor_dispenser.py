import random

# These are the emails you will be censoring. The open() function is opening the text file that the
# emails are contained in and the .read() method is allowing us to save their contexts to the following
# variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

''' The following method takes in two arguments. The first is the text that needs to be
    censored and the second being the email that needs censoring. Than returns the new text.'''
def censor_this(c_text, email):

    scrable_text = scrable(c_text)

    # for the really sort words that might be found in other bigger words we need to make
    # adjustments to avoid this
    if len(c_text) <= 4:
        c_text += ' '
        scrable_text += ' '

    # As long as c_text is still in the email the while loop needs to continue
    while c_text in email or c_text.title() in email:
        # First find the starting index of the found location of c_text
        if c_text in email:
            index = email.find(c_text)
        elif c_text.title() in email:
            index = email.find(c_text.title())
        
        # Than email needs to be changed to remove c_text and replace it with the scrable_text
        email = email[:index] + scrable_text + email[index + len(c_text) :]

    # Fianlly return the email after the while loop has found all occurances of c_text        
    return email

def scrable(text):
    # These letters are for generating random letters to replace the c_text that needs to be censor
    letters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '[', ']', '<',
               '>', 'F', '7', 'U', '8', '9', 'K', '-', 'C']
    # A variable to store the replacement for c_text
    new_text = ""

    # A for loop to iterate to the length of c_text
    for i in range(len(text)):
        # A letter is chosen at random each time the for loop is ran and added to new_text
        new_text += random.choice(letters).upper()
    
    return new_text

''' This function is a helper method. (In other words don't worry about it ;)'''
def my_func(e):
    return len(e)

''' The following function censors a list of terms from the given text. paramters are the terms and
    the text that needs to be censored. And returns the new text.'''
def censor_these(terms, email):
    # Sorts the terms by size (Largest to smallest)
    terms.sort(reverse = True, key = my_func)

    # For every term
    for t in terms:
        # Run the censor_this() method on each word and set the result to email
        email = censor_this(t, email)
    
    return email

''' The following method is an extra one not part of the project. The method formats text and prints
    to the console.'''
def print_c_format(email, line_cap = 100):
    # Keeps track of the last index used to add a next-line
    used_index = 0
    # Keeps track of the last time a space was found
    last_space = -1
    # Keeps track of the count for the line
    line_count = 0
    # Keeps track of the index we are currently on in the for loop
    count = 0
    # The for loop goes through each index in the email's text
    for x in email:
        # Checks if the line_cap is meet
        if line_count > line_cap:
            # Cheks if a space was found in the last line or not
            if last_space >= used_index:
                # Adds a next-line and removes the extra space so it doesn't look weird
                email = email[:last_space] + "\n" + email[last_space + 1:]
                # Adjest variables for the next line of text
                #count += 1
                used_index == last_space
                line_count = 0
            else:
                # This is the scenario where a new space was not found on the next line
                # POTENTIAL BUG: might cut off an extra letter when it shouldn't
                email = email[:line_count] + "\n" + email[line_count:]
                # Adjest variables for the next line of text
                count += 1
                used_index == last_space
                line_count = 0
        else:
            # if line cap isn't meet than check if the current idex is a space
            if x == " ":
                last_space = count
            elif '\n' in x:
                # Since a next-line was found before we meet the line_cap we need to reset line_count
                line_count = 0
        line_count += 1 
        count += 1
    print(email)

''' The following method censors a list of given terms is they occure more than the skip amount in
    the given email. '''
def keep_these_down(terms, email, skip=2):
    #  A list to store the scrabled version of each term
    scrabled = []

    # A for loop to go trough each term and store teh value of the screabled term
    for x in terms:
        scrabled.append(scrable(x))

    # This list is going store every indavidual letter in the email
    letters = []
    # For loop to iterate through the email
    for x in email:
        letters.append(x)

    # This list is going to store each word and each symbol in it's own index
    words = []
    # This varibale keeps track of the last used index
    last_index = 0
    # for loop that iterates through the length of the letters list
    for x in range(len(letters)):
        # If the current character isn't a letter
        if not letters[x].isalpha():
            # Than append all the leters in between the last_index and the current index
            words.append(''.join(letters[last_index:x]))
            # Also need to append the current index
            words.append(letters[x])
            # Update last_index
            last_index = x + 1
    
    # Keeps tracks of matched wordcount
    count = 0
    # For loop to go through the length of the list words
    for x in range(len(words)):
        # If the current word matches one of the terms that needs to be censored
        if words[x] in terms:
            # Add one to the count
            count += 1
            # If the count is high than the amount that needs to be skipped
            if count > skip:
                # Than replace the current index with the scrabled word
                words[x] = scrabled[terms.index(words[x])]
    # Join all the varibles from words and return
    return ''.join(words)

""" TESTING """

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]

'''print(censor_term("learning algorithms", email_one))


new_email = cesor_this(proprietary_terms, email_two)
print_eformat(new_email, 70)
#print_eformat(email_two, 70) '''

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control",
    "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
    "distressing", "concerning", "horrible", "horribly", "questionable"]

email = censor_these(proprietary_terms, email_three)
print_c_format(keep_these_down(negative_words, email), 50)
#keep_these_down(negative_words, email)







