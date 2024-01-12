import xmltodict
import os

def get_files (file):
    print(f'Pegou informações do arquivo {file}.')
    with open(f'./nfs/{file}', 'r') as xml_file:
        file_dict = xmltodict.parse(xml_file)

files_list = os.listdir('./nfs')

for file in files_list:
    get_files(file)