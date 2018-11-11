
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("gdal" , list_name,getDependency)
    list_name = addDependency("libpng" , list_name,getDependency)
    list_name = addDependency("freetype" , list_name,getDependency)
    list_name = addDependency("jasper" , list_name,getDependency)

    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    # download_source(str_name,"https://github.com/openscenegraph/OpenSceneGraph.git")
    download_source(str_name,"https://github.com/shelltdf/OpenSceneGraph.git","OpenSceneGraph-3.4")
    if(b_only_download):
        return
    
    dir_name = my_build_and_install_dir(dict_config)
    
    STR_CFG = " -DGDAL_INCLUDE_DIR='../../../install/" + dir_name + "/include/gdal'"
    
    if(dict_config['release']):
        STR_CFG += " -DGDAL_LIBRARY='../../../install/" + dir_name + "/lib/gdal111.lib'"
    else:
        STR_CFG += " -DGDAL_LIBRARY='../../../install/" + dir_name + "/lib/gdal111d.lib'"
    
    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    