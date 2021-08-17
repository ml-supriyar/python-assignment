# Import the library
import re
import sys
import os.path
import argparse


# Function to print filename, line number and the line
def print_msg(file_name,line_number,pattern,line,machine):
    try:
        machine=int(machine)
    if machine==1:
        print("{}:{}:{}".format(file_name,line_number,pattern))
    else:
        print("{}:{}".format(file_name,line))


# Regex functionn to search pattern in a file
def regex_search(path,pattern,machine):
    file_exists=os.path.isfile(path)
    if file_exists==False:
        return
    ipfile = open(path,"r")
    lines=ipfile.readlines()
    search_pattern= re.compile(pattern)
 

# Print the line number if the pattern exist
    for counter, line in enumerate(lines):
        ab = search_pattern.search(line)
        boolean = bool(ab)
        if boolean:
            print_msg(path,counter+1,pattern,line,machine)
            
            
#  Create the parser , Add and Parse the arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex", help="Pattern")
    parser.add_argument("-f", "--files", help="file name")
    parser.add_argument("-m", "--machine", help="file name")
    args = parser.parse_args()
    path = args.files
    machine=args.machine
    pattern = args.regex
    regex_search(path,pattern,machine)
