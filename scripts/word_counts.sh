#!/bin/bash

function count() {
    file=$1
    filtered=$(cat $file | sed 's:^//.*$::' | sed 's:^ *- \*.*$::')
    words=$(echo $filtered | wc -w)
    echo "$file,$words"
}

where=$1
for file in $(find "${where}" -name "*.md" | sort); do
  count $file
done