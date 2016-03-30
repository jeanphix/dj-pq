from setuptools import setup, find_packages


setup(
    name='dj-pq',
    version='1.4.2',
    license='BSD License',
    author='jean-philippe serafin',
    url='https://github.com/jeanphix/dj-pq/',
    author_email='serafinjp@gmail.com',
    description='``pq`` wrapper for django',
    long_description=open('README.rst').read(),
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Internet',
        'Topic :: System :: Distributed Computing',
        'Topic :: System :: Systems Administration',
    ],
    install_requires=[
        'django',
        'pq==1.4',
    ],
)
