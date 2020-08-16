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


function check_awk() {
    echo "1st 2st 3st 4st"  > ss.log
    echo "1ss 2ss 3ss 4ss" >> ss.log
    #awk '{print $0 $2}' ss.log

    # way.1
    while read line;
    do
        echo "read info from file: ${line}"
        echo ${line} | tac -s " "
    done < ss.log
    # way.2
    #cat ss.log | ( while read line; do echo $line; done )

    word="show me"
    for((i=0; i<${#word}; i++))
    do 
        echo ${word:i:1}
    done
}


function check_grep() {
    grep -e "re1" -e "re2" file
    grep "main()" . -r --include *.{c,cpp} --exclude "README" --exclude-dir "ex-dir"
}


function main() {
    echo "main inlet"
    if [[ 1 ]]; then
      check_awk
    else
      check_input $@
    fi
}


main $@