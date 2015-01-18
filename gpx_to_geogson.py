#!/usr/bin/python

# Example run:
# python gpx_to_geogson.py /Users/danielgoldin/Downloads/runkeeper-data-export-4716231-2015-01-18-1726 2013 > runs.2013.geo.json
# python gpx_to_geogson.py /Users/danielgoldin/Downloads/runkeeper-data-export-4716231-2015-01-18-1726 > runs.all.geo.json

# And then after use topjson to reduce file size
# topojson -s -q 5e5 -o runs.2014.topo.json runs.2014.geo.json

import re
import os
import json
import sys

RE_LAT = re.compile('lat="(.+?)"')
RE_LON = re.compile('lon="(.+?)"')

def get_files(path, filt = None):
    if filt is not None:
        return [os.path.join(path,fn) for fn in next(os.walk(path))[2] if fn.endswith('.gpx') and filt in fn]
    else:
        return [os.path.join(path,fn) for fn in next(os.walk(path))[2] if fn.endswith('.gpx')]

def to_geojson(lines):
    coordinates = []
    for line in lines:
        if line.startswith('<trkpt'):
            lat = float(RE_LAT.findall(line)[0])
            lon = float(RE_LON.findall(line)[0])
            coordinates.append( [lon, lat] )
    return  {
                'type' : 'Feature',
                'geometry' : {
                    'type' : 'LineString',
                    'coordinates' : coordinates
                },
                'properties' : {
                    'file' : 'f'
                }
            }

if __name__ == '__main__':
    base_path = sys.argv[1]
    filt = None
    if len(sys.argv) > 2:
        filt =  sys.argv[2]

    paths = get_files(base_path, filt)

    j = { 'type' : 'FeatureCollection', 'features' : [] }

    for path in paths:
        with open(path, 'r') as f:
            lines = f.readlines()
            run_coords = to_geojson(lines)
            j['features'].append( run_coords )

    print json.dumps(j)