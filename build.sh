#!/bin/sh

current_dir=$(dirname $0)

# Create base extension directory
base_dir="${current_dir}/dist/Equalize Sidebearings.roboFontExt"
mkdir -p "${base_dir}/lib"

# Copy Python files to extension lib directory
cp "${current_dir}"/*.py "${base_dir}/lib"

# Copy Info.plist into extension bundle
cp "${current_dir}"/info.plist "${base_dir}"
