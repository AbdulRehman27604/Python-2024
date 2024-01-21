''' Q1. Write code to do the following:
A- open the file happy.txt for reading
B- read and print the whole file using the read function
C- update the code to read and print just the first line of the file
D- add a while loop to read and print every line single spaced
E- update the code to print every word on its own line single spaced
F- write the code to print every word on its own line single spaced using a for loop
G- update F so that the first line of the file is skipped
'''
def Q1a():
    
    file = open('happy.txt','r')
    object = file.read()
    print(object)
    file.close()
    
    print('....Again')
    file = open("happy.txt","r")
    line = file.readline()
    print(line)
    file.close()
    
    print(".....Again")
    file = open("happy.txt","r")
    lines = file.readline()
    while lines != '':
        cur_line = lines.strip()
       # print(cur_line)
        lo_word = cur_line.split()
        for value in lo_word:
            print(value)
        lines = file.readline()
    file.close()   
    
    print("....Again")
    file = open('happy.txt','r')
    for sentences in file:
        new_sentence = sentences.strip()
        print(new_sentence)
    file.close
Q1a()
        
''' Q2. Write code to do the following:
- open the file happy.txt for appending
- add the words: 'authored by Pharell Williams' to the end of the file on its own line
'''


'''def q2():
    
    file = open("happy.txt","a")
    sentence = '\nauthored by Pharell Williams'
    file.write(sentence)
    file.close
    
    file = open("happy.txt","r")
    x = file.read()
    print(x)
    
q2()'''
    


''' Q3. Write code to do the following:
- open the file not_happy.txt for writing
- add the words: 'You should be happier' to this file
Before you run this code, look at the contents of not_happy.txt
- close the file, run the program and then reopen the file
'''


def q3():
    file = open("not_happy.txt","w")
    file.write('You should be happier')
    file.close
q3()
    
