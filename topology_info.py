import requests

#OpenDayLight RESTCONF API settings.
#TODO: Replace <ip_address>
odl_url = 'http://<ip_address>:8181/restconf/operational/network-topology:network-topology'
odl_username = 'admin'
odl_password = 'admin'

# Fetch information from API.
response = requests.get(odl_url, auth=(odl_username, odl_password))

# Find information about nodes in retrieved JSON file.
for nodes in response.json()['network-topology']['topology']:

    # Walk through all node information.
    node_info = nodes['node']

    # Look for MAC and IP addresses in node information.
    for node in node_info:
        try:
            ip_address  = node['host-tracker-service:addresses'][0]['ip']
            mac_address = node['host-tracker-service:addresses'][0]['mac']
            print('Found host with MAC address %s and IP address %s' % (mac_address, ip_address))
        except:
            pass
