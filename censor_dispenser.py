import random

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

''' The following method takes in two arguments. The first is the text that needs to be
    censored and the second being the email that needs censoring. Than returns the new text.'''
def censor_term(c_text, email):
    # These letters are for generating random letters to replace the c_text that needs to be censor
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    # A variable to store the replacement for c_text
    new_text = ""
    # A for loop to iterate to the length of c_text
    for i in range(len(c_text)):
        # A letter is chosen at random each time the for loop is ran and added to new_text
        new_text += random.choice(letters).upper()

    # As long as c_text is still in the email the while loop needs to continue
    while c_text in email:
        # First find the starting index of the found location of c_text
        index = email.find(c_text)
        # Than email needs to be changed to remove c_text and replace it with the new_text
        email = email[:index] + new_text + email[index + len(c_text) :]
    # Fianlly return the email after the while loop has found all occurances of c_text        
    return email

''' The following function censors a list of terms from the given text. paramters are the terms and
    the text that needs to be censored. And returns the new text.'''
def cesor_terms(terms, email):
    for t in terms:



""" TESTING """

print(censor_term("learning algorithms", email_one))