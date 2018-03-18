
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    
    # download_source(str_name,"https://github.com/hunter-packages/jpeg.git")
    # download_source(str_name,"https://github.com/LuaDist/libjpeg.git")
    download_source(str_name,"https://github.com/stohrendorf/libjpeg-cmake.git")
    configure(str_name)
    build(str_name)
    install(str_name)
    
    