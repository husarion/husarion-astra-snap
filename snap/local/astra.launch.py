from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch_ros.actions import Node, PushRosNamespace
from launch.substitutions import EnvironmentVariable, LaunchConfiguration


def launch_setup(context, *args, **kwargs):
    params_file = LaunchConfiguration("params_file").perform(context)
    ffmpeg_params_file = LaunchConfiguration("ffmpeg_params_file").perform(context)
    namespace = LaunchConfiguration("namespace").perform(context)
    device_namespace = LaunchConfiguration("device_namespace").perform(context)

    remapping = []
    if namespace:
        remapping.append(("/tf", f"/{namespace}/tf"))
        remapping.append(("/tf_static", f"/{namespace}/tf_static"))

    astra_node = Node(
        package="astra_camera",
        executable="astra_camera_node",
        name="camera",
        namespace=device_namespace,
        parameters=[
            {
                "camera_name": device_namespace,
                "camera_link_frame_id": device_namespace + "_link",
            },
            params_file,
            ffmpeg_params_file,
        ],
        remappings=remapping,
        output="screen",
    )

    # healthcheck_node = Node(
    #     package="healthcheck_pkg",
    #     executable="healthcheck_node",
    #     name="healthcheck_astra",
    #     namespace=device_namespace,
    #     output="screen",
    # )

    # return [PushRosNamespace(namespace), astra_node, healthcheck_node]
    return [PushRosNamespace(namespace), astra_node]

def generate_launch_description():
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "params_file",
                default_value="/var/snap/husarion-astra/common/astra_params.yaml",
                description="Full path to the Astra parameters file",
            ),
            DeclareLaunchArgument(
                "ffmpeg_params_file",
                default_value="/var/snap/husarion-astra/common/ffmpeg_params.yaml",
                description="Full path to the FFMPEG plugin parameters file",
            ),
            DeclareLaunchArgument(
                "namespace",
                default_value=EnvironmentVariable("namespace", default_value=""),
                description="Namespace which will appear in front of all topics (including /tf and /tf_static).",
            ),
            DeclareLaunchArgument(
                "device_namespace",
                default_value="camera",
                description="Sensor namespace that will appear after all topics and TF frames, used for distinguishing multiple cameras on the same robot.",
            ),
            OpaqueFunction(function=launch_setup),
        ]
    )