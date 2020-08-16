#!/usr/bin/env bash


set -e

function check_input() {
    echo "\$\*: $*"
    echo "PWD: $PWD, 0: $0"

    if [[ -f "$0" ]] && [[ $0 =~ ^/.* ]]; then
        TOP=${0}
    else
        TOP=$PWD/$0
    fi
    echo "TOP1: $TOP, TOP2: ${TOP%/*}"
}

function main() {
    echo "main inlet"
    if [[ 1 ]]; then
      check_input $@
    else
      echo "1 is false."
    fi
}


main $@