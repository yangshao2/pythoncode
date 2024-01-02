 conda create --name et1 python=3.9
 python -m ipykernel install --user --name et1 --display-name "et1"

conda activate et1
#install ipykernel and pip
conda install -c anaconda ipykernel
conda install pip

conda install gdal 

#install rasterio
conda config --add channels conda-forge
conda config --set channel_priority strict
conda install rasterio
#install pandas, geopandas (pip install works too)
pip install rasterio
pip install pandas
pip install geopandas

conda install -c conda-forge qgis


#use jupyter notebook, I suggest install package from notebook
!pip install rasterio
!pip install geopandas
