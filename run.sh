#!/bin/bash

if [[ "$1" = "run" ]]; then
	docker run -ti -v ${PWD}:/usr/src/app --rm --name test ultralytics/yolov5 /bin/bash
fi
