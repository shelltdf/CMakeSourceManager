
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("libtiff" , list_name,getDependency)
    # list_name = addDependency(str_name , list_name)
    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name)
    
    # getLibrary( "libtiff" ,dict_config, b_only_download )
    
    # download_source(str_name,"https://github.com/smanders/libgeotiff.git")
    download_source(str_name,"https://github.com/shelltdf/libgeotiff.git")
    configure(str_name," -DBUILD_SHARED_LIBS=1 ")
    build(str_name)
    install(str_name)
    