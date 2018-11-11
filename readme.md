# CMake Source Manager

这是一个基于cmake和python的自动化代码下载和编译工具。目的是为了方便大量第三方库的编译和部署。

主要目的还是为了方便osg和osgEarth的开发。以后也会支持其他库。



## 依赖环境

* CMake
* python2 / python3 同时支持

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


##依赖关系

``` mermaid
graph LR
	anttweakbar
	boost
    curl --> zlib
    draco
    eigen
    flann
    freeglut
    freetype --> libpng
    gdal --> libpng
    gdal --> libgeotiff
    gdal --> libiconv
    gdal --> curl
    gdal --> libjpeg
    gdal --> proj4
    geos
    glew
    ifcplusplus --> osg
    ifcplusplus --> boost
    leveldb
    libbzip2
    libgeotiff --> libtiff
    libiconv
    libjpeg
    liblas --> boost
    libpng --> zlib
    libtiff --> zlib
    libtiff --> libjpeg
    ogre3d
    ork --> stb
    ork --> tinyxml
    ork --> glew
    ork --> freeglut
    ork --> pthread
    osg --> gdal
    osg --> libpng
    osg --> freetype
    osgearth --> osg
    osgearth --> geos
    osgeffect --> osg
    osgentity --> osg
    osgsplit --> osg
    osgsplit --> boost
    osgsplit --> ifcplusplus
    osgsplit --> liblas
    osgsplit --> osgeffect
    osgsplit --> osgentity
    paraview
    proj4
    proland --> ork
    proland --> anttweakbar
    proland --> libtiff
    pthread
    qhull
    stamen
    stb
    tinyxml
    zlib
    _FBX_SDK
    _Qt
    _SilverLining
    _Triton
    
```