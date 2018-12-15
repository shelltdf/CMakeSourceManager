
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("zlib" , list_name,getDependency)
    list_name = addDependency("libjpeg" , list_name,getDependency)

    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    if(b_only_download):
        # download_source(str_name,"https://gitlab.com/libtiff/libtiff.git")
        # download_source(str_name,"https://github.com/LuaDist/libtiff.git")
        download_source(str_name,"https://github.com/shelltdf/libtiff.git")
        # download_source(str_name,"https://github.com/shelltdf/libtiff.git","branch-3.9") #for TIFFClientOpen()
        
        return
        
    STR_CFG = " "

    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    