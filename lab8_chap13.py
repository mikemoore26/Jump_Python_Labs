# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#!/usr/bin/python 
import argparse
import requests 

parser = argparse.ArgumentParser(description='Search some files')

# The following argument collects all of the extra command-line arguments into a list. It’s
# being used to make a list of filenames in the example:
    
parser.add_argument(dest='filenames',metavar='filename', nargs='*')


# The following argument specification allows an argument to be repeated multiple times
# and all of the values append into a list. 

# The required flag means that the argument must be supplied at least once. 
# The use of -p and --pat mean that either argument name is acceptable.

parser.add_argument('-p', '--pat',metavar='pattern', required=True,
 dest='patterns', action='append', help='text pattern to search for')

# The following argument sets a Boolean flag depending on whether or not the argument
# was provided:
parser.add_argument('-v', dest='verbose', action='store_true', help='verbose mode')

# The following argument takes a single value and stores it as a string:
parser.add_argument('-o', dest='outfile', action='store', help='output file')


# the following argument specification takes a value, but checks it against a set of possible choices.

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',help='search speed')

args = parser.parse_args()
 


print('filename ' ,args.filenames)
print('pattern ' ,args.patterns)
print('verbose ',  args.verbose)
print('outfile ', args.outfile)
print('speed ',args.speed)


def call_url(url):
    r = requests.get(url)
    print(r.text)
 
#if args.url is not None:
#    call_url(args.url)
 
# ********* NOTES *********

# The dest argument specifies the name of an attribute where the result of
#parsing will be placed.

# The metavar argument is used when generating help messages.

#The action argument specifies the processing associated with the argument and is often
#store for storing a value or append for collecting multiple argument values into a list.

















