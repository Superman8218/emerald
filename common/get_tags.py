import getopt
import os
from sets import Set
import sys

import pdb

def main():

    # Get the input file from the command line

    input_file = os.getcwd()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "i:", ["input="])
    except getopt.GetoptError:
        print '-i <inputfile>'
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-i':
            input_file = os.path.join(input_file, arg)

    #Parse the file

    with open(input_file) as f:
        current_tag = ''
        complement = ''
        tag_list = Set([])
        output = {}
        for line in f:
            line = line.strip('\n')
            if line:
                if not current_tag:
                    # pdb.set_trace()
                    current_tag = line
                    complement = current_tag[0] + '/' + current_tag[1:]
                    if current_tag not in tag_list:
                        tag_list.add(current_tag)
                        output[current_tag] = Set([])
                elif line == complement:
                    current_tag = ''
                elif line[0] == '<':
                    index = line.find('>')
                    if index != -1:
                        substring = line[:index+1]
                        if not (' ' or '/') in substring:
                            output[current_tag].add(substring)

        output_file = os.path.join(os.getcwd(), 'fbo/format.txt')
        with open(output_file, 'w') as out:
            for tag in output:
                out.write(tag + ':\n\n')
                for field in output[tag]:
                    out.write(field)
                    out.write('\n')
                out.write('\n')

if __name__ == "__main__":
    main()
