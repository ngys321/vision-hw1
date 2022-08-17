from uwimg import *
im1 = load_image("data/ron.png")
im2 = load_image("data/dumbledore.png")
f = make_gaussian_filter(5)
ron_lfreq = convolve_image(im1, f, 1)
ron_hfreq = im1 - ron_lfreq

dumbledore_lfreq = convolve_image(im2, f, 1)

ronbledore = ron_hfreq + dumbledore_lfreq
clamp_image(ronbledore) # 합성 이미지에서 overflow 나 underflow 를 없애줌

save_image(ron_hfreq, "ron_high-frequency")
save_image(dumbledore_lfreq, "dumbledore_low-frequency")
save_image(ronbledore, "ronbledore")
