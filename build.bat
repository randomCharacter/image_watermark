pyinstaller --onefile --windowed --noconsole image_watermark.py
if not exist dist\watermark mkdir dist\watermark
xcopy watermark\random.png dist\watermark
if not exist dist\images mkdir dist\images
xcopy images\.gitkeep dist\images\.gitkeep
if not exist dist\out_images mkdir dist\out_images
xcopy out_images\.gitkeep dist\out_images\.gitkeep
cd dist
powershell Compress-Archive .\* -DestinationPath image_watermark.zip
cd ..