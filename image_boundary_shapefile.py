import rasterio
import rasterio.features
import rasterio.warp
from shapely.geometry import box
import geopandas as gpd

with rasterio.open('LE70140342019145EDC00_ETa.tif') as dataset:
    bounds  = dataset.bounds
    df = gpd.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
    df.crs = dataset.crs
    df.to_file("boundary.shp")
