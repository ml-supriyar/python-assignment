#Import Libraries
import re 
import sys
import os.path
import argparse


# Function that prints the expected output
def print_msg(file_name,line_number,pattern,line,machine,start_pos):
# Print machine readable output if value is 1
    if machine==1:
        print("{}:{}:{}:{}".format(file_name,line_number,start_pos,pattern))
    elif machine==0:
        print("{}:{}".format(file_name,line))
    else:
        print("Please enter 0 or 1 for -m flag")


# Checks if the given patterns exists in the file
def regex_search(path,pattern,machine):
# Check if the file exist
    file_exists=os.path.isfile(path)
# If the file doest exists then print the error msg and return
    if file_exists==False:
        print("File not found, Enter correct file name")
        return
# Open the file using the given path
    ipfile = open(path,"r")
# Reads the lines and stores it as a list
    lines=ipfile.readlines()
    search_pattern= re.compile(pattern)
# Iterate through each element of the list
    for counter, line in enumerate(lines):
# Finditer scans the string from left to right, and matches are returned in the iterator form.
        for m in search_pattern.finditer(line):
# Points starting index of the match and calls print function whenever there is a match
            start_pos=m.start()
            if start_pos==0 or start_pos:
                print_msg(path,counter+1,pattern,line,machine,start_pos)

                
def main():
# Taking the inputs with -m , -r , -f flags
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex", help="Pattern")
    parser.add_argument("-f", "--files", help="file name")
    parser.add_argument("-m", "--machine", help="machine readable")
# Assigning user given input to variables
    args = parser.parse_args()
    path = args.files
    machine=args.machine
    pattern=args.regex
# Handles error  , if machine is none then it will be initialized to zero
    if machine==None:
        machine=0
# Handles error if the machine input is not an integer 
    try:
        machine=int(machine)
    except:
        print("Please enter 0 or 1 for -m flag")
        return
# If -m flag is 0 and one it goes to regex_search function 
    if machine==1 or machine==0:
        try:
            regex_search(path,pattern,machine)
# If path and patern is empty then it will return with print msg
        except:
            print("please enter filename with f flag and pattern with -r flag")
            return
    else:
        print("Please enter 0 or 1 for -m flag")
        return
    

if __name__ == "__main__":
    main()
