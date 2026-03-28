# Hexapod ROS 2 Workspace
#
# Build:
#   docker build -t hexapod .
#
# Run (interactive shell with workspace sourced):
#   docker run -it --rm hexapod
#
# Run a specific node:
#   docker run -it --rm hexapod ros2 run hexapod_control gait_controller_node

FROM ros:jazzy

# Install build tools and common ROS dependencies
RUN apt-get update && apt-get install -y \
        python3-colcon-common-extensions \
        python3-rosdep \
        python3-pip \
        ros-jazzy-xacro \
        ros-jazzy-robot-state-publisher \
        ros-jazzy-joint-state-publisher \
    && rm -rf /var/lib/apt/lists/*

# Create the ROS 2 workspace
WORKDIR /ros2_ws

# Copy the workspace source packages
COPY hexapod_ws/src ./src

# Install package dependencies declared in package.xml files (if any packages exist)
RUN apt-get update \
    && rosdep update \
    && (rosdep install --from-paths src --ignore-src -r -y 2>/dev/null || true) \
    && rm -rf /var/lib/apt/lists/*

# Build the workspace (succeeds even when src/ is empty)
RUN . /opt/ros/jazzy/setup.bash \
    && colcon build --symlink-install \
    && rm -rf build/ log/

# Source both the ROS installation and the workspace overlay on login
RUN echo "source /opt/ros/jazzy/setup.bash" >> /root/.bashrc \
    && echo "[ -f /ros2_ws/install/setup.bash ] && source /ros2_ws/install/setup.bash" >> /root/.bashrc

# Copy and install the custom entrypoint
COPY docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["bash"]
