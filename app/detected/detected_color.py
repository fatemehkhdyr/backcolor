import cv2                      # OpenCV bindings
import numpy as np
from collections import Counter
import urllib.request


class BackgroundColorDetector():
    def __init__(self, imageLoc):
        # self.img = cv2.imread(imageLoc, 1)
        self.img = cv2.imdecode(np.asarray(bytearray(urllib.request.urlopen(imageLoc).read()), dtype=np.uint8), -1)
        self.manual_count = {}
        self.w, self.h, self.channels = self.img.shape
        self.total_pixels = self.w*self.h

    def count(self):
        for y in range(0, self.h):
            for x in range(0, self.w):
                RGB = (self.img[x, y, 2], self.img[x, y, 1], self.img[x, y, 0])
                if RGB in self.manual_count:
                    self.manual_count[RGB] += 1
                else:
                    self.manual_count[RGB] = 1

    def twenty_most_common(self):
        self.count()
        self.number_counter = Counter(self.manual_count).most_common(20)

    def rgb_to_hex(self, rgb):
        return '%02x%02x%02x' % rgb

    def detect(self):
        self.twenty_most_common()
        self.percentage_of_first = (float(self.number_counter[0][1])/self.total_pixels)
        return "#"+str(self.rgb_to_hex(self.number_counter[0][0]))


# if __name__ == "__main__":
#     BackgroundColor = BackgroundColorDetector("https://picsum.photos/id/237/200/300")
#     print(BackgroundColor.detect())