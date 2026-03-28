#!/bin/bash
# Docker entrypoint: source ROS and workspace, then run the requested command.
set -e

# Source the base ROS 2 installation
# shellcheck disable=SC1091
source /opt/ros/jazzy/setup.bash

# Source the workspace overlay if it has been built
if [ -f /ros2_ws/install/setup.bash ]; then
    # shellcheck disable=SC1091
    source /ros2_ws/install/setup.bash
fi

exec "$@"
