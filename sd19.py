#This will be my function
def new_comment(name, comment):
    target = open(name, 'w')
    target.write(comment)
    target.close()

##this will be to append a document
def ap_comment(name):
    target = open(name, 'a')
    target.write(comment)
    target.close
##this will be the code to run it i guess??
print("""Welcome to the beta stage of my teacher feedback system.
\nFirst, I will ask you for an assignment name.\nThen I will ask
you to type your comment for that assignment. Eventually I hope to
have more features, but I am still learning what the heck I am doing. """)
print("Do you want to make a new assignment or modify an existing one?\n")
answer = input('n or m?')
n = "n"
if answer == n:
    print('What would you like to call this assignment?\n')
    name = input(' Put .txt at the end of your name!!\n')
    print("Okay, what would you like the comment to be?\n All of your text must be on one line, do not hit enter until you are done!!!")
    comment = input()
    print('''Got it, I'm going to write it to the file now''')
    print("should be good to go now!!")
    new_comment(name, comment)
else:
    print("Let's modify an existing comment!")
    print("What is the name of the file you want to modify?\n")
    name = input('Write out the whole name including the file extension!')
    print("what would you like it to say?\n")
    comment = input()
    print("Got it, modifying it now. . . ")
    ap_comment(name)
    print("Goodbye")
