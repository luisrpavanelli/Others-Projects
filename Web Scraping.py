import webbrowser, sys, pyperclip
if len(sys.argv) > 1:
# Obtém o endereço da linha de comando.
 address = '870 Valencia St, San Francisco, CA 94110'.join(sys.argv[1:])
else:
# Obtém o endereço do clipboard.
 address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
