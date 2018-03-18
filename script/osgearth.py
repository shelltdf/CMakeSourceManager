
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("osg" , list_name,getDependency)
    # list_name = addDependency(str_name , list_name)
    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name)
    
    # getLibrary( "osg" ,dict_config, b_only_download )
    
    download_source(str_name,"https://github.com/gwaldron/osgearth.git")
    
    STR_CFG = " -DGDAL_INCLUDE_DIR='../../install/include/gdal'"
    STR_CFG += " -DGDAL_LIBRARY='../../install/lib/x86/gdal111.lib'"
    
    configure(str_name,STR_CFG)
    build(str_name)
    install(str_name)
    
    