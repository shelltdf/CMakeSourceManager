
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("libpng" , list_name,getDependency)
    list_name = addDependency("libgeotiff" , list_name,getDependency)
    list_name = addDependency("libiconv" , list_name,getDependency)
    list_name = addDependency("curl" , list_name,getDependency)
    list_name = addDependency("libjpeg" , list_name,getDependency)
    list_name = addDependency("proj4" , list_name,getDependency)
    list_name = addDependency("geos" , list_name,getDependency)
    list_name = addDependency("expat" , list_name,getDependency)

    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    if(b_only_download):
        # download_source(str_name,"https://github.com/aashish24/gdal-svn.git","cmake4gdal")
        download_source(str_name,"https://github.com/shelltdf/gdal-svn.git","cmake4gdal")
        
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
    
    dir_name = my_build_and_install_dir(dict_config)
    
    # STR_CFG += " -DCURL_INCLUDE_DIR='../../../install/" + dir_name + "/include/'"
    
    if(dict_config['release']):
        pass
        # STR_CFG += " -DCURL_LIBRARY='../../../install/" + dir_name + "/lib/libcurl_imp.lib'"
        # STR_CFG += " -Dgeotiff_LIBRARY='../../../install/" + dir_name + "/lib/geotiff.lib'"
        STR_CFG += " -DGEOS_LIBRARY='../../../install/" + dir_name + "/lib/geos_c.lib'"
        STR_CFG += " -DPROJ_LIBRARY='../../../install/" + dir_name + "/local/lib/proj_5_0.lib'"
        STR_CFG += " -DPROJ_INCLUDE_DIR='../../../install/" + dir_name + "/local/include/'"
    else:
        STR_CFG += " -DCURL_LIBRARY='../../../install/" + dir_name + "/lib/libcurl-d_imp.lib'"
        STR_CFG += " -Dgeotiff_LIBRARY='../../../install/" + dir_name + "/lib/geotiff_d.lib'"
        STR_CFG += " -DGEOS_LIBRARY='../../../install/" + dir_name + "/lib/geos_c.lib'"
        STR_CFG += " -DEXPAT_LIBRARY='../../../install/" + dir_name + "/lib/expatd.lib'"
        STR_CFG += " -DPROJ_LIBRARY='../../../install/" + dir_name + "/local/lib/proj_5_0_d.lib'"
        STR_CFG += " -DPROJ_INCLUDE_DIR='../../../install/" + dir_name + "/local/include/'"
        
    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    