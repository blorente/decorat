#!/bin/bash
repo_root=$(git rev-parse --show-toplevel)
(
    cd $repo_root
    ./scripts/create_tree.py wiki > _includes/toc.html
)