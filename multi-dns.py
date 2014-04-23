from dns import resolver, reversename
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP", help="IP address to lookup")
args = parser.parse_args()

dns_servers = {'cde': '10.10.10.10', 'prod': '10.10.10.11'}
resolvers = {}

def new_resolver (dns_ip):
#takes the IP address of the specific DNS server as an argument	
#returns a resolver object
	temp = resolver.Resolver('configure=False')
	temp.nameservers = [dns_ip]
	return temp

def build_resolvers():
#builds a list of resolvers to use for DNS lookup
#stores in global dictionary resolvers
	for zone in dns_servers :
		resolvers[zone] = new_resolver(dns_servers[zone])
	return

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="IP address to lookup")
	args = parser.parse_args()	
	build_resolvers()
	ip_reverse = reversename.from_address(args.ip)
	for zone in resolvers:
		print zone, resolvers[zone].query(ip_reverse)
	
if __name__ == '__main__' :
	main()