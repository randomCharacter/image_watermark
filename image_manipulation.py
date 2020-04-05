from position import Position

from PIL import Image

def add_watermark(in_img, position, watermark, out_img):
	# Load images
	img = Image.open(in_img)
	watermark = Image.open(watermark)
	# Get size
	img_w, img_h = img.size
	w_w, w_h = watermark.size

	if (position == Position.BL):
		offset = (0, img_h - w_h)
		img.paste(watermark, offset, watermark)
	elif (position == Position.BR):
		offset = (img_w - w_w, img_h - w_h)
		img.paste(watermark, offset, watermark)
	elif (position == Position.TL):
		offset = (0, 0)
		img.paste(watermark, offset, watermark)
	elif (position == Position.TR):
		offset = (img_w - w_w, 0)
		img.paste(watermark, offset, watermark)
	else:
		for i in range(0, img_w, w_w):
			for j in range(0, img_h, w_h):
				offset = (i, j)
				img.paste(watermark, offset, watermark)

	img.save(out_img)