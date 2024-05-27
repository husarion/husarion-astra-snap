build:
    #!/bin/bash
    export SNAPCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=1
    snapcraft

install:
    #!/bin/bash
    unsquashfs husarion-astra*.snap
    sudo snap try squashfs-root/
    sudo snap connect husarion-astra:raw-usb
    sudo husarion-astra.stop

remove:
    #!/bin/bash
    sudo snap remove husarion-astra
    sudo rm -rf squashfs-root/

clean:
    #!/bin/bash
    export SNAPCRAFT_ENABLE_EXPERIMENTAL_EXTENSIONS=1
    snapcraft clean   