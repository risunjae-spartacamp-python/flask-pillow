from PIL import Image

img = Image.open("images/cat.png")
frame = Image.open("images/frame.png")

resized_frame = frame.resize((img.width))

img.paste(frame, (0, 0), frame)

img.save("images/out.png")
img.show()
