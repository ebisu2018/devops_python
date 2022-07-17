'''

pypi，公共的模块存储中心，pip install的时候会从pypi上下载包
pip是包管理工具

打包工具
1. distutils, 用setup.py构建安装包
2. setuptools，包管理的核心模块，是distutils的增强版，一般使用该模块
3. pip，包含在安装文件中，是setuptools的增强，用于包管理
   3.4之前没有pip，需要执行python setup.py才可以安装pip
4. wheel，zip打包的扩展名为whl，之前都是egg文件，现在被whl替代了
安装不需要本地编译，pypi很多包都是whl的格式

python中标准库的代码放在Lib中
第三方的放在site-packages下

源代码打包的方式：
sdist方式，相当于直接把源代码copy
执行python setup.py sdist
bdist方式，相当于编译成二进制打包，调用pip install安装即可
python setup.py bdist

pip freeze > requirements
pip install -r requirements

'''

from setuptools import setup

setup(
    name='m',
    version='0.1.1',
    author='hibiya',
    url='https://www.portuguel.com',
    packages=['m1', 'm1.m2'], # 打包只会打包和非子包的py文件
    py_modules=['t1'], # 加载外部的模块
    data_files=[('install', ['requirements'])], # 包含了requirements文件
    python_requires='>3.6'
)