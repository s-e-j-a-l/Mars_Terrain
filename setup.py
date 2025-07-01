from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'martian_drone'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        
        # ✅ Corrected path for the launch file
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),

        # ✅ Ensure the world file is in the correct location
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),

        # ✅ Ensure the Python script is installed correctly
        (os.path.join('lib', package_name), glob(package_name + '/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros-gazebo',
    maintainer_email='ros-gazebo@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'drone_control = martian_drone.drone_control:main',  # ✅ Add entry point for drone_control.py
            'read_depth = martian_drone.read_depth:main',
            'keyboard_control = martian_terrain.keyboard_control:main',
            'play_world = martian_terrain.play_world:main',


        ],
    },
)
