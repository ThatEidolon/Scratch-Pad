# This is a script to solve an issue with a customer's DNS
# It takes an IP as an imput, and queries multiple nameservers
# with a reverse lookup to see what each one believes to be the
# hostname.
# --Eid010n

from dns import resolver, reversename
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("IP", help="IP address to lookup")
args = parser.parse_args()

dns_servers = {'cde': '8.8.8.8', 'prod': '8.8.4.4'}
resolvers = {}

def new_resolver (dns_ip):
# takes the IP address of the specific DNS server as an argument	
# returns a resolver object
	temp = resolver.Resolver('configure=False')
	temp.nameservers = [dns_ip]
	return temp

def build_resolvers():
# builds a list of resolvers to use for DNS lookup
# stores in global dictionary resolvers
	for zone in dns_servers :
		resolvers[zone] = new_resolver(dns_servers[zone])
	return


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("ip", help="IP address to lookup")
	args = parser.parse_args()	
	build_resolvers()
	try:
		ip_reverse = reversename.from_address(args.ip)
	except:
		print "[-] Must use valid IP address"
		return
	for zone in resolvers:
		try:
			hostname = resolvers[zone].query(ip_reverse, "PTR")[0]
		except:
			hostname = ''
		finally:
			print zone, ' : ', hostname
	
if __name__ == '__main__' :
	main()
