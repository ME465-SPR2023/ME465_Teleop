from launch_ros.actions import Node
from launch import LaunchDescription


def generate_launch_description():
    joy = Node(
        package="joy",
        executable="joy_node",
        name="joy",
    )
    teleop = Node(
        package="ME465_Teleop",
        executable="teleop_node",
        name="teleop",
    )
    return LaunchDescription([
        joy,
        teleop,
    ])
