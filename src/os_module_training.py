import os

from logging_setup import base_logger

print('BULK FILE RENAME TOOL - 🐱 PET PROJECT')

current_folder = os.getcwd()
print(f'Current folder: {current_folder}')

dir_path = input("Enter path to the dir:\n")
print(dir_path)
os.chdir('..')
os.chdir('testing_files')
current_folder = os.getcwd()
base_logger.info(f'Current folder: {current_folder}')

folder_obj = os.listdir()   # all files and directories in catalog
base_logger.info(f'All catalog objects: {folder_obj}')

base_logger.info('Remove dir objects from list')

for obj in folder_obj:
    obj_path = current_folder + '\\' + obj
    base_logger.info(f'Object path: {obj_path}')
    if not os.path.isfile(obj_path):
        folder_obj.remove(obj)


base_logger.info(f'Edited all catalog objects: {folder_obj}')

# os.rename('test.txt', 'test_edited.txt')

base_logger.info('Renaming...')

counter = 1
for obj in folder_obj:
    os.rename(obj, f'File{counter}.txt')
    counter += 1

base_logger.info('Ready')
