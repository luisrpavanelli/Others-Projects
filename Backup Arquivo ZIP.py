# BackupToZip.py – Copia uma pasta toda e seu conteúdo para
# um arquivo ZIP cujo nome seja incrementado.
import zipfile, os
def backupToZip(folder):
  # Faz backup de todo o conteúdo de "folder" em um arquivo ZIP.
  folder = os.path.abspath(folder) # garante que folder é um path absoluto
  # Determina o nome do arquivo que esse código deverá usar de acordo com
  # os arquivos já existentes.
number = 1
while True:
   zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
   if not os.path.exists(zipFilename):
    break
number = number + 1
  # TODO: Cria o arquivo ZIP.
  # TODO: Percorre toda a árvore de diretório e compacta os arquivos de cada pasta.
print('Done.')
backupToZip('C:\\delicious')