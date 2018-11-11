
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("zlib" , list_name,getDependency)

    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    download_source(str_name,"https://github.com/glennrp/libpng.git")
    if(b_only_download):
        return
        
    configure(str_name,dict_config)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    