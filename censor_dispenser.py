import random

# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_text(text, email):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
     'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upper = [True, False]
    email_text = email.read()

    while text in email:
        index = email_text.find(text)
        
        new_text = ""
        for i in range(len(text)):
            if random.choice(upper):
                new_text.append(random.choice(letters).upper())
            else:
                new_text.append(random.choice(letters))

        email_text = email_text[:index] + new_text + email_text[index + len(text):]
    return email_text

print(censor_text("learning algorithms", email_one))

