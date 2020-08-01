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
def censor_this(c_text, email, skip = 0):
    # These letters are for generating random letters to replace the c_text that needs to be censor
    letters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '{', '}', '[', ']', '<',
     '>', 'F', '7', 'U', '8', '9', 'K', '-', 'C']
    # A variable to store the replacement for c_text
    new_text = ""

    # A for loop to iterate to the length of c_text
    for i in range(len(c_text)):
            # A letter is chosen at random each time the for loop is ran and added to new_text
            new_text += random.choice(letters).upper()

    # for the really sort words that might be found in other bigger words we need to make
    # adjustments to avoid this
    if len(c_text) <= 4:
        c_text += ' '
        new_text += ' '

    # As long as c_text is still in the email the while loop needs to continue
    while c_text in email or c_text.title() in email:
        # First find the starting index of the found location of c_text
        if c_text in email:
            index = email.find(c_text)
        elif c_text.title() in email:
            index = email.find(c_text.title())
        
        # Than email needs to be changed to remove c_text and replace it with the new_text
        email = email[:index] + new_text + email[index + len(c_text) :]

    """ Skip section"""
    if skip > 0:
        count = 0
        while new_text in email:
            if count == skip:
                return email
            email = email[:index] + c_text + email[index + len(c_text):]
            count += 1

    # Fianlly return the email after the while loop has found all occurances of c_text        
    return email

''' This function is a helper method. (In other words don't worry about it ;)'''
def my_func(e):
    return len(e)

''' The following function censors a list of terms from the given text. paramters are the terms and
    the text that needs to be censored. And returns the new text.'''
def censor_these(terms, email, skip = 0):
    # Sorts the terms by size (Largest to smallest)
    terms.sort(reverse = True, key = my_func)

    # For every term
    for t in terms:
        # Run the censor_this() method on each word and set the result to email
        email = censor_this(t, email, skip)
    
    return email

''' The following method is an extra one not part of the project. The method formats text and prints
    to the console.'''
def print_eformat(email, line_cap = 100):
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

def keep_it_down(terms, email, skip = 2):
    return censor_these(terms, email, skip)






""" TESTING """

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]

'''print(censor_term("learning algorithms", email_one))


new_email = cesor_this(proprietary_terms, email_two)
print_eformat(new_email, 70)
#print_eformat(email_two, 70) '''

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control",
    "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
    "distressed", "concerning", "horrible", "horribly", "questionable"]
email = censor_these(proprietary_terms, email_three)
print_eformat(keep_it_down(negative_words, email), 50)









