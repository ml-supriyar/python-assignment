import re 
import sys
import os.path
import argparse


def print_msg(file_name,line_number,pattern,line,machine,start_pos):
    try:
        machine=int(machine)
    except:
        print("Please enter 0 or 1 for -m flag")
        return
    if machine==1:
        print("{}:{}:{}:{}".format(file_name,line_number,start_pos,pattern))
    elif machine==0:
        print("{}:{}".format(file_name,line))
    else:
        print("Please enter 0 or 1 for -m flag")




def regex_search(path,pattern,machine):
    file_exists=os.path.isfile(path)
    if file_exists==False:
        print("file not found, enter correct file name")
        return
    ipfile = open(path,"r")
    lines=ipfile.readlines()
    search_pattern= re.compile(pattern)
    for counter, line in enumerate(lines):
        for m in search_pattern.finditer(line):
            start_pos=m.start()
            if start_pos==0 or start_pos:
                print_msg(path,counter+1,pattern,line,machine,start_pos)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--regex", help="Pattern")
    parser.add_argument("-f", "--files", help="file name")
    parser.add_argument("-m", "--machine", help="machine readable")
    args = parser.parse_args()
    path = args.files
    machine=args.machine
    pattern=args.regex
    if machine==None:
        machine=0
    try:
        machine=int(machine)
    except:
        print("Please enter 0 or 1 for -m flag")
        return
    if machine==1 or machine==0:
        try:
            regex_search(path,pattern,machine)
        except:
            print("please enter filename with f flag and pattern with -r flag")
            return
    else:
        print("Please enter 0 or 1 for -m flag")
        return


if __name__ == "__main__":
    main()
