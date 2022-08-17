from uwimg import *
im = load_image("data/dog.jpg")
f = make_highpass_filter()
blur = convolve_image(im, f, 0)
save_image(blur, "dog-highpass-wo-clamp")
#to overflow and underflow of pixel value, clamping is needed.
clamp_image(blur)
save_image(blur, "dog-highpass")
