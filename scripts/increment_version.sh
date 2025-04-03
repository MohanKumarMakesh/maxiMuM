#!/bin/bash
# Increment the patch version (e.g., v1.0.0 -> v1.0.1)
VERSION_FILE="version.txt"
if [ ! -f "$VERSION_FILE" ]; then
    echo "v1.0.0" > $VERSION_FILE
fi

CURRENT_VERSION=$(cat $VERSION_FILE)
BASE_VERSION=$(echo $CURRENT_VERSION | cut -d. -f1,2)
PATCH_VERSION=$(echo $CURRENT_VERSION | cut -d. -f3)
NEW_PATCH_VERSION=$((PATCH_VERSION + 1))
NEW_VERSION="${BASE_VERSION}.${NEW_PATCH_VERSION}"

echo $NEW_VERSION > $VERSION_FILE
echo "New version: $NEW_VERSION"
export VERSION=$NEW_VERSION