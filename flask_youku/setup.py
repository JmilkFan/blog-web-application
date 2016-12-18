from setuptools import setup, find_packages


setup(
    name='Flask-Youku',
    version='0.1',
    license='MIT',
    description='Flask extension to allow easy embedding of Youku videos',
    author='JmilkFan(Fan Guiju)',
    author_email='fangui_ju@163.com',
    install_requires=['Flask'],
    packages=find_packages()
)
