from PIL import Image
import glob
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack

global Multiplier

global blur_devider

global keep_fraction

try:
    print('Set a multiplier for the logarithmic scale, the default value is: 2000')
    Multiplier = float(input('Multiplier :'))
except ValueError:
    Multiplier = 2000

try:
    print('Set a "blur divider" default value is: 10')
    blur_devider = float(input('blur divider: '))
except ValueError:
    blur_devider = 10

try:
    print('set a value for fractions to keep, default value is: 0.1')
    keep_fraction = float(input('fractions: '))
except ValueError:
    keep_fraction = 0.1

print('insert a file path to your folder to import all .png files')
print('Example: ')
print('C:/Users/Olofs/PycharmProjects/FysProjekt2')
filepath = input('File path: ')
filepath = filepath.replace(" \ ", "/")
#C:/Users/Demo/Nextcloud/Photos/com.agilitech.spycalcfree/Documents/undermap/com.agilitech.spycalcfree/Documents/test

def more(image):
    R, C, D = image.shape


def two(image):
    R, C = image.shape


image_list = []
for filename in glob.glob(filepath + "/*.png"):
    im = Image.open(filename).convert('RGB')  # Gör om alla filer till RGB filer ist för " RGBA " etc
    image_list.append(im)

    image = im
    image = np.asanyarray(
        image) / 255  # Turns image into a Numpy arry! <-- big love right here! samt delar upp färgskalorna
    try:
        two(image)

        R, C = image.shape
        print((R, C), image.dtype)
        rows, cols = image.shape
        crow, ccol = int(rows / 2), int(cols / 2)

        fft_image = np.fft.fftn(image)
        fft_shift = np.fft.fftshift(fft_image)
        magnitute_spectrum = Multiplier * np.log(np.abs(fft_shift))
        fft_shift[crow - R:crow + C, ccol - R:ccol + C] = 0

    except ValueError:
        more(image)
        R, C, D = image.shape
        print((R, C, D), image.dtype)
        rows, cols, depth = image.shape
        crow, ccol, ddepth = int(rows / 2), int(cols / 2), int(depth / 2)

        fft_image = np.fft.fftn(image)
        fft_shift = np.fft.fftshift(fft_image)
        magnitute_spectrum = Multiplier * np.log(np.abs(fft_shift))
        fft_shift[crow - R:crow + C, ccol - C:ccol + C, ddepth - D:ddepth + D] = 0

    plt.figure()
    plt.imshow(magnitute_spectrum)
    plt.colorbar()
    plt.title('Magnitude spectrum of FFT ')

    fft_invshift = np.fft.ifftshift(fft_shift)
    image_back = np.fft.ifftn(fft_invshift)
    image_back = np.abs(image_back)

    Copy = fft_image.copy()


    def More(Copy):
        R, C, D = Copy.shape
        Copy[int(R * keep_fraction):int(R * (1 - keep_fraction))] = 0
        Copy[:, int(C * keep_fraction):int(C * (1 - keep_fraction))] = 0
        Copy[:, :, int(D * keep_fraction):int(D * (1 - keep_fraction))] = 0


    def Two(Copy):
        R, C = Copy.shape
        Copy[int(R * keep_fraction):int(R * (1 - keep_fraction))] = 0
        Copy[:, int(C * keep_fraction):int(C * (1 - keep_fraction))] = 0

        try:
            Two(Copy)

        except ValueError:
            More(Copy)


    image_final = np.fft.ifftn(Copy).real

    plt.figure()
    plt.imshow(np.abs(image_final))
    plt.colorbar()
    plt.title('Original image')

    F = np.abs(R - C)
    if F <= 100:
        F = 100
        print(F)
    else:
        print(F)
    kernel_dim = F
    kernel = []
    for i in range(kernel_dim):
        kernel.append([1 / (kernel_dim ** 2) for i in range(kernel_dim)])
    kernel3 = [[0.0020 * F, 0.0020 * F, 0.0020 * F], [0.0015 * F, 0.0015 * F, 0.0015 * F],
               [0.001 * F, 0.001 * F, 0.001 * F]]

    # 1-D Gaussian
    t = np.linspace(-10, 10, 30)
    bump = np.exp(-0.1 * t ** 2)
    bump /= np.trapz(bump)  # Normalizes integral to 1

    kernel = bump[:, np.newaxis] * bump[np.newaxis, :]

    # Padded FT
    kernel_ft = fftpack.fft2(kernel3, shape=image.shape[:2], axes=(0, 1))

    # Convolve
    img_ft = fftpack.fft2(image, axes=(0, 1))

    blur_img_ft = kernel_ft[:, :, np.newaxis] * img_ft
    blur_img = fftpack.ifft2(blur_img_ft, axes=(0, 1)).real

    blur_img = np.clip(blur_img, 0, 1)

    plt.figure()
    plt.imshow(blur_img)
    plt.title('Blurred image')

    Adder = kernel3
    print(Adder)

    image_mult = np.abs((image_final + (1 - image) * blur_img / blur_devider)).real
    plt.figure()
    plt.imshow(image_mult)
    plt.colorbar()
    plt.title('Sharpened by convolution')

plt.show()
