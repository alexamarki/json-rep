import shutil
import datetime


def make_reserve_arc(source, dest):
    current_datetime_sec = str(datetime.datetime.now()).split('.')[0]
    dt_for_filename = '_archive_at_' + current_datetime_sec.replace(' ', '_').replace(':', '-')
    source_arc_name = source.strip().split('/')[-1] + dt_for_filename
    shutil.make_archive(source_arc_name, 'zip', root_dir=source)
    shutil.move('./' + source_arc_name + '.zip', dest)
    return current_datetime_sec


print('Welcome to archiver v0.1!')
print('Please input a path to the directory the contents of which you want to archive:')
source_folder = input()
print('Thank you! Now, input a path to the directory you want to put the archive into:')
dest_folder = input()
print('Excellent! Creating your archive now...')
datetime_msg = make_reserve_arc(source_folder, dest_folder)
print(f'...done! Made an archive of folder at {source_folder} in {dest_folder}')
print(f'Time of archival: {datetime_msg}')
