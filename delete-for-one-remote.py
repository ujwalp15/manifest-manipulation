#!/usr/bin/env python3

from xml.etree import ElementTree
import subprocess
from functions import indent, is_source_tree
import sys

if not is_source_tree():
    sys.exit(1)
manifest = subprocess.check_output(['repo', 'manifest'])
xml_root = ElementTree.fromstring(manifest)
lm = ElementTree.Element('manifest')
projects = xml_root.findall('project')
defaults = xml_root.find('default')
default_remote = defaults.get('remote')
if (len(sys.argv) >= 2):
    remote_to_remove = sys.argv[1]
else:
    print("Error, no remote specified for removal")
    sys.exit(1)

for project in projects:
    remote = project.get('remote')
    if remote == remote_to_remove or (remote is None and remote_to_remove == default_remote):
        lm.append(ElementTree.Element('remove-project', attrib={
            'name': project.get('name')
        }))

indent(lm, 0)
raw_xml = ElementTree.tostring(lm)
raw_xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + raw_xml.decode('utf-8')
f = open('delete_{0}.xml'.format(remote_to_remove), 'w')
f.write(raw_xml)
f.close()
