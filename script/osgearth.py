
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("osg" , list_name,getDependency)
    list_name = addDependency("geos" , list_name,getDependency)

    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    # download_source(str_name,"https://github.com/gwaldron/osgearth.git")
    download_source(str_name,"https://github.com/shelltdf/osgearth.git")
    if(b_only_download):
        return
    
    dir_name = my_build_and_install_dir(dict_config)
    
    STR_CFG = " -DGDAL_INCLUDE_DIR='../../../install/" + dir_name + "/include/gdal'"
    STR_CFG += " -DGDAL_LIBRARY='../../../install/" + dir_name + "/lib/gdal111.lib'"
    
    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    