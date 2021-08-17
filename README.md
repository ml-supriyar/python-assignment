# Python-assignment

Python script that searches for lines matching regular expression -r (--regex) in file/s -f (--files), Print if a line matches with file name and the line number for every match.

This script uses re module to which lets you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

## Below are some Sample Outputs:
```
Cmd 1:
python3 regex_match.py -f samplefile.txt -r hello -m 1

Output:
sampletxt.txt:3:7:hello
sampletxt.txt:3:45:hello
sampletxt.txt:3:63:hello

```
Above is machine readable output with -m flag where -f flag is File path -r flag is Pattern

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
