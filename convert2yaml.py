# Things to test for:
# [ ] verify that there is 2 inputs given at command line, if not, specify you need 2 required
# [ ] verify first path is valid
# [ ] verify second path is valid
# [ ] each path must be specific '/'

import os.path
import sys

print('Name of script', sys.argv[0])  # Script name is always at 0

# Ensure 2 arguments are passed into program
if len(sys.argv) < 3:
    print('\n***ERROR*** 2 arguments are required.\n')
    print('Argument 1: the path to the input CSV file itself')
    print('Argument 2: the path to the YAML output file')
    print('Exiting...')
    sys.exit()

# Verify the paths that were passed are valid:
# (parameter 1 is path to csv file, parameter 2 is path to output yaml file to)
csv_path = os.path.isdir(sys.argv[1])
print(csv_path)

head, tail = os.path.split(sys.argv[2])
yaml_out_path = os.path.isdir(head)
print(head, 'printing head from path input split')
print(yaml_out_path)



