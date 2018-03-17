
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    # list_name = addDependency(str_name , list_name,getDependency)
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name)
    
    download_source(str_name,"https://github.com/madler/zlib.git")
    
    # STR_CGG = ''
    # if(dict_config['static']):
        # STR_CGG += ''
    # else:
        # STR_CGG += ''
    
    configure(str_name)
    build(str_name)
    install(str_name)
    
    