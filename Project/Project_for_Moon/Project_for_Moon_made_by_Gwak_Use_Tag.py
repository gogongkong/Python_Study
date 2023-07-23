import os
import numpy as np 
import xml.etree.ElementTree as ET

def modify_xml_by_tag(xml_path, xml_save_path, tag):
    # Read
    with open(xml_path) as f :
        tree = ET.parse(f)
        root = tree.getroot()

    for child in root.iter(tag):
        # Do somthing here
        # Change Attribution
        child.attrib['price'] = child.attrib['MOD']
    # Save
    with open(xml_save_path, "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)


print("--- Find Recursively All by Tags--------")
modify_xml_by_tag("Break2.xml", "xml_modified_by_tag.xml", tag="book")
