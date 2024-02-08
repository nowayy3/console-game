from PIL import Image

img1 = Image.open('loose.png')
img1 = img1.resize((500,500))
img1.save('loose1.png')