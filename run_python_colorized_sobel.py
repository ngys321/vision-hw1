from uwimg import *
im = load_image("data/dog.jpg")
color_sobel = colorize_sobel(im)

save_image(color_sobel, "dog-colorized-sobel")
