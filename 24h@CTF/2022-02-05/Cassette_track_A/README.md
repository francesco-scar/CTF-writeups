# 24h@CTF Cassette track A Writeup

## Category

Steganography

## Description

The challenge provides a [wav file](resources/secret.wav) containing a secret message (the flag) and the [original audio file](resources/original.wav)


## Writeup

The challenge is in the steganography category, so we can expect to find the flag in the spectrogram of the audio file:

`sox secret.wav -n spectrogram -o secret_low_resolution.png`

produces

![secret_low_resolution](resources/secret_low_resolution.png?raw=true)

where you can barely see some letters and digits mixed with the original spectrogram.

To properly read the flag we can subtract the image corresponding to the original file from the image corresponding to the secret file. The default resolution is too low to read the string, so we should increase the spectrogram resolution with `-X` (pixels/second) and `-Y` (y height in pixels) options.

```
sox secret.wav -n spectrogram -o secret.png -X 200 -Y 2050
sox original.wav -n spectrogram -o original.png -X 200 -Y 2050
```

and then subtract the images with the following [python script](resources/img_diff.py) that also converts the result in a black and white image to read easily the flag.

```py
from PIL import Image, ImageChops

im1 = Image.open(r"secret.png")
im2 = Image.open(r"original.png")

diff = ImageChops.difference(im1, im2)


thresh = 8
fn = lambda x : 255 if x > thresh else 0
r = diff.convert('L').point(fn, mode='1')
r.save('diff_b_w.png')

diff.save('diff.png')
```

The final result is the following and, with some patience and guessing, you can read the flag

![secret_low_resolution](resources/diff_b_w_crop.png?raw=true)


## Flag

`FLAG{W3lc0m3_t0_4ud10_St3G4n0gr4pHy}`

-----

If you find errors or you want to contribute to this writeup go to the [GitHub repository](https://github.com/francesco-scar/CTF-writeups/tree/main/24h%40CTF/2022-02-05/Cassette_track_A) or contact me [opening an issue](https://github.com/francesco-scar/CTF-writeups/issues).
