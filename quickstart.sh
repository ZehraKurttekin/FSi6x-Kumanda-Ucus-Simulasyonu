#!/usr/bin/env bash
set -e

ROS_SETUP="/opt/ros/jazzy/setup.bash"
WORKSPACE_DIR="$HOME/sancak_ws"
INSTALL_SETUP="$WORKSPACE_DIR/install/setup.bash"
DDS_PATH="$WORKSPACE_DIR/external/Micro-XRCE-DDS-Gen/scripts"

if [ ! -f "$ROS_SETUP" ]; then
  echo "ROS 2 Jazzy bulunamadı. Önce ROS 2 Jazzy kurulumunu yapın."
  exit 1
fi

if [ ! -d "$WORKSPACE_DIR" ]; then
  echo "Proje klasörü bulunamadı: $WORKSPACE_DIR"
  exit 1
fi

if [ ! -f "$INSTALL_SETUP" ]; then
  echo "Proje daha önce derlenmemiş görünüyor."
  echo "Aşağıdaki komutları çalıştırın:"
  echo "  source /opt/ros/jazzy/setup.bash"
  echo "  cd ~/sancak_ws"
  echo "  colcon build --symlink-install"
  echo "  source ~/sancak_ws/install/setup.bash"
  exit 1
fi

source "$ROS_SETUP"
source "$INSTALL_SETUP"
export PATH="$PATH:$DDS_PATH"

cd "$WORKSPACE_DIR"
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
