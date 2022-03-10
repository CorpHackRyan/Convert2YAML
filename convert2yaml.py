import os.path
import sys
import re
import csv
import time

# Things to test for:
# [x] verify that there is 2 inputs given at command line, if not, specify you need 2 required
# [x] verify first path is valid
# [x] verify second path is valid
# [x] each path must be specific '/'
# [ ] understand yaml file structure
# [ ] convert csv to yaml
# [ ] convert xlsv to yaml
# [ ] write automated tests/unit testing to test functions below
# [ ] create functions instead of having everything in the main script


print('\n\n======  CSV/XLSX to YAML converter   ====== ')


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

print(f'\nInput file given:        {sys.argv[1]}  - VALID INPUT')
print(f'Output file path valid:  {out_file} - VALID INPUT & will be written to: {out_path}')

# Some YAML references below:
# https://circleci.com/blog/what-is-yaml-a-beginner-s-guide/
# https://www.cloudbees.com/blog/yaml-tutorial-everything-you-need-get-started
# https://camel.readthedocs.io/en/latest/yamlref.html

# Notes about YAML
# YAML doesn't allow TAB chars, spaces only

# Open csv input file for reading & get headers
with open(sys.argv[1], mode='r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = next(csv_reader)
    print(f'Total column headers:    {len(header)}')  # total sols

    # Read data contents of csv file into memory
    each_row = []
    start_time = time.time()

    for row in csv_reader:
        each_row.append(row)
    print(f'Total record entries:    {len(each_row)}\n')

    with open(sys.argv[2], mode='w') as yaml_out_file:
        for idx, row_data in enumerate(each_row):
            if len(row_data) != len(header):
                print(f'******** Potential error or data missing in row {idx+1}. Only {len(row_data)} values found - '
                      f'should be {len(header)} values. *********')
                print('Continuing to process data')
                print(f'processing {row_data}')
                yaml_out_file.write(''.join(row_data) + '\n')
            else:
                print(f'processing {row_data}')
                #print(len(row_data))
                yaml_out_file.write(''.join(row_data) + '\n')





    end_time = time.time()
    time_elapsed = (end_time - start_time)
    print(f'Data processing completed in {round(time_elapsed * 1000, 3)} ms.')




















