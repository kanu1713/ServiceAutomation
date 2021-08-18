#!/bin/bash

set -e

cmd="$@"

>&2 echo "Welcome to python"
exec $cmd