import xmltodict
import os
import json
import pandas as pd

def get_files (file, values):
    print(f'Pegou informações do arquivo {file}.')
    with open(f'./nfs/{file}', 'rb') as xml_file:
        file_dict = xmltodict.parse(xml_file)
        
        try:
            if 'NFe' in file_dict:                
                infos_nf = file_dict['NFe']['infNFe']
            else:
                infos_nf = file_dict['nfeProc']['NFe']['infNFe']
            note_number = infos_nf['@Id']
            company_emit = infos_nf['emit']['xNome']
            client_name =  infos_nf['dest']['xNome']
            adress = infos_nf['dest']['enderDest']
            if 'vol' in infos_nf['transp']:
                weight = infos_nf['transp']['vol']['pesoB']
            else:
                weight = 'Peso não informado.'
            values.append([note_number, company_emit, client_name, adress, weight])
        except Exception as e:
            print(e)
            print(json.dumps(file_dict, indent=4))
            
files_list = os.listdir('./nfs')

columns = ['numero_nota', 'empresa_emissora', 'nome_cliente', 'endereço', 'peso']
values = []

for file in files_list:
    get_files(file, values)

chart = pd.DataFrame(columns=columns, data=values)
chart.to_excel('NotasFiscais.xlsx', index=False)
