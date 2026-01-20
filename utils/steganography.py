import cv2

def hide_char(image_path, char, output_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))

    binary_char = format(ord(char), '08b')

    flat = img.flatten()

    for i in range(8):
        flat[i] = (flat[i] & 254) | int(binary_char[i])

    stego = flat.reshape(img.shape)
    cv2.imwrite(output_path, stego)


def extract_char(image_path):
    img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    img = cv2.resize(img, (128, 128))

    flat = img.flatten()
    bits = "".join(str(flat[i] & 1) for i in range(8))
    return chr(int(bits, 2))
