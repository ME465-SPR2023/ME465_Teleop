from setuptools import setup
from glob import glob

package_name = 'ME465_Teleop'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name, glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Cameron Devine PhD',
    maintainer_email='cdevine@stmartin.edu',
    description='Example node for ME 465 in spring 2023 at Saint Martin\'s University',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'teleop_node = ME465_Teleop.teleop_node:main'
        ],
    },
)
