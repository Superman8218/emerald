from os.path import basename
import os

import pudb

def main():
    pudb.set_trace()
    list_dir = 'mail/lists/email_1.csv'
    parcels_dir = os.path.join('mail/parcels/', basename(list_dir).split('.')[0])

    if not os.path.exists(parcels_dir):
        os.makedirs(parcels_dir)

    with open(list_dir, 'r') as lf:
        lines = lf.readlines()
        file_count = 0
        line_index = 0
        while(True):
            parcel_name = os.path.join(parcels_dir, 'parcel_{0}'.format(file_count))
            with open(parcel_name, 'w') as pf:
                for x in xrange(0,5):
                    if line_index < len(lines):
                        pf.write(lines[line_index])
                        line_index += 1
                    else:
                        return
            file_count += 1

if __name__ == "__main__":
    main()
