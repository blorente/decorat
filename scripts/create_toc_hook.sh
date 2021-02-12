#!/bin/bash
repo_root=$(git rev-parse --show-toplevel)
(
    cd $repo_root
    create_toc.sh
    git add _includes/toc.html
)