import os.path
import sys

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
# (parameter 1 is path to csv file, parameter 2 is path to output yaml file to)
if not (os.path.isdir(sys.argv[1])):
    print(sys.argv[1], ' is not a valid path.\nQuietly terminating myself...')
    sys.exit()

if not(os.path.isdir(sys.argv[2])):
    print(sys.argv[2], ' is not a valid path.\nQuietly terminating myself...')
    sys.exit()

head, tail = os.path.split(sys.argv[2])  # head yields' filename from path
yaml_out_path = os.path.isdir(head)

print(yaml_out_path)



