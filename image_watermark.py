import tkinter as tk
from tkinter import ttk
import glob
from image_manipulation import add_watermark

from position import Position

def get_watermarks():
	return [file for file in glob.glob("watermark/*.png")]

def get_position(value):
	return Position(value)

def convert_images(position, watermark):
	types = ("images/*.png", "images/*.jpg", "images/*.gif")
	images = []
	for type in types:
		images.extend(glob.glob(type))

	p = get_position(position)

	for image in images:
		out_image = 'out_images/' + image.split("/")[-1]

		add_watermark(image, p, watermark, out_image)

if __name__ == "__main__":
	# Create main window
	top = tk.Tk()
	top.title = "Image watermark"

	# Select watermark type
	label_position = tk.Label(text="Watermark position:")
	label_position.config(width=100)
	label_position.config(font=("Courier", 20))
	label_position.pack()

	listbox_position = ttk.Combobox(top, values=[position.value for position in Position])
	listbox_position.config(width=100)
	listbox_position.config(font=("Courier", 20))
	listbox_position.pack()

	# Select watermark image
	watermarks = get_watermarks()

	# Select watermark type
	label_watermark = tk.Label(text="Select watermark:")
	label_watermark.config(width=100)
	label_watermark.config(font=("Courier", 20))
	label_watermark.pack()

	listbox_watermark = ttk.Combobox(top, values=watermarks)
	listbox_watermark.config(width=100)
	listbox_watermark.config(font=("Courier", 20))
	listbox_watermark.pack()

	# Add button
	saveButton = tk.Button(top, text="Add watermark", command=(lambda: convert_images(listbox_position.get() ,listbox_watermark.get())))
	saveButton.config(width=50)
	saveButton.config(font=("Courier", 20))
	saveButton.pack()

	top.mainloop()
