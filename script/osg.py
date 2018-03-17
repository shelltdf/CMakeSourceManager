
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("gdal" , list_name,getDependency)
    list_name = addDependency("libpng" , list_name,getDependency)
    # list_name = addDependency(str_name , list_name)
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name);
    
    # getLibrary( "gdal" ,dict_config, b_only_download )
    # getLibrary( "libpng" ,dict_config, b_only_download )
    
    download_source(str_name,"https://github.com/openscenegraph/OpenSceneGraph.git")
    configure(str_name)
    build(str_name)
    install(str_name)
    
    