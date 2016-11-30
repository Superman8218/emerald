from functools import partial

from bs4 import BeautifulSoup

from models import FboMaster
import pdb

"""So the idea here is going to be to just use the list of all the fields in the fbo_master model.  If a field isn't in the fbo_master model then we can just log it and deal with it.  But all of the fields should be present"""

record_types = [
    'presol',
    'srcsgt',
    'snote',
    'combine',
    'amdcss',
    'mod',
    'award',
    'archive'
]

srcsgt_fields = [
    'agency',
    'office'
]

field_names = [field.name for field in FboMaster._meta.get_fields()]

def tag_filter(tag, name):
    return tag.name == name

def nonempty_tag(tag):
    return tag.name is not None

def parse_file(file_path):
    """So right now this is built to only extract one type of record, but we can definitely make it extract more"""
    soup = BeautifulSoup(open(file_path))
    # records = filter(partial(tag_filter, name='srcsgt'), soup.children)
    records = filter(nonempty_tag, soup.children)
    for record in records:
        master = FboMaster()
        fields = filter(lambda x: x.name in field_names, records[0](True))
    # pdb.set_trace()
        for item in fields:
            text = item.find(text=True, recursive=False).encode('utf-8').strip()
            print item.name + ': ' + text
            setattr(master, item.name, text)
        master.save()
