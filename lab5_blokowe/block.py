from PIL import Image

img = Image.open("plain.bmp")

pixels = img.load() # create the pixel map

for i in range(img.size[0]):    # for every pixel:
    for j in range(img.size[1]):
        pix1 = ((pixels[i,j][0])+77)%255
        pix2 = ((pixels[i,j][1])+22)%255
        pix3 = ((pixels[i,j][2])+11)%255
        pixels[i,j] = (pix1, pix2, pix3) # set the colour accordingly

img.show()
img.save("example.bmp")
