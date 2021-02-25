#!/bin/bash
root=$(git rev-parse --show-toplevel)
(
cd $root
git pull --ff-only origin master
nvim .
)
