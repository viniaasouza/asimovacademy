import os

# Obtendo o diretório de trabalho atual
cwd = os.getcwd()

# Listando todos os arquivos e diretórios no diretório atual
full_list = os.listdir(cwd)

# Filtrando a lista para incluir apenas arquivos que não sejam .py
files_list = [i for i in full_list if os.path.isfile(i) and '.py' not in i]

# Obtendo os tipos de arquivos (extensões) únicos
types = list(set([i.split('.')[-1] for i in files_list]))

# Criando diretórios para cada tipo de arquivo, se ainda não existirem
for file_type in types:
    if not os.path.exists(file_type):
        os.mkdir(file_type)

# Movendo cada arquivo para o diretório correspondente ao seu tipo
for file in files_list:
    from_path = os.path.join(cwd, file)
    to_path = os.path.join(cwd, file.split('.')[-1], file)  # Incluindo o nome do arquivo no destino
    os.replace(from_path, to_path)

   


