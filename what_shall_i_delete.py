import os
import math


def human_read_format(data):
    pow = 0
    if data:
        pow = math.floor(math.log(data, 1024))
    n_bytes = ["Б", "КБ", "МБ", "ГБ", "ТБ", "ПБ", "ЭБ", "ЗБ", "ЙБ"]
    return f"{round(data / 1024 ** pow)}{n_bytes[pow]}"


def get_folder_size(start_path):
    total_size = 0
    for path, _, filenames in os.walk(start_path):
        for filename in filenames:
            total_size += os.path.getsize(os.path.join(path, filename))
    return total_size


def get_folders_sizes(parent_directory):
    folders = {}
    for directory in os.listdir(parent_directory):
        full_path = os.path.join(parent_directory, directory)
        if os.path.isdir(full_path):
            folders[directory] = get_folder_size(full_path)
    sorted_dirs = sorted(folders.items(), key=lambda key_value_pair: key_value_pair[1], reverse=True)[:10]
    output = ''
    for dir in sorted_dirs:
        output += f'{dir[0]:<20}{human_read_format(dir[1]):>15}\n'
    return output

print('Welcome to Cleanup Helper v0.1!')
print('Want to get the 10 largest subdirectories in directory?')
print('Just put in a path to that directory:')
print("Excellent! Here are the results:\n" + get_folders_sizes(input()))
