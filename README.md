# Python Assignment

Python script that will check for a pattern inside the file. If a line has that pattern then print the output accordingly.


If -m ( --machine ) flag is 1 it will generate machine readable output with the below format. <br/>
file_name:no_line:start_pos:matched_text

f -m is 0 then it will print the below format.<br/>
file_name:line

This script uses re module which lets you check if a particular string matches a given regular expression.

## Below are some Sample Outputs:
```
Cmd 1:
python3 regex_match.py -f samplefile.txt -r hello -m 1

Output:
sampletxt.txt:3:7:hello
sampletxt.txt:3:45:hello
sampletxt.txt:3:63:hello

```
Above is machine readable output with -m flag 

where : -f flag is File path and -r flag is Pattern

```
Cmd 2:
python3 regex_match.py -f samplefile.txt -r hello

Output:
sampletxt.txt:Try to hello use OOP in order to encapsulate hello differences hello between output

sampletxt.txt:Try to hello use OOP in order to encapsulate hello differences hello between output

sampletxt.txt:Try to hello use OOP in order to encapsulate hello differences hello between output

```
This is the normal output without -m flag


## Error Handling Sample:

```
Cmd :
python3 regex_match.py  -f sample.txt -r hello

Output:
file not found, enter correct file name

```
