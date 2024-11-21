from setuptools import setup, find_packages

try:
    import rosbag
except ImportError:
    print("rosbag is not installed, please install it first.")
    exit(1)
    
setup(
    name="bag_filter",
    version="0.1.0",
    description="A tool for filtering ROS bag",
    author="jeremy xia",
    author_email="xhy279@gmail.com",
    url="https://github.com/xhy279/bag-fitler",
    packages=find_packages(),
    package_data={
        "bag_filter": ["config/*.yaml"],
    },
    include_package_data=True,  
    install_requires=[
        "pyyaml>=5.3.1"
    ],
    classifiers=[
        'Environment :: ROS',
    ]
)
