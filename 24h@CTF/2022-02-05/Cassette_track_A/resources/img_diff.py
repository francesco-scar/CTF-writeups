from PIL import Image, ImageChops

im1 = Image.open(r"secret.png")
im2 = Image.open(r"original.png")

diff = ImageChops.difference(im1, im2)


thresh = 8
fn = lambda x : 255 if x > thresh else 0
r = fiff.convert('L').point(fn, mode='1')
r.save('diff_b_w.png')

diff.save('diff.png') 
