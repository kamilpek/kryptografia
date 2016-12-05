# python3 block.py
# Kamil Pek 231050
# 05.12.201

from PIL import Image

if __name__ == '__main__':
    img = Image.open("plain.bmp")
    pixels = img.load() # create the pixel map

    for i in range(img.size[0]):    # for every pixel:
        for j in range(img.size[1]):
            if (i != 0) & (j != 0):
                k = i - 1
                l = j - 1
                # print (k, l, "!=0")
            else:
                k = i
                l = j
                # print (k, l, "=0")
            pixa1 = (pixels[i,j][0])
            pixa2 = (pixels[i,j][1])
            pixa3 = (pixels[i,j][2])
            pixb1 = (pixels[k,l][0])
            pixb2 = (pixels[k,l][1])
            pixb3 = (pixels[k,l][2])
            pix1 = pixa1 ^ pixa1
            pix2 = pixa2 ^ pixa2
            pix3 = pixa3 ^ pixa3
            pixels[i,j] = (pix1, pix2, pix3) # set the colour accordingly
            # pixels[i,j] = (pixa1, pixa2, pixa3) # set the colour accordingly
            # pixels[i,j] = (pixb1, pixb2, pixb3) # set the colour accordingly
            pixels[i,j] = hash(pixels[i,j])

    img.show()
    img.save("example.bmp")
