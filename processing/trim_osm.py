import pathlib
import subprocess
import zipfile

import laspy

filepath = "C:/Users/crist/Documents/Local/LemmonTest/thinningTest/USGS_LPC_AZ_PimaCounty_2021_B21_527552.laz"

with laspy.open(filepath) as lazfile:
    x_min, y_min, _ = lazfile.header.mins
    x_max, y_max, _ = lazfile.header.maxs

print(f"Clip to: {x_min, y_min, x_max, y_max}")
ogr_command = f'ogr2ogr -spat {x_min} {y_min} {x_max} {y_max} trimmed_pima pima_projected'
subprocess.call(ogr_command)

osm_directory = pathlib.Path("trimmed_pima")
with zipfile.ZipFile("osm.zip", mode="w") as archive:
    for file_path in osm_directory.iterdir():
        archive.write(file_path, arcname=file_path.name)
        print("zip file written to: {file_path}")
