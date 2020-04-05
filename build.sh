#!/bin/bash

pyinstaller --onefile --windowed --noconsole image_watermark.py
mkdir dist/watermark
cp watermark/random.png dist/watermark
mkdir dist/images
mkdir dist/out_images
pushd dist
zip image_watermark.zip *
popd