import doctest

'''
Q1. Design a function that will take a filename of a file with rows of
names and email addresses separated by commas and creates and
returns a dictionary of email contacts.

What will happen if the given file has 2 lines with the same name
but different email addresses?
'''
def create_contacts(file_name: str) -> dict[str, str]:
    """returns a dictionary with email contacts from the filename:
    -dict[name, email]
    precondition; filenmae exits and contains lines with:
    name and email seperated by commas
    >>> create_contacts('empty.csv')
    {}
    >>> create_contacts('emailInfo.csv')
    {'abc': 'abc@foo.ca', 'cde': 'ced@foo.ca',\
    'fgh': ' fgh@foo.ca', 'ijk': 'ijk@foo.ca'}
    """
    name_to_email = {}
    file_handle = open(file_name)
    for line in file_handle:
        line = line.strip()
        name, email = line.split(',')
        #Create an entry in the dict
        name_to_email[name] = email
    file_handle.close()
    return name_to_email

''' Q2. Design a function that takes a filename of a file with rows of votes
containing a voter id followed by vote (yes, no or abstain) and returns
a dictionary containing the counts of votes for yes, no, abstain.
'''
def count_votes(file_name: str) -> dict[int, int, int]:
    """ returns a dictionary of vote counts in filename with line as:
    voter id and vote seperated by space.
    >>> count_votes('empty.txt')
    {'yes': 0, 'no': 0, 'abstain': 0}
    >>> count_votes('votes.txt')
    {'yes': 4, 'no': 2, 'abstain': 1}
    """
    vote_counter = {'yes': 0, 'no': 0, 'abstain': 0}
    file_handle = open(file_name,'r')
    for line in file_handle:
        line = line.strip()
        name, vote = line.split(' ')
        vote_counter[vote] += 1
  
    file_handle.close()
    return vote_counter
        
        

'''
Q3. Design a function that takes a text file and creates and returns a
dictionary of all the words in the file (no duplicates) followed by
the number of times that word occured.
'''
def count_words(file_name: str) -> dict[str: int]:
    """
    >>> count_words('empty.txt')
    {}
    >>> count_words('small.txt')
    {'one': 1, 'two': 3, 'three': 2, 'repeat': 1, 'bye': 1}
    """
    word_to_count = {}
    file_handle = open(file_name)
    for line in file_handle:
        line = line.strip()
        lo_words = line.split(' ')
        for word in lo_words:
            if word not in word_to_count:
                word_to_count[word] = 1
            else:
                word_to_count[word] += 1
    file_handle.close()
    return word_to_count



''' Q4. Design a function that takes a dictionary of names:email addresses
and prompts the user to input a name and prints the email address if
found otherwise prints "name not found.  Would you like to add this contact?"
If the user enters yes, proceeds to collect the name and email address
and create a new name:email address entry in the dictionary.
Test this function from the shell.
'''
