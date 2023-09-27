from setuptools import setup

package_name = 'racing_image_collect'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nuo.wu',
    maintainer_email='nuo.wu@horizon.cc',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'racing_image_collect = racing_image_collect.racing_image_collect:main',
        ],
    },
)
