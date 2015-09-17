import sys
import os
#print("hello world")
#Take the read/write script that we made:
#-Open the file only once
#	*hint, you need to read and write with your open
#	*hint, you also need to reset your file pointer (see seek())
#-Save the output to a new file instead of printing
#	*hint, you will need an output file

##########   WRITING FILE OUT   ##########
# #open file to read
to_write_file_pointer = open('to_read.txt', 'r+')
# #open file to write
to_new_file = open('new_file.txt', 'w')

#FOR: number in range from 1 to 10, write the number and a new line to our file
for number in range(1, 10):
    #write number to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(number))
#create a list of letters to output to our file
letters = ['a', 'b', 'c', 'd', 'e']
 #FOR: letter in letters from a to e, write letter and a new line to our file
for letter in letters:
    ##write letter to file (with a new line)
    to_write_file_pointer.write("{0}\n".format(letter))

##########   READING FILE IN   ##########
# #open file to read
to_write_file_pointer.seek(0)
#FOR: line in to_read_file_pointer, read and print each line
for line in to_write_file_pointer:
    # #print line
    to_new_file.write("Line: {0}".format(line))
    #print("Line: {0}".format(line))

#uncomment line below to remove file after reading
#os.remove('to_read.txt')

#close file
to_write_file_pointer.close()
to_new_file.close()
raise SystemExit(0)
#ALL DONE!
