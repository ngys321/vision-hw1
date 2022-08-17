from uwimg import *
im = load_image("data/dog.jpg")
f = make_emboss_filter()
blur = convolve_image(im, f, 1)
#to overflow and underflow of pixel value, clamping is needed.
clamp_image(blur)
save_image(blur, "dog-emboss")
