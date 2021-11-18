import cv2

def enlarge(input_path):
    img = cv2.imread(input_path)
    scale_percent = 3 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)
    # resize image
    resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    cv2.imwrite(input_path, resized)


enlarge("right_arrow.png")