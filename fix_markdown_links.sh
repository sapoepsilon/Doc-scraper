#!/bin/bash

# This script is used to fix the markdown links in the documentation folder and its subfolders. And removes .bak files
find ./documentation -type f -name "*.md" -exec sed -i '.bak' -e ':a' -e 'N' -e '$!ba' -e 's/\[\([^]]*\)\n\([^]]*\)\]/[\1\2]/g' {} +
find . -type f -name "*.md" -exec sh -c 'mv "$1" "${1%.md}.mdx"' _ {} \;
