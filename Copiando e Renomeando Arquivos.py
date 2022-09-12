import shutil, os
os.chdir('C:\\')
shutil.copy('C:\\spam.txt', 'C:\\delicious') #copia o arquivo
'C:\\delicious\\spam.txt'
shutil.copy('eggs.txt', 'C:\\delicious\\eggs2.txt') #copia o arquivo e renomeia
'C:\\delicious\\eggs2.txt'