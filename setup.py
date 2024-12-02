from setuptools import setup, find_packages

setup(
    name='plane_detection',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy==1.24.4',
        'opencv-python==4.10.0.84',
        'pyrealsense2==2.55.1.6486',
        'open3d==0.18.0',
    ],
    entry_points={
        'console_scripts': [
            'plane_detection=plane_detection:main',
        ],
    },
    author='KazukiHigashi',
    description='A project for plane detection using OpenCV, Numpy, and RealSense',
    license="Apache 2.0",
)