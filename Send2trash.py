import send2trash
baconFile = open('bacon.txt', 'a') # cria o arquivo
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
send2trash.send2trash('bacon.txt')