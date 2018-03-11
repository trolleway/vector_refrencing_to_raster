
import urllib
import shutil
import os
import csv


photo_url = 'https://upload.wikimedia.org/wikipedia/commons/6/69/Domodedovo_city_aerial_view_%2818347077140%29.jpg'
gcp_url = 'http://warper.wmflabs.org/maps/2219/gcps.csv'
source = 'cropped.gpkg'


rasters_dir = 'temp'

if os.path.exists(rasters_dir):
    try:
        shutil.rmtree(rasters_dir)
    except:
        pass
if not os.path.exists(rasters_dir):
    os.makedirs(rasters_dir)
    
gcp_file = os.path.join(rasters_dir,"gcp.csv")
urllib.urlretrieve(photo_url, os.path.join(rasters_dir,"photo.jpg"))
urllib.urlretrieve(gcp_url, gcp_file)


gcp_option = ''

input_file = csv.DictReader(open(gcp_file))
for row in input_file:
    #print row
    gcp_part = ' -gcp {ungeoref_x} {ungeoref_y} {georef_x} {georef_y}  '.format(ungeoref_x=row['lon'], ungeoref_y=row['lat'], georef_x=row['x'], georef_y=str(0-float(row['y'])))
    
    gcp_option += gcp_part
   
ogr_string = 'ogr2ogr -f GPKG -progress -overwrite {gcp_option} -tps refed.gpkg "{source}"'.format(gcp_option=gcp_option,source=source)
print ogr_string
os.system(ogr_string)
        
