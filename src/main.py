import os


print('BULK FILE RENAME TOOL - PROJECT')


current_folder = os.getcwd()
print(f'Current folder: {current_folder}')

os.chdir('..')
os.chdir('testing_files')
current_folder = os.getcwd()
print(f'Current folder: {current_folder}')

folder_obj = os.listdir()   # all files and directories in catalog
print(f'All catalog objects: {folder_obj}')

print('Delete dirs objects')

for obj in folder_obj:
    obj_path = current_folder + '\\' + obj
    print(f'Object path: {obj_path}')
    if not os.path.isfile(obj_path):
        folder_obj.remove(obj)


print(f'Edited all catalog objects: {folder_obj}')

# os.rename('test.txt', 'test_edited.txt')

print('Renaming...')

counter = 1
for obj in folder_obj:
    os.rename(obj, f'File{counter}.txt')
    counter += 1

print('Ready')
