import cv2
from imwatermark import WatermarkDecoder

bgr = cv2.imread('outputs/txt2img-samples/samples/00000.png')

decoder = WatermarkDecoder('bytes', 32)
watermark = decoder.decode(bgr, 'dwtDct')
print(watermark.decode('utf-8'))
