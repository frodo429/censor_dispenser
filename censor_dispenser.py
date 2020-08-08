import random

# These are the emails you will be censoring. The open() function is opening the text file that the
# emails are contained in and the .read() method is allowing us to save their contexts to the following
# variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

proprietary_terms = ["she", "personality matrix", "sense of self",
                     "self-preservation", "learning algorithm", "her", "herself"]

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control",
                  "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed",
                  "distressing", "concerning", "horrible", "horribly", "questionable"]

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

''' The following method scrables what ever word is passed to it'''
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

''' The following method is an extra method not part of the OG project. The method indents paragraphs,
    line spaces and prints
    to the console.'''
def print_n_format(email, line_cap=100):
    # Stores the text after '\n' is added to appropriate spots to sperate each line
    done = ""
    # Stores what is currently being checked
    checking = ""
    # Keeps tracks of up to what index has been sorted through
    c_count = 0
    # This while loop needs to continue as long as c_count hasn't meet the length of email
    while c_count < len(email):
        # If theirs more than line_cap(default value is 100) characters left to check
        if len(email) - c_count > line_cap:
            # Than add the next line_cap (100 or the value passed into the method) characters to
            # be checked
            checking = email[c_count: c_count + line_cap]
            # Add the value of line_cap to c_count
            c_count += line_cap
        # Other wise that means ther's less than line_cap characters left to check
        else:
            # Set checking equal to the remainding characters
            checking = email[c_count:]
            # Up date c_count to match the correct index
            c_count += len(email) - c_count
        # The following loop runs until checking is empty 
        while checking != "":
            # If there's a '\n' in checking
            if '\n' in checking:
                # Than we need to find last '\n' that occured
                # Loop throuh checking backwards one char at a time
                for x in range(len(checking) - 1, 0, -1):
                    # If the current index matches '\n'
                    if checking[x] == '\n':
                        # Than add all the chars up to and including the '\n'
                        done += checking[: x + 1]
                        # Update c_count, Reset checking, Break for loop
                        c_count -= len(checking[x + 1 :])
                        checking = ""
                        break
            # Since in this case there isn't a '\n'
            else:
                # Loop through each char backwards one at a time
                for x in range(len(checking) - 1, 0, -1):
                    # Until we find the last space that occured
                    if checking[x] == " ":
                        # Add everything up to that space to done and add '\n' as well
                        done += checking[:x] + "\n"
                        # Update c_count, Update checking and break loop
                        c_count -= len(checking[x+1:])
                        checking = ""
                        break
    
    # New list to store each line of the text
    lines = done.split('\n')
    # Loop through each line
    for n in range(len(lines)):
        # If the line is long enough than it needs to be spaced out to the line_cap
        if len(lines[n]) > line_cap - 7:
            # Run the helper method and set the current index to the new value
            lines[n] = line_spaceing(lines[n], line_cap)
    # Set output to lines joined by '\n'
    output = '\n'.join(lines)
    # Print output to console
    print('\n'.join(lines))
    # Also return output in case it needs to be stored to a new variable out side this method or idk
    return output

''' The following method spaces out a given line to the given legth or the defult line_cap. (helper
    method to c_format)'''
def line_spaceing(line, line_cap=100):
    # A count of the amount of space that need to be added
    needed = line_cap - len(line)
    # A list to store the index of each space in the line
    space_list = []
    # For loop to iterate through the length of the given line
    for x in range(len(line)):
        # If a space was found
        if line[x] == ' ':
            # Than the index is added to space_list 
            space_list.append(x)
    # A for loop to iterate to the length of needed
    for n in range(1 ,needed):
        # At the begining of each iteration find the right index to add a space at
        index = int(len(space_list) / needed * n)
        index = space_list[index] + n
        # Add a space at the index 
        line = line[:index] + ' ' + line[index:]
    return line


''' The following method censors a list of the terms from the negative_words list and proprietary_terms
    list if they occure more than the skip amount in the given email. '''
def keep_it_down(email, skip=2):
    scrable_this = negative_words + proprietary_terms
    #  A list to store the scrabled version of each term
    # To store all the words individually
    words = []
    # Keeps count of last used index
    count = 0
    # Loop through each char in the email
    for x in range(len(email)):
        # In the case that the current index isn't a letter
        if not email[x].isalpha():
            # if the current count doesn't equal x
            if count != x:
                # Append the word
                words.append(email[count:x])
            # Append the single char
            words.append(email[x])
            # Update count
            count = x + 1
    # Keeps tracks of matched wordcount
    count = 0
    # For loop to go through the length of the list words
    for x in range(len(words)):
        # If the current word matches one of the terms that needs to be censored
        if words[x] in scrable_this:
            # Add one to the count
            count += 1
            # If the count is high than the amount that needs to be skipped
            if count > skip:
                # Than replace the current index with the scrabled word
                words[x] = scrable(words[x])
    # Join all the varibles from words and return
    return ''.join(words)

def censor_left_n_right(email):
    # List of all the words that need to be scrabled
    scrable_this = negative_words + proprietary_terms
    # To store all the words individually
    words = []
    # Keeps count of last used index
    count = 0
    # Loop through each char in the email
    for x in range(len(email)):
        # In the case that the current index isn't a letter
        if not email[x].isalpha():
            # if the current count doesn't equal x
            if count != x:
                # Append the word
                words.append(email[count:x])
            # Append the single char
            words.append(email[x])
            # Update count
            count = x + 1
    # Loop through all the words
    for x in range(len(words)):
        # If a words matchs one in scrable_this
        if words[x] in scrable_this:
            # Than swap that word out for the scrabled version
            words[x] = scrable(words[x])
            if x > 0:
                # Than loop through backwards from the current word till we find another word
                for i in range(1, x):
                    # If the length of the current index is over 1 than we found a word
                    if len(words[x - i]) > 1:
                        # Replace that index with the scrabled version
                        words[x - i] = scrable(words[x - i])
                        # Break for loop
                        break
                    else:
                        # Still need to scrabled the spaces and random chars inbetween (just my opinion)
                        words[x - i] = scrable(words[x - i])
            if x < len(words):
                # Loop through all the indexs after the current index
                for i in range(1, len(words) - x):
                    # When it finds a index with a length over 1 than it found a word
                    if len(words[x + i]) > 1:
                        # Replace that index with the crabled version
                        words[x + i] = scrable(words[x + i])
                        # break for loop
                        break
                    else:
                        # Still need to scrabled the spaces and random chars inbetween (just my opinion)
                        words[x + i] = scrable(words[x + i])
    # return the words list join
    return ''.join(words)
    



""" TESTING """

'''
print(censor_this("learning algorithms", email_one))


new_email = censor_these(proprietary_terms, email_two)
print_n_format(new_email, 70)
print_n_format(email_two, 70)

email = censor_these(proprietary_terms, email_three)
print_n_format(keep_it_down(email_one), 70)
print_n_format(keep_it_down(email_two), 70)
print_n_format(keep_it_down(email_three), 70)'''
#print_n_format(keep_it_down(email_four), 70)
#keep_it_down(email)
print_n_format(censor_left_n_right(email_four), 70)
print_n_format(email_four, 70)
