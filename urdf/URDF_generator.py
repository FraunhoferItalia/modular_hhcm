import sys
import re
import xml.etree.ElementTree as ET
import xacro

def main():    

    ET.register_namespace('xacro', "http://ros.org/wiki/xacro")

    #obtaining tree from base file
    tree = ET.parse('ModularBot.urdf.xacro')

    root = tree.getroot()


    # for child in root:
    #   print child.tag, child. attrib, child.text

    # childs=root.findall('link')

    # count = 0
    # for link in root.iter('link'):
    #     if link.get('suffix') > count :
    #       count = link.get('suffix')
    #       LastElement = link

    length_value = str(0.8)

    #adding 3 links to the tree
    a = ET.SubElement(root, "{http://ros.org/wiki/xacro}add_link", suffix = '1', length = length_value, a_i = '0', d_i = '${len1}', alpha_i = '0', theta_i = '0')
    b = ET.SubElement(root, "{http://ros.org/wiki/xacro}add_link", suffix = '2', length = length_value, a_i = length_value, d_i = '0', alpha_i = '${-pi/2}', theta_i = '0')
    c = ET.SubElement(root, "{http://ros.org/wiki/xacro}add_link", suffix = '3', length = length_value, a_i = length_value, d_i = '0', alpha_i = '${pi/2}', theta_i = '0')

    #writing .xacro file
    tree.write(sys.argv[1], xml_declaration=True, encoding='utf-8')

    #converting from .xacro to .urdf
    xacro.main()

if __name__ == '__main__':
  main()