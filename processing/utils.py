import os.path
import shutil
from PIL import Image

def make_neighbors_pima(filename_base, num):
    '''Returns a list of filenames for tiles adjacent to num for Pima County data.'''

    factors = [-999, 1, 1001, -1000, 0, 1000, -1001, -1, 999]
    nums = [num + n for n in factors]
    filenames = [filename_base.replace('NUM', n) for n in nums]
    return filenames

def copy_files(source_path, destination_path, filenames, overwrite=False):
    '''Copies a list filenames of lidar tiles from source_path to destination_path.'''
    for file_name in filenames:
        print(file_name)
        source_file = os.path.join(source_path, file_name)
        destination_file = os.path.join(destination_path, file_name)

        if not overwrite and os.path.exists(destination_file):
            print(f"Skipping {file_name}. File already exists at destination.")
            continue

        shutil.copy2(source_file, destination_file)
        print(f"Copied {source_file} to {destination_file}")

def copy_cluster(source_path, destination_path, filename_base, num):
    '''Copies a lidar tile and all surrounding tiles from source_path to destination_path.'''
    filenames = make_neighbors(filename_base, num)
    copy_files(source_path, destination_path, filenames)

def find_incomplete(lidar_path, tile_path):
    '''Returns a list of complete filenames of tiles to be processed.'''
    lidar_files = [os.path.basename(f) for f in os.listdir(lidar_path) if f.endswith('.laz')]
    tile_files = [os.path.basename(f)[:-4] for f in os.listdir(tile_path) if f.endswith('laz.png')]

    todo = [tile for tile in lidar_files if tile not in tile_files]
    print(f"There are {len(todo)} files left to do in {lidar_path}")
    return todo

def delete_empty_tiles(tile_folder):
    '''Deletes all empty PNGs from a tile_folder and all child folders.'''
    file_count = 0
    dir_count = 0

    for root, dirs, files in os.walk(tile_folder, topdown=False):
        for filename in files:
            if filename.endswith('.png'):
                path = os.path.join(root, filename)
                try:
                    img = Image.open(path)
                    if img.getbbox() is None:  # Check if the image is fully transparent
                        os.remove(path)
                        file_count += 1
                        print(f"Deleted {filename}")
                except Exception as e:
                    print(f"Error processing {filename}: {str(e)}")

        # Remove empty folders
        for root, dirs, files in os.walk(tile_folder, topdown=False):
            for dir in dirs:
                dirpath = os.path.join(root, dir)
                if not os.listdir(dirpath):  # Check if the directory is empty
                    os.rmdir(dirpath)
                    dir_count += 1
                    print(f"Removed empty directory {dirpath}")

    print(f"Removed {file_count} files and {dir_count} directories")


