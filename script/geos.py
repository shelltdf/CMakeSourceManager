
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    # download_source(str_name,"https://github.com/OSGeo/geos.git","3.5.0")
    download_source(str_name,"https://github.com/shelltdf/geos.git")
    if(b_only_download):
        return
        
    STR_CFG = ' -DGEOS_ENABLE_TESTS=0'

    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    