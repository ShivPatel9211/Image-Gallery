# from django.conf import settings
# media_root = settings.MEDIA_ROOT
from PIL import Image
import numpy as np

original_photo = R"E:\Python Project\Image Gallery\rotate.jpeg"
print(original_photo)
# with Image.open(original_photo) as image:
#     image.rotate(-90)
#     image.save("rotate-output.jpeg")
image = np.array(Image.open(original_photo))
image = Image.fromarray(np.rot90(image))
# image.rotate(-90)
image.save("rotate.jpeg")
# rotated_photo.show()