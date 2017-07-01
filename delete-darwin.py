#!/usr/bin/env python3.5

from xml.etree import ElementTree
import subprocess
from functions import indent, is_source_tree
import sys

if not is_source_tree():
    sys.exit(1)
manifest = subprocess.check_output(['repo','manifest'])
xml_root = ElementTree.fromstring(manifest)
lm = ElementTree.Element('manifest')
projects = xml_root.findall('project')
for project in projects:
    path = project.get('path')
    if path != None and path.find('darwin') != -1:
        lm.append(ElementTree.Element('remove-project', attrib = {
            'name': project.get('name')
        }))
indent(lm, 0)
raw_xml = ElementTree.tostring(lm)
raw_xml = '<?xml version='1.0' encoding='UTF-8'?>\n' + raw_xml.decode('utf-8')
f = open('delete_darwin.xml', 'w')
f.write(raw_xml)
f.close()

