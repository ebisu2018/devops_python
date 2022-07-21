'''

编译语言和CPU的指令集有关，与操作系统有关，不是跨平台
解释语言需要虚拟机上运行，是跨平台

pypi，公共模块存储中心，pip install的时候会从pypi上下载包
pip是包管理工具，底层依赖于setuptools

打包以及安装都需要setup.py文件
之前包的格式是egg，现在都是whl，包含代码以及相关的元数据

关于打包发布
1. distutils, 用setup.py构建安装包，基本停用
2. setuptools，包管理的核心模块，是distutils的增强版，一般使用该模块！相当于Linux中的rpm
3. pip，包含在安装文件中，是setuptools的增强，用于包管理，相当于yum或apt
4. whl，不用本地编译，是二进制安装

python中标准库的代码放在Lib中，第三方的包放在site-packages下
python setup.py install，会把包安装到site-packages下

源代码打包的方式：
1. sdist方式，直接把源代码打包，生成了dist的目录的tar.gz压缩包
python setup.py sdist
源码分发依然用pip install方式安装到site-packages下

2. bdist方式，编译成二进制打包
python setup.py bdist
pip install xxx.whl安装到site-packages下

如果代码中包含了第三方包，打包不会带过去，需要写入requirements中
pip freeze > requirements
pip install -r requirements，在目标上自动安装


'''

from setuptools import setup

setup(
    name='m',
    version='0.1.1',
    author='author',
    url='https://www.portuguel.com',
    packages=['m1', 'm1.m2'], # 只会对包以及非子包py文件打包
    # py_modules=['t1'], # 加载不在包中的模块
    data_files=[('install', ['requirements'])], # 包含了requirements文件
    python_requires='>3.6'
)