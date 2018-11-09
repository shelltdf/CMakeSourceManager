# CMake Source Manager

这是一个基于cmake和python的自动化代码下载和编译工具。目的是为了方便大量第三方库的编译和部署。

主要目的还是为了方便osg和osgEarth的开发。以后也会支持其他库。



## 依赖环境

* CMake
* python2 (当前版本还不支持python3)

##编译说明

1. 启动vs控制台

2. 输入命令（假设编译zlib，使用vs2015编译64bit版本）

```
python cmake-git.py source zlib
python cmake-git.py install zlib -arch vs2017-32 [-release] [-debug] [-dynamic] [-static]

// -arch 架构名称
vs2017-32
vs2017-64
vs2015-32
vs2015-64
vs2013-32
vs2013-64
vs2012-32
vs2012-64
vs2010-32
vs2010-64
```

3. 等待结束

## 编译框架支持列表

| 编译器    | dynamic release | dynamic debug | static release | static debug |
| --------- | ------- | ----- | ------------ | ----------- |
| vs2017-32 |         |       |              |             |
| vs2017-64 |         |       |              |             |
| vs2015-32 |         |       |              |             |
| vs2015-64 | 支持   | 支持 |  |             |


