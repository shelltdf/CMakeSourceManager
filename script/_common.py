
# import git
# from git import Repo
import os

def my_exec( str_cmd ):
    print "exec - "  + str_cmd
    
    if(True):
        os.system(str_cmd)
    else:
        ps = subprocess.Popen(str_cmd)
        ps.wait()

def my_build_and_install_dir(dict_config):
    dir_name = ""
    dir_name += dict_config['arch']
    
    if(dict_config['static']==True):
        dir_name += '_static'
    if(dict_config['dynamic']==True):
        dir_name += '_dynamic'
        
    if(dict_config['arch'][:2]=="vs"):
        return dir_name
        
    if(dict_config['debug']==True):
        dir_name += '_debug'
    if(dict_config['release']==True):
        dir_name += '_release'
    return dir_name
    
        
def my_into_build_dir( str_name , dict_config ):

    if(os.path.isdir("build")==False):
        os.system( "mkdir build" )
    os.chdir( "build" )
    
    dir_name = my_build_and_install_dir(dict_config)
        
    if(os.path.isdir(dir_name)==False):
        os.system( "mkdir " + dir_name)
    os.chdir( dir_name )
    
    if(os.path.isdir(str_name)==False):
        os.system( "mkdir " + str_name )
    os.chdir( str_name )
    
    
def my_out_build_dir( str_name ):
    os.chdir( ".." )
    os.chdir( ".." )
    os.chdir( ".." )
    
    
def my_into_source_dir( str_name ):

    if(os.path.isdir("source")==False):
        os.system( "mkdir source" )
    os.chdir( "source" )
    
    if(os.path.isdir(str_name)==False):
        os.system( "mkdir " + str_name)
    os.chdir( str_name )
    
def my_out_source_dir():
    os.chdir( ".." )
    os.chdir( ".." )
    
    
def addDependency( str_name , list_name ,getDependency ):

    list_sn = []        
    list_sn += getDependency(str_name) 
    
    list_sn += [str_name]
    list_name = list_sn + list_name
    
    for a in range(0, len(list_name)):
        for b in range(a+1, len(list_name)):
            if list_name[a] == list_name[b] :
                list_name[b] = ""
    
    list_ret = []
    for a in range(0, len(list_name)):
        if list_name[a] != "":
            list_ret += [list_name[a]]
            
    return list_ret
    

def download_source(str_name , str_git_url , str_branch='master'):
    e = os.path.isdir("./source/" + str_name + "/.git") 
    if(e):
        print str_name + " git is exist"
        my_exec( "git fetch" )
        
    else:
        print "clone git : " + str_git_url
        # git.Git("./source/" + str_name).clone(str_git_url)
        # Repo.clone_from(str_git_url, "./source/" + str_name ,branch=str_branch)
        
        # my_into_source_dir( str_name )
        
        cmd = "git clone --branch " + str_branch + " " + str_git_url +" ./source/"+str_name 
        my_exec( cmd )
        
        # my_out_source_dir()
        
    
def configure(str_name ,dict_config, str_config = ""):
    my_into_build_dir( str_name ,dict_config )
    dir_name = my_build_and_install_dir(dict_config)
    
    BUILD_TYPE = ""
    BUILD_STATIC_LIB = ""
    if(dict_config['static']==True):
        BUILD_STATIC_LIB = " -DBUILD_STATIC_LIB=1"
    if(dict_config['dynamic']==True):
        BUILD_STATIC_LIB = " -DBUILD_STATIC_LIB=0"
        
    if(dict_config['arch'][:2]!="vs"):
        if(dict_config['debug']==True):
            BUILD_TYPE = ' -DBUILD_TYPE=debug'
        if(dict_config['release']==True):
            BUILD_TYPE = ' -DBUILD_TYPE=release'
        
    
    # e = os.path.isfile("CMakeCache.txt") 
    # if(e):
        # print str_name + "configure is exist"
    # else:
    my_exec( "cmake ../../../source/" + str_name + 
    " -DCMAKE_INSTALL_PREFIX='../../../install/" + dir_name + "' " +
    dict_config['cmake_cfg'] + BUILD_TYPE + BUILD_STATIC_LIB + str_config )
    
    my_out_build_dir( str_name )
    
    
def build(str_name,dict_config):
    my_into_build_dir( str_name ,dict_config)
    if(dict_config['arch'][:2]=="vs"):
        if(dict_config['debug']==True):
            os.system('msbuild ALL_BUILD.vcxproj /p:Configuration=Debug')
        if(dict_config['release']==True):
            os.system('msbuild ALL_BUILD.vcxproj /p:Configuration=Release')
    else:
        os.system('make')
    my_out_build_dir( str_name )
    pass
    
def install(str_name,dict_config):
    my_into_build_dir( str_name ,dict_config)
    if(dict_config['arch'][:2]=="vs"):
        if(dict_config['debug']==True):
            os.system('msbuild INSTALL.vcxproj /p:Configuration=Debug')
        if(dict_config['release']==True):
            os.system('msbuild INSTALL.vcxproj /p:Configuration=Release')
    else:
        os.system('make install')
    my_out_build_dir( str_name )
    pass
    