'''A student stores daily notes in a file called notes.txt. Write a program that opens the
file, reads all the contents, and displays them on the screen.'''

file = open("notes.txt","w")
file.write("hello")
file.close()
file = open("notes.txt","r")
print(file.read())
file.close()
