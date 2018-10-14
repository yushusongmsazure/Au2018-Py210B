import csv
import xml.etree.ElementTree as ET 

def parseXML(xmlFile):
    tree = ET.parse(xmlFile)

    root = tree.getroot()
    total = 0

    groups = root.findall('CloudGroup')
    #clouds = groups.findall('Cloud')
    
    for item in groups:
        clouds = item.findall('Cloud')
        for cloud in clouds:
            glb = cloud.find('GlobalValues')
            envs = glb.findall('EnvironmentSetting')
            for env in envs:
                name = env.get('Name')
                match = ['Providers.Feature.Instances','Providers.AppliancePublisher.Instances','Providers.Authorization.Instances','Providers.Shim.Instances','Providers.Test.Instances','Frontdoor.Web.Instances','Frontdoor.Admin.Instances']
                if name in match:
                    v = int(env.get('Value'))
                    total = total + v
                    print(name)
                    print(v)
    print('Total:')
    print(total)

parseXML('Settings_AUX_Prod_Frontdoor.xml')
