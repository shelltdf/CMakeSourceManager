
# import git
from git import Repo
import os

def my_exec( str_cmd ):
    print "exec - "  + str_cmd
    
    if(True):
        os.system(str_cmd)
    else:
        ps = subprocess.Popen(str_cmd)
        ps.wait()
        
def my_into_build_dir( str_name ):
    if(os.path.isdir("build")==False):
        os.system( "mkdir build" )
    os.chdir( "build" )
    if(os.path.isdir(str_name)==False):
        os.system( "mkdir " + str_name )
    os.chdir( str_name )
    
def my_out_build_dir( str_name ):
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

    else:
        print "clone git : " + str_git_url
        # git.Git("./source/" + str_name).clone(str_git_url)
        Repo.clone_from(str_git_url, "./source/" + str_name ,branch=str_branch)

    
def configure(str_name , str_config = ""):
    my_into_build_dir( str_name )
    # e = os.path.isfile("CMakeCache.txt") 
    # if(e):
        # print str_name + "configure is exist"
    # else:
    my_exec( "cmake ../../source/" + str_name + " -DCMAKE_INSTALL_PREFIX='../../install' " + str_config )
    my_out_build_dir( str_name )
    
    
def build(str_name):
    my_into_build_dir( str_name )
    os.system('msbuild ALL_BUILD.vcxproj /p:Configuration=Release')
    my_out_build_dir( str_name )
    pass
    
def install(str_name):
    my_into_build_dir( str_name )
    os.system('msbuild INSTALL.vcxproj /p:Configuration=Release')
    my_out_build_dir( str_name )
    pass
    