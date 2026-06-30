from launch import LaunchDescription
from launch.actions import ExecuteProcess, LogInfo


def generate_launch_description():

    sitl = ExecuteProcess(
        cmd=[
            '/home/tunahan/sancak_ws/external/ardupilot/Tools/autotest/sim_vehicle.py',
            '-v',
            'ArduCopter',
            '-f',
            'gazebo-iris',
            '--console'
        ],
        output='screen'
    )

    return LaunchDescription([
        LogInfo(
            msg='SANCAK SITL Layer Baslatildi'
        ),
        sitl
    ])
