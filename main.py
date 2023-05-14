import xmltodict

with open('7.osm', 'r', encoding='utf-8') as f:
    dct = xmltodict.parse(f.read())

hotels = {}
for node in dct['osm']['node']:
    if 'tag' in node:
        tags = node['tag']
        if isinstance(tags, list):
            for tag in tags:
                if tag['@k'] == 'tourism' and tag['@v'] == 'hotel':
                    name = node.get('name', 'Unnamed Hotel')
                    hotel_type = node.get('hotel', 'Unknown')
                    if hotel_type not in hotels:
                        hotels[hotel_type] = set()
                    hotels[hotel_type].add(name)

print('Total number of hotels:', sum(len(h) for h in hotels.values()))
for hotel_type, names in sorted(hotels.items()):
    print(f"{hotel_type}: {', '.join(sorted(names))}")
