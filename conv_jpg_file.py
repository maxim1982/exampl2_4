import subprocess
import os

dir_in = 'Source'
dir_out = 'Resault'

try:
    os.mkdir(dir_out, mode=0o777)
except:
    print('Директория уже создана.')

print('Обрабатываем файлы jpg в каталоге ', dir_in)

path_run = os.getcwd() + '\\'
path_source = os.path.abspath(dir_in) + '\\'
path_res = os.path.abspath(dir_out) + '\\'

print(path_run,path_source,path_res)

print('И записываем файлы jpg в каталоге ', dir_out)

for file in os.listdir(path_source):
    if (os.path.isfile(path_source + file)):
            subprocess.call([path_run + 'convert.exe', path_source + file, '-resize', '200', path_res+'out_'+file ])
            print(path_source + file)


