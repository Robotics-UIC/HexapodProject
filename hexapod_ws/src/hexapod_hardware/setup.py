from setuptools import find_packages, setup

package_name = "hexapod_hardware"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/config", ["config/hardware.yaml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="TODO",
    maintainer_email="todo@example.com",
    description="Hardware abstraction scaffolding for the hexapod project.",
    license="TODO",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "servo_driver_node = hexapod_hardware.servo_driver_node:main",
        ]
    },
)
