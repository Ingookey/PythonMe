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


function check_tr() {
    tr_list=(9.0.0HUUiEI\)D 9.0.0HUUiEI\)T 9.0.0HUUiEI\))
    for item in ${tr_list[*]}
    do
        result=$(echo ${item} | sed "s|^.*)||")
        echo "item: ${item}, result: ${result}"
    done
}

function main() {
    echo "main inlet"
    if [[ 1 ]]; then
      check_tr
    else
      check_input $@
    fi
}


main $@