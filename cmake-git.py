
import os.path
import sys
from pprint import pprint

def findScript(str_name):

    #find script
    e = os.path.isfile("./script/" + str_name + ".py") 
    if(e == False):
        print str_name + "is not exist"
        return False
    
    #import script
    s = __import__('script.' + str_name)
    val = getattr(s, str_name)

    return val
    
def getDependency( str_name ):
    val = findScript(str_name)
    
    list_name = val.getDependency( str_name ,getDependency )
    return list_name;


def getLibrary( str_name , b_only_download ,dict_config ):
    val = findScript(str_name)
    
    #do script
    val.SBI( str_name , b_only_download ,dict_config, getLibrary )
    

def main():
    # print "start"
    
    ARG_COM = "install" # "source" / "install" 
    ARG_NAME = ""
    
    if len(sys.argv) >= 3:
        ARG_COM = sys.argv[1]
        ARG_NAME = sys.argv[2]
    else:
        return
        
    # print( ARG_COM  + " " + ARG_NAME )
    
    
    dict_config = {'release': True, 'static': False}

    # getLibrary( ARG_NAME , ARG_COM == "source" , dict)
    
    list_name = getDependency( ARG_NAME )
    print list_name
    
    for x in list_name:
        getLibrary( x , ARG_COM == "source" , dict_config )
    
    
if __name__ == "__main__":
    main()
