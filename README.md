# map-fun

This is just a quick repo I put together to play around with GitHub's visualization of geographic data. The only interesting thing here is thte gpx_to_geogson.py script that can be used to take a series of GPX files containing a series of points (latitude and longitude) and converting them to a series of lines within a geojson object.

If the file is too large you should run it through the [topojson utility](https://github.com/mbostock/topojson) to reduce the size.