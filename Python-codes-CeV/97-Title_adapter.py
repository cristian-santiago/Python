'''
This function will show a msg with the line above and below the msg with the same size

------
Hello
------

-------------
I'm Cristian
-------------
'''

def line(msg):
    len_msg = len(msg)
    print("-"*len_msg)
    print(msg)
    print("-"*len_msg)
    
a = input(str("Insert the message: "))

line(a)