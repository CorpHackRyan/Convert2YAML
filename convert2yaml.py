import os.path
import sys
import re

# Things to test for:
# [x] verify that there is 2 inputs given at command line, if not, specify you need 2 required
# [x] verify first path is valid
# [x] verify second path is valid
# [x] each path must be specific '/'
# [ ] write automated tests/unit testing

# Ensure 2 arguments are passed into program
if len(sys.argv) < 3:
    print('\n***ERROR*** 2 arguments are required.\n')
    print('required: Argument 1: the path to the input CSV file itself')
    print('required: Argument 2: the path to the YAML output file\n')
    print('Quietly terminating myself.....')
    sys.exit()

# Verify the paths that were passed are valid:
# (sys.arg[] parameter 1 is path to csv input file, parameter 2 is path + filename to output yaml file to)
if not (os.path.isfile(sys.argv[1])):
    print(sys.argv[1], ' is not a valid filename.\nQuietly terminating myself...')
    sys.exit()

out_path, out_file = os.path.split(sys.argv[2])  # head will return path only, tail will return filename from given path
yaml_out_path = os.path.isdir(out_path)

if not(os.path.isdir(out_path)):
    print(out_path, ' is not a valid path.\nQuietly terminating myself...')
    sys.exit()

# Verify filename input is valid. Obviously not perfect as system chaining operators will override the input, but you
# get the idea of where my head is at.

match = re.search(r'[#<$+%>!`&*|{?=}/:r"\"@^]', out_file)

if match is not None:
    print(match.group(), 'is not a valid character for a filename.\nQuietly terminating myself...')
    sys.exit()













