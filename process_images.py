import os
import shutil
import glob


UUID = os.getenv('UUID')
TYPE = os.getenv('TYPE')

path= TYPE+'/'+UUID+'/raw/*'

files = glob.glob(path)

os.mkdir(TYPE+'/'+UUID+"/processed/")

for file in files:
    #file_path= "type-1-imaging/2020-07-28-rezaee/processed/"+ file.rsplit('/', 1)[-1]
    processed_file_path= TYPE+'/'+UUID+"/processed/"+ file.rsplit('/', 1)[-1]
    shutil.move(file, processed_file_path)
    print('Moved',file,'to processed')
