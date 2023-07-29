#!/usr/bin/env bash
# Installation script for the wlog terminal utility

if [[ "$EUID" -ne 0 ]]; then
	echo "Please, run as root user"
	exit 1
fi

if [[ ! -f "./main.py" ]]; then
	echo "Worker Logger file missing"
	exit 1
fi

mkdir -p /usr/local/bin/

if ! cp -f ./main.py /usr/local/bin/wlog_v1; then
	echo "Failed to copy binary to dir in PATH"
	exit 1
fi

sudo chmod +x /usr/local/bin/wlog_v1

ln -sf /usr/local/bin/wlog_v1 /usr/local/bin/wlog
echo "Worker Logger installed successfully.
Run 'wlog' from anywhere for new or existing notes with auto timestamp :)"
