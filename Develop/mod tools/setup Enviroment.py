print('Setting up Enviroment...')
import subprocess
subprocess.popen('pip install --upgrade google-api-python-client')
subprocess.popen('pip install --upgrade json-config')
subprocess.popen('pip install --upgrade faker')
import webbrowser
print('you will need to install pygame seperately. once finished installing press enter.(WARNING: USE py2.7 files!)')
webbrowser.open_new_tab('http://www.pygame.org/download.shtml')
raw_input()
print('think thats about it! we are finished with installation!')
raw_input()