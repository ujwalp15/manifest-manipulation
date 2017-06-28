#!/usr/bin/env python3.*

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
defaults = xml_root.find('default')
if defaults.get('remote') == 'github': # Gah, it's LineageOS. No remote specified == Lineage github.
    for project in projects:
        remote = project.get('remote')
        if remote == 'aosp':
            lm.append(ElementTree.Element('remove-project', attrib = {
                'name': project.get('name')
            }))
else:
    for project in projects:
        remote = project.get('remote')
        if not remote:
             lm.append(ElementTree.Element('remove-project', attrib = {
                'name': project.get('name')
             }))
indent(lm, 0)
raw_xml = ElementTree.tostring(lm)
raw_xml = '<?xml version='1.0' encoding='UTF-8'?>\n' + raw_xml.decode('utf-8')
f = open('delete_aosp.xml', 'w')
f.write(raw_xml)
f.close()

