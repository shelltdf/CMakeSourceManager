
from ._common import *

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("osg" , list_name,getDependency)
    list_name = addDependency("geos" , list_name,getDependency)

    return list_name + [str_name]
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):

    # download_source(str_name,"https://github.com/gwaldron/osgearth.git")
    download_source(str_name,"https://github.com/shelltdf/osgearth.git","2.8")
    if(b_only_download):
        return
    
    dir_name = my_build_and_install_dir(dict_config)
    
    STR_CFG = " -DGDAL_INCLUDE_DIR='../../../install/" + dir_name + "/include/gdal'"
    if(dict_config['release']):
        STR_CFG += " -DGDAL_LIBRARY='../../../install/" + dir_name + "/lib/gdal111.lib'"
        STR_CFG += " -DCURL_LIBRARY='../../../install/" + dir_name + "/lib/libcurl_imp.lib'"
    else:
        STR_CFG += " -DGDAL_LIBRARY='../../../install/" + dir_name + "/lib/gdal111d.lib'"
        STR_CFG += " -DCURL_LIBRARY='../../../install/" + dir_name + "/lib/libcurl-d_imp.lib'"
        STR_CFG += " -DOPENTHREADS_LIBRARY='../../../install/" + dir_name + "/lib/OpenThreadsd.lib'"
        STR_CFG += " -DOSG_LIBRARY='../../../install/" + dir_name + "/lib/osgd.lib'"
        STR_CFG += " -DOSGDB_LIBRARY='../../../install/" + dir_name + "/lib/osgDBd.lib'"
        STR_CFG += " -DOSGFX_LIBRARY='../../../install/" + dir_name + "/lib/osgFXd.lib'"
        STR_CFG += " -DOSGGA_LIBRARY='../../../install/" + dir_name + "/lib/osgGAd.lib'"
        STR_CFG += " -DOSGMANIPULATOR_LIBRARY='../../../install/" + dir_name + "/lib/osgManipulatord.lib'"
        STR_CFG += " -DOSGSHADOW_LIBRARY='../../../install/" + dir_name + "/lib/osgShadowd.lib'"
        STR_CFG += " -DOSGSIM_LIBRARY='../../../install/" + dir_name + "/lib/osgSimd.lib'"
        STR_CFG += " -DOSGTERRAIN_LIBRARY='../../../install/" + dir_name + "/lib/osgTerraind.lib'"
        STR_CFG += " -DOSGTEXT_LIBRARY='../../../install/" + dir_name + "/lib/osgTextd.lib'"
        STR_CFG += " -DOSGUTIL_LIBRARY='../../../install/" + dir_name + "/lib/osgUtild.lib'"
        STR_CFG += " -DOSGVIEWER_LIBRARY='../../../install/" + dir_name + "/lib/osgViewerd.lib'"
        STR_CFG += " -DOSGWIDGET_LIBRARY='../../../install/" + dir_name + "/lib/osgWidgetd.lib'"
    
    
    configure(str_name,dict_config,STR_CFG)
    build(str_name,dict_config)
    install(str_name,dict_config)
    
    