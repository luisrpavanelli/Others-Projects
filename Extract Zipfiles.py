import zipfile, os
os.chdir('C:\\') # vai para a pasta que contém example.zip
exampleZip = zipfile.ZipFile('example.zip')
exampleZip.extractall()
exampleZip.close()