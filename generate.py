import ConfigParser

Config = ConfigParser.ConfigParser()

cfgfile = open("metadata.ini", 'w')

Config.add_section('general')
Config.set('general', 'author', 'John Doe')
Config.set('general', 'email', 'john_doe@microsoft.com')

collections = []
for i in range(1000):
    collections.append('collection_%s' % i)
Config.set('general', 'collections', ','.join(collections))

for i, collection in enumerate(collections):
    Config.add_section(collection)
    Config.set(collection, 'name', 'Collection %s'%i)
    Config.set(collection, 'tags', 'a, b, c, d')
    Config.set(collection, 'description', 'description collection %s' %i)
    Config.set(collection, 'qgis_minimum_version', '2.0')
    Config.set(collection, 'qgis_maximum_version', '2.99')

Config.write(cfgfile)
cfgfile.close()
