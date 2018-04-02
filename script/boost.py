
from _common import *
# import shutil

def getDependency( str_name ,getDependency):
    list_name = []
    
    list_name = addDependency("zlib" , list_name,getDependency)
    list_name = addDependency("libiconv" , list_name,getDependency)
    list_name = addDependency("libbzip2" , list_name,getDependency)
    
    return list_name + [str_name]
    
    
def SBI( str_name , b_only_download ,dict_config, getLibrary ):
    # print(str_name)
    
    # download_source(str_name,"https://github.com/boost-cmake/boost.git")
    # download_source(str_name,"https://github.com/microcai/boost.git")
    download_source(str_name,"https://github.com/Orphis/boost-cmake.git")
    if(b_only_download):
        return
        
    # STR_CGG = ''
    # if(dict_config['static']):
        # STR_CGG += ''
    # else:
        # STR_CGG += ''
    
    configure(str_name,dict_config)
    build(str_name,dict_config)
    # install(str_name,dict_config)
    
    rd_dir = ""
    if(dict_config['debug']==True):
        rd_dir += 'Debug'
    if(dict_config['release']==True):
        rd_dir += 'Release'
        
    dist_dir = my_build_and_install_dir(dict_config)
    dist_dir = os.getcwd() + '/install/' + dist_dir
    source_dir = my_build_and_install_dir(dict_config)
    source_dir = os.getcwd() + "/build/" + source_dir + "/" + str_name + "/" + rd_dir
    print source_dir
    print dist_dir
    copyfiles(source_dir,dist_dir+"/lib","*.lib")
    
    
    
    
    