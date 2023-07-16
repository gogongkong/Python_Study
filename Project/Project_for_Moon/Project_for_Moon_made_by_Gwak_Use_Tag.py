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
        child.attrib['price'] = str(10 * float(child.attrib['price'] ))
        print(child, child.attrib['price'], "-->", str(10 * float(child.attrib['price'] )))

    # Save
    with open(xml_save_path, "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)


def modify_xml_by_attrib(xml_path, xml_save_path, attrib):
    # Read
    with open(xml_path) as f :
        tree = ET.parse(f)
        root = tree.getroot()

    for child in root.iter():       # for all iterative children
        if attrib in child.attrib:
            # Do somthing here
            # Change Attribution
            if child.attrib['author'] == "Bumjin":
                child.attrib['price'] = str(10 * float(child.attrib['price'] ))
                print(child, child.attrib['price'], "-->", str(10 * float(child.attrib['price'] )))

    # Save
    with open(xml_save_path, "wb") as file:
        tree.write(file, encoding='utf-8', xml_declaration=True)


print("--- Find Recursively All by Tags--------")
modify_xml_by_tag("xml_test.xml", "xml_modified_by_tag.xml", tag="book")
print("--- Find Recursively All by Attrib--------")
modify_xml_by_attrib("xml_test.xml", "xml_modified_by_attrib.xml", attrib="author")