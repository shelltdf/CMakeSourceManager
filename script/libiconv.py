
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    # list_name = addDependency(str_name , list_name)
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name)
    
    # download_source(str_name,"https://github.com/LuaDist/libiconv.git")
    download_source(str_name,"https://github.com/vovythevov/libiconv-cmake.git")
    configure(str_name)
    build(str_name)
    install(str_name)
    
    