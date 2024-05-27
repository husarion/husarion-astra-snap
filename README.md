# husarion-astra-snap

Snap for Orbbec Astra customized for Husarion robots

## Apps

| app | description |
| - | - |
| `husarion-astra.start` | Start the `husarion-astra.daemon` service |
| `husarion-astra.stop` | Stop the `husarion-astra.daemon` service |
| `husarion-astra` | Start the application in the foreground (run in the current terminal). Remember to stop the daemon first |

## Setup FFMPEG

The default values for `ffmpeg-image-transport` are:

```bash
$ sudo snap get husarion-astra driver.ffmpeg-image-transport
Key                                     Value
driver.ffmpeg-image-transport.encoding  libx264
driver.ffmpeg-image-transport.preset    ultrafast
driver.ffmpeg-image-transport.tune      zerolatency
```

to check available options run:

```bash
ffmpeg -encoders
```

find the list of available presets by running

```bash
ffmpeg -h encoder=$SELECTED_ENCODER`
```

## Setup Astra Params

Default astra params are stored in the following file:

```bash
$ sudo snap get husarion-astra driver.params-file
/var/snap/husarion-astra/common/astra_params.yaml
```

The default `astra_params.yaml` file content:

```yaml
---
/**:
  ros__parameters:
    camera_name: camera
    depth_registration: false
    serial_number: ''
    device_num: 1
    vendor_id: '0x2bc5'
    product_id: ''
    enable_point_cloud: true
    enable_colored_point_cloud: true
    point_cloud_qos: default
    connection_delay: 100
    color_width: 640
    color_height: 480
    color_fps: 30
    enable_color: true
    flip_color: false
    color_qos: default
    color_camera_info_qos: default
    depth_width: 640
    depth_height: 480
    depth_fps: 30
    enable_depth: true
    flip_depth: false
    depth_qos: default
    depth_camera_info_qos: default
    ir_width: 640
    ir_height: 480
    ir_fps: 30
    enable_ir: true
    flip_ir: false
    ir_qos: default
    ir_camera_info_qos: default
    publish_tf: true
    tf_publish_rate: 10.0
    ir_info_url: ''
    color_info_url: ''
    color_depth_synchronization: false
    oni_log_level: verbose
    oni_log_to_console: false
    oni_log_to_file: false
    enable_d2c_viewer: false
    enable_publish_extrinsic: false
```

To set a new params create a copy of the `astra-params.yaml` file:

```bash
sudo cp \
/var/snap/husarion-astra/common/astra_params.yaml \
/var/snap/husarion-astra/common/astra_params2.yaml
```

Modify the content of the `astra-params2.yaml` file, eg:

```bash
sudo vim /var/snap/husarion-astra/common/astra_params2.yaml
```

And set the new path to the config file:

```bash
sudo snap set husarion-astra driver.params-file=/var/snap/husarion-astra/common/astra_params2.yaml
```