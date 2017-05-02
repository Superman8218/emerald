import re

tag_regex = re.compile(r'<[A-Z]+>')

field_aliases = {
    'date': handle_date,
    'year': handle_year,
    'zip' : 'zip_code',
    'classcod' : 'class_code',
    'offadd' : 'office_address',
    'respdate' : handle_respdate,
    'archdate' : 'archive_date',
    'contact' : handle_contact,
    'desc' : 'description',
}

def extract_tag(line):
    tag_end_index = line.find('>')
    if tag_end_index != -1:
        return line[1:tag_end_index]

def get_tag_complement(tag):
    return '</{0}>'.format(tag)

def parse_file(file_path):
    current_tag = ''
    complement = ''
    previous_line = ''
    master = None
    with open(file_path, 'r') as f:
        lines = [line.strip('\n') for line in list(f)]
        for index in xrange(0, len(lines)):
            line = lines[index]
            if not line:
                continue
            if not current_tag:
                current_tag = extract_tag(line)
                complement = get_tag_complement(current_tag)
                master = Master()
            elif line == complement:
                current_tag = ''
            elif tag_regex.match(line):
                pass
