from launch import LaunchDescription
from launch.actions import LogInfo, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

from ament_index_python.packages import get_package_share_directory

import os


def generate_launch_description():

    gazebo_launch = os.path.join(
        get_package_share_directory('ros_gz_sim'),
        'launch',
        'gz_sim.launch.py'
    )

    world_file = '/home/tunahan/sancak_ws/worlds/sancak_world.sdf'

    return LaunchDescription([

        LogInfo(
            msg='SANCAK Simulation Layer Baslatildi'
        ),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                gazebo_launch
            ),
            launch_arguments={
                'gz_args': f'{world_file} -r'
            }.items()
        )

    ])
