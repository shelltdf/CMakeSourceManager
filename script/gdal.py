
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("libgeotiff" , list_name,getDependency)
    list_name = addDependency("libiconv" , list_name,getDependency)
    list_name = addDependency("curl" , list_name,getDependency)
    list_name = addDependency("libjpeg" , list_name,getDependency)
    # list_name = addDependency(str_name , list_name)
    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    print(str_name)
    
    # getLibrary( "libgeotiff" ,dict_config, b_only_download )
    # getLibrary( "libiconv" ,dict_config, b_only_download )
    # getLibrary( "curl" ,dict_config, b_only_download )
    # getLibrary( "libjpeg" ,dict_config, b_only_download )
    
    download_source(str_name,"https://github.com/aashish24/gdal-svn.git","cmake4gdal")
    configure(str_name," -DGDAL_USE_OPENCL=0 ")
    build(str_name)
    install(str_name)
    
    