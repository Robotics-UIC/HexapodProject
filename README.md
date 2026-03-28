# HexapodProject

A ROS 2 Jazzy workspace for a six-legged (hexapod) robot.

## Running with Docker

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) installed and running

### Build the image

```bash
docker build -t hexapod .
```

### Run an interactive shell

```bash
docker run -it --rm hexapod
```

The shell will have both the ROS 2 Jazzy installation and the hexapod workspace automatically sourced.

### Run a specific ROS 2 node

```bash
docker run -it --rm hexapod ros2 run <package_name> <node_name>
```

For example, once packages are added to `hexapod_ws/src/`:

```bash
docker run -it --rm hexapod ros2 run hexapod_control gait_controller_node
```

### Rebuild after adding packages

After adding new ROS 2 packages to `hexapod_ws/src/`, rebuild the image:

```bash
docker build -t hexapod .
```

## Workspace layout

```
hexapod_ws/
└── src/          # Place ROS 2 packages here
docker/
└── entrypoint.sh # Container entrypoint (sources ROS + workspace)
Dockerfile        # Docker build definition
.dockerignore     # Files excluded from the Docker build context
```