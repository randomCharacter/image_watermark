#!/bin/bash

pyinstaller --onefile --windowed --noconsole image_watermark.py
mkdir dist/watermark
mkdir dist/images
mkdir dist/out_images
zip image_watermark.zip dist/*