# Python-assignment

Python script that searches for lines matching regular expression -r (--regex) in file/s -f (--files), Print if a line matches with file name and the line number for every match.

This script uses re module to which lets you check if a particular string matches a given regular expression (or if a given regular expression matches a particular string, which comes down to the same thing).

## Sample Output:
``
Cmd:
python3 regex_match.py -f sampletxt.txt -r hello -m 1

Output:
sampletxt.txt:3:7:hello
sampletxt.txt:3:45:hello
sampletxt.txt:3:63:hello

``
