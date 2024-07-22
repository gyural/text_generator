import cloudinary
import cloudinary.uploader
import os
from dotenv import load_dotenv
from cloudinary import CloudinaryImage
import cloudinary.api
from getDatas.get_product_img import get_img_path

# Configuration
load_dotenv(verbose=True)
remix_api_key = os.getenv('')
cloudinary.config(
  cloud_name = "dhabktrg9",
  api_key = os.getenv('CLOUDINARY_API_KEY'),
  api_secret = os.getenv('CLOUDINARY_API_KEY_SECRET') ,
)

def uploadImage(img_path):

  # Upload the image and get its URL
  # ==============================

  # Upload the image.
  # Set the asset's public ID and allow overwriting the asset with new versions
  cloudinary.uploader.upload(f"{img_path}", unique_filename = False,
                             overwrite=True)

  # Build the URL for the image and save it in the variable 'srcURL'
  srcURL = CloudinaryImage("why").image(format='png', width=1024, height=1024)

  # Log the image URL to the console.
  # Copy this URL in a browser tab to generate the image on the fly.
  print("****2. Upload an image****\nDelivery URL: ", srcURL, "\n")


if __name__ == '__main__':
    paths = get_img_path()
    path2 = '/Users/imgyuseong/PycharmProjects/text_generator/datas/user-input-sample/removebg-preview.png'
    print(paths[0])
    uploadImage(img_path=path2)
