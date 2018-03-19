
from _common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("libpng" , list_name,getDependency)
    list_name = addDependency("libgeotiff" , list_name,getDependency)
    list_name = addDependency("libiconv" , list_name,getDependency)
    list_name = addDependency("curl" , list_name,getDependency)
    list_name = addDependency("libjpeg" , list_name,getDependency)

    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    # download_source(str_name,"https://github.com/aashish24/gdal-svn.git","cmake4gdal")
    download_source(str_name,"https://github.com/shelltdf/gdal-svn.git","cmake4gdal")
    if(b_only_download):
        return
        
    STR_CFG = " -DGDAL_USE_OPENCL=0 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_BMP=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_DIMAP=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_GIF=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_JPEG=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_MEM=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_OZI=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_OZIMAP=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_PNG=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_POSTGISRASTER=0 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_RAW=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_SAGA=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_TIL=1 "
    STR_CFG += " -DGDAL_ENABLE_FRMT_WMS=1 "
    STR_CFG += " -DOGR_ENABLE_CSV=1 "
    STR_CFG += " -DOGR_ENABLE_DFX=1 "
    STR_CFG += " -DOGR_ENABLE_GPX=1 "
    STR_CFG += " -DOGR_ENABLE_LIBKML=0 "
    STR_CFG += " -DOGR_ENABLE_MEM=1 "
    STR_CFG += " -DOGR_ENABLE_MYSQL=0 "
    STR_CFG += " -DOGR_ENABLE_PG=0 "
    STR_CFG += " -DOGR_ENABLE_S57=1 "
    STR_CFG += " -DOGR_ENABLE_SHP=1 "
    STR_CFG += " -DOGR_ENABLE_SQLITE=0 "
    STR_CFG += " -DOGR_ENABLE_SXF=1 "
    STR_CFG += " -DOGR_ENABLE_VRT=1 "
    STR_CFG += " -DOGR_ENABLE_WFS=1 "
    
    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    