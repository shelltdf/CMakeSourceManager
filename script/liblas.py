
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("boost" , list_name,getDependency)
    list_name = addDependency("libgeotiff" , list_name,getDependency)
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    download_source(str_name,"https://github.com/libLAS/libLAS.git")
    if(b_only_download):
        return
        
    STR_CFG = ''
    # STR_CFG += ' -DBoost_DIR=../../install/' + my_build_and_install_dir(dict_config) + '/'
    # STR_CFG += ' -DBoost_INCLUDE_DIR=../../install/' + my_build_and_install_dir(dict_config) + '/include'
    
    # STR_CFG += ' -DBoost_THREAD_LIBRARY_DEBUG=../../install/' + my_build_and_install_dir(dict_config) + '/lib/boost_thread-mt-gd'
    # STR_CFG += ' -DBoost_THREAD_LIBRARY_RELEASE=../../install/' + my_build_and_install_dir(dict_config) + '/lib/boost_thread-mt'
    
    STR_CFG += ' -DWITH_TESTS=0 -DWITH_UTILITIES=0'
    STR_CFG += ' -DBUILD_OSGEO4W=0'
    
    if(dict_config['static']):
        STR_CFG += ''
    else:
        STR_CFG += ''
        
        dir_name = my_build_and_install_dir(dict_config)
    if(dict_config['release']):
        pass
    else:
        STR_CFG += " -DGEOTIFF_LIBRARY='../../../install/" + dir_name + "/lib/geotiff_d.lib'"

    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    