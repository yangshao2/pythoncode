import rasterio
import geopandas
from rasterio.mask import mask
from shapely.geometry import box

with rasterio.open('LE70140342019145EDC00_ETa.tif') as dataset:
    bounds  = dataset.bounds
    df = geopandas.GeoDataFrame({"id":1,"geometry":[box(*bounds)]})
    df.crs = dataset.crs
    df.to_file("boundary.shp")

lc = rasterio.open('/media/newhd/yshao/lc1mdata/Baywide_13Class_20132014.tif')
gdf = geopandas.read_file('boundary.shp')
gdf1 = gdf.to_crs(lc.crs)

def getFeatures(gdf):
    """Function to parse features from GeoDataFrame in such a manner that rasterio wants them"""
    import json
    return [json.loads(gdf.to_json())['features'][0]['geometry']]

coords = getFeatures(gdf1)

#mask image
out_img, out_transform = mask(lc, shapes=coords, crop=True)

out_meta = lc.meta.copy()
out_meta.update({"driver": "GTiff",
                 'dtype': 'uint8',
                 "height": out_img.shape[1],
                 "width":  out_img.shape[2],
                 "transform": out_transform})
out_tif= "subset.tif"
with rasterio.open(out_tif, "w", **out_meta) as dest:
    dest.write(out_img)





