import csv
import xml.etree.ElementTree as ET 

def parseXML(xmlFile):
    tree = ET.parse(xmlFile)

    root = tree.getroot()

    group = root.findall('CloudGroup')

    for item in group:
        print(item)








parseXML('Settings_AUX_Prod_Providers.xml')