from setuptools import find_packages, setup

package_name = "hexapod_sensors"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        ("share/ament_index/resource_index/packages", [f"resource/{package_name}"]),
        (f"share/{package_name}", ["package.xml"]),
        (f"share/{package_name}/config", ["config/sensors.yaml"]),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="TODO",
    maintainer_email="todo@example.com",
    description="Sensor scaffolding for the hexapod project.",
    license="TODO",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "imu_node = hexapod_sensors.imu_node:main",
            "camera_node = hexapod_sensors.camera_node:main",
            "state_estimator_node = hexapod_sensors.state_estimator_node:main",
        ]
    },
)
