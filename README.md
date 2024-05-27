# husarion-astra-snap

Snap for Orbbec Astra customized for Husarion robots

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

