import os.path
import shutil

tile_path = "M:/lidar/pimaTiles"
lidar_path = "M:/lidar/pima"

lidar_files = [os.path.basename(f) for f in os.listdir(lidar_path) if f.endswith('.laz')]
tile_files = [os.path.basename(f)[:-4] for f in os.listdir(tile_path) if f.endswith('laz.png')]


todo = [tile for tile in lidar_files if tile not in tile_files]
print(f"There are {len(todo)} files left to do in {lidar_path}")

destination_path = "C:/Users/crist/Documents/Local/mapant_local_data/in"
for file_name in todo[:20]:
    source_file = os.path.join(lidar_path, file_name)
    destination_file = os.path.join(destination_path, file_name)

    # shutil.copy2(source_file, destination_file)
    # print(f"Copied {source_file} to {destination_file}")

print("All done!")