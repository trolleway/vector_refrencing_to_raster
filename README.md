# vector_to_raster
refrencing vector geodata to aerial photo from WIkimaps Warper using ogr2ogr

# Usage

1. Find an aerial photography on Wikimedia Commons
2. Edit description of photo in Wikimedia. Change {{Information}} template to {{Map}}. A link to Wikimaps Warper will appear on File: page.
3. Click a link to Wikimaps Warper, login with Wikimedia account, make a georefrence photo to OSM using Thin Plate algorithm.

4. Fill in gcp.py URLs, and path to source vector layer.
6. python gcp.py
7. Add in QGIS photo and refed.gpkg - it will be overlayed, in local coordinates.
