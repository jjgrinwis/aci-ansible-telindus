import yaml
import csv

bds = dict(
    bds={}
)

csv_file = 'vlan-ids.csv'
yml_file = 'group_vars/all/bds.yaml'

with open(csv_file, 'rb') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        bd = 'bd_vlan' + row['VLAN']
        bds['bds'][bd] = {}
        bds['bds'][bd]['desc'] = str(row['Omschrijving']).replace(" ", "-")
        bds['bds'][bd]['vlan_id'] = int(row['VLAN'])
        bds['bds'][bd]['leafs'] = str(row['leafs'])
        bds['bds'][bd]['ipg'] = str(row['interface_policy_group'])

with open(yml_file,'w') as ymlfile:
    ymlfile.write(yaml.dump(bds, default_flow_style=False))
