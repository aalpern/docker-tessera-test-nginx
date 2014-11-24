#!/bin/sh

docker run -d -P -e GRAPHITE_URL=http://graphite.prod.urbanairship.com --name test test
