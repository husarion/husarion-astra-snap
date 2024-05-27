#!/usr/bin/bash

log() {
    local message="$1"
    # Log the message with logger
    logger -t "${SNAP_NAME}" "launcher: $message"
}

log_and_echo() {
    local message="$1"
    # Log the message with logger
    logger -t "${SNAP_NAME}" "configure hook: $message"
    # Echo the message to standard error
    echo >&2 "$message"
}

# Iterate over the snap parameters and retrieve their value.
# If a value is set, it is forwarded to the launch file.
OPTIONS="\
 params-file \
 namespace \
 device-namespace \
"

LAUNCH_OPTIONS=""

for OPTION in ${OPTIONS}; do
  VALUE="$(snapctl get driver.${OPTION})"
  if [ -n "${VALUE}" ]; then
    OPTION_WITH_UNDERSCORE=$(echo ${OPTION} | tr - _)
    LAUNCH_OPTIONS+="${OPTION_WITH_UNDERSCORE}:=${VALUE} "
  fi
done

if [ "${LAUNCH_OPTIONS}" ]; then
  # watch the log with: "journalctl -t husarion-astra"
  log_and_echo "Running with options: ${LAUNCH_OPTIONS}"
fi

ros2 launch $SNAP/usr/bin/astra.launch.py ${LAUNCH_OPTIONS} ffmpeg_params_file:=$SNAP_COMMON/ffmpeg_params.yaml
