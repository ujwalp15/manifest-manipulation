#!/usr/bin/env python3.5
from xml.etree import ElementTree
import subprocess

# in-place prettyprint formatter
def indent(elem, level=0):
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

manifest = subprocess.check_output(['repo','manifest'])
xml_root = ElementTree.fromstring(manifest)
lm = ElementTree.Element("manifest")
projects = xml_root.findall('project')
for project in projects:
    path = project.get('path')
    if path != None and path.find('linux') != -1:
        lm.append(ElementTree.Element("remove-project", attrib = {
            "name": project.get('name')
        }))
indent(lm, 0)
raw_xml = ElementTree.tostring(lm)
raw_xml = '<?xml version="1.0" encoding="UTF-8"?>\n' + raw_xml.decode("utf-8")
f = open('delete_linux.xml', 'w')
f.write(raw_xml)
f.close()

