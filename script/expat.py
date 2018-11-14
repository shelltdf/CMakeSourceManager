
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    download_source(str_name,"https://github.com/libexpat/libexpat.git")
    if(b_only_download):
        return
        
    STR_CFG = ''
    # if(dict_config['static']):
        # STR_CFG += ''
    # else:
        # STR_CFG += ''
    
    configure(str_name,dict_config,STR_CFG,'expat')
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    