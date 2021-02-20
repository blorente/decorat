#!/bin/bash
set -x

mkdir output
INFILES=$(find wiki/stories/ -name '*.md' -type f | sort)

pandoc \
    --toc \
    --output=output/Stories_from_Decorat.pdf scripts/header.md ${INFILES}
