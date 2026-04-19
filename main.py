import geopandas as gpd
import rasterio
from rasterstats import zonal_stats

VECTOR_PATH = 'data/infrastructure.shp'
RASTER_PATH = 'data/flood_risk.tif'
OUTPUT_PATH = 'output/flood_risk_assessment.geojson'

infra = gpd.read_file(VECTOR_PATH)

with rasterio.open(RASTER_PATH) as src:
    raster_crs = src.crs

if infra.crs != raster_crs:
    infra = infra.to_crs(raster_crs)

stats = zonal_stats(
    infra,
    RASTER_PATH,
    stats=['mean'],
    nodata=-9999
)

infra['flood_risk_index'] = [
    s['mean'] if s and 'mean' in s else None for s in stats
]

infra.to_file(OUTPUT_PATH, driver="GeoJSON")

print("✔ Flood risk analysis completed successfully.")
