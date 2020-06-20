from dnacentersdk import api
import json
import time
import calendar
from pprint import pprint

dna = api.DNACenterAPI(username="devnetuser", password="Cisco123!",
                       base_url="https://sandboxdnac2.cisco.com")

##### NETWORKS AND SITES ####

# Print Site Topology
sites = dna.networks.get_site_topology()
for site in sites.response.sites:
    for child_sites in sites.response.sites:
        if child_sites.parentId == site.id:
            print(f'{site.name} -> {child_sites.name}')
        for more_children in sites.response.sites:
            if more_children.parentId == child_sites.id and child_sites.parentId == site.id:
                print(f'{site.name} -> {child_sites.name} -> {more_children.name}')

# Print Vlans
vlans = dna.networks.get_vlan_details()
for vlan in vlans.response:
    print(vlan)

# Physical Topology Details
phys_top = dna.networks.get_physical_topology()
print(json.dumps(phys_top, indent=2, sort_keys=True))


############### DEVICES #############
# Print Device Details
devices = dna.devices.get_device_list()
for device in devices.response:
    print(device.type)
    print(device.hostname)
    print(device.managementIpAddress)
    print(device.id)
    print(" ")

# Get a specific device
device = dna.devices.get_device_by_id('72dc1f0a-e4da-4ec3-a055-822416894dd5')
pprint(device)


######## HEALTH CHECKS ################
############# CLIENTS ##############
# Get Client Health with Epoch Datetime
epoch_datetime = str(calendar.timegm(time.gmtime()))

client_health = dna.clients.get_overall_client_health(timestamp=epoch_datetime)

print(json.dumps(client_health, indent=2, sort_keys=True))
print(' ')
