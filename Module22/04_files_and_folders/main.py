import os

my_dir = 'Module14'
check_path = os.path.abspath(os.path.join('..', '..', my_dir))
print('Каталог для проверки:', check_path)

total_size = 0
total_files = 0
total_dir = 0
for dirpath, dirnames, filenames in os.walk(check_path):
    total_dir += len(dirnames)
    total_files += len(filenames)
    for file in filenames:
        path = os.path.join(dirpath, file)
        total_size += os.path.getsize(path)
print('Размер каталога (в Кб):', total_size / 1024)
print('Количество подкаталогов:', total_dir)
print('Количество файлов:', total_files)
