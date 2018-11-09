## 依赖环境

* CMake
* python2 (当前版本还不支持python3)


##编译开关

* dynamic / static 
* release / debug 

##编译架构[尚未支持]

* HOST编译器：msvc mingw cygwin gcc clang emc
* 交叉编译目标：native ndk
* 位宽：32 64
  
##编译说明

### Visual Studio 2015
### Visual Studio 2017
1. 启动vs控制台

2. 输入命令（假设编译zlib，使用vs2017编译32bit版本）

```
python cmake-git.py source zlib
python cmake-git.py install zlib -arch vs2017-32 [-release] [-debug] [-dynamic] [-static]
```

3. 等待结束

