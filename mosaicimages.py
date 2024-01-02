import glob
import subprocess
import os
import numpy as np
import rasterio
from osgeo import gdal,ogr,osr,gdalconst

os.chdir('/home/yshao/wri')


tfile=glob.glob('outputr*.tif')
tfile1=" ".join(str(x) for x in tfile)
os_vrt="gdalbuildvrt mosaic.vrt -srcnodata 0 " + tfile1
subprocess.run(os_vrt,shell=True)

os_mosaic="gdalwarp mosaic.vrt output.tif"
subprocess.run(os_mosaic,shell=True)
