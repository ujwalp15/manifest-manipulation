#!/usr/bin/env python3.5

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
for project in projects:
    name = project.get('name')
    clone_depth = project.get('clone-depth')
    if clone_depth is None and name.find('prebuilts') != -1:
        lm.append(ElementTree.Element('remove-project', attrib={
            'name': project.get('name')
        }))
        attrib = {
            'name': project.get('name'),
            'path': project.get('path'),
            'clone-depth': "1"
        }
        if project.get('remote'):
            attrib['remote'] = project.get('remote')
        if project.get('revision'):
            attrib['revision'] = project.get('revision')
        lm.append(ElementTree.Element('project', attrib))
indent(lm, 0)
raw_xml = ElementTree.tostring(lm)
raw_xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + raw_xml.decode('utf-8')
f = open('shallow_prebuilts.xml', 'w')
f.write(raw_xml)
f.close()
