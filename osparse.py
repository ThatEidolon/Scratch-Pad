import xml.etree.ElementTree as ET
import dnspython

dnsservers = {'cde':'10.10.1.3','test':'10.10.2.3','prod':'10.10.3.3'}


tree = ET.parse('test.xml')
root = tree.getroot()
"""
list = [
		{'path': 'address', 'element': 'addr'},
		{'path': 'hostnames/hostname', 'element': 'name'},
		{'path': 'os/osmatch', 'element': 'name'}
]

for host in root.iter('host'):
	for i in list:
		item = host.find(i['path'])
		if item is not None: 
			print (i['path']), ':', item.get(i['element'])
		else:
			print (i['path']), ": UNKNOWN"
	print "\n"
	
"""

for host in root.iter('host'):
	address = host.findall('address')
	hostname = host.find('hostnames/hostname')
	os = host.find('os/osmatch')
	print address[0].get('addr'), hostname.get('name'), os.get('name')