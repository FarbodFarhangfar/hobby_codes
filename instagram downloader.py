import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import os.path


import requests
from bs4 import BeautifulSoup

def download_profile_pic(username):
   url = f"https://www.instagram.com/{username}/"

   response = requests.get(url, verify=False)

   soup = BeautifulSoup(response.content, 'html.parser')

   meta_tag = soup.find('meta', attrs={'property': 'og:image'})

   profile_pic_url = meta_tag['content']

   file_name = f"{username}_profile_pic.jpg"

   pic_response = requests.get(profile_pic_url)

   save_address = os.path.join("E:\Python Files\pyton lesson\more project\downloaded_images", file_name)
   with open(save_address, 'wb') as f:
      f.write(pic_response.content)

   print(f"Profile picture for {username} downloaded successfully!")
   print(response.json())
   return save_address





def generate_image():
    # Get the text from the input box
    text = text_entry.get()

    try:
        saved_address = download_profile_pic(text)

        image = Image.open(saved_address)

        # Convert the PIL image to a PhotoImage object
        photo = ImageTk.PhotoImage(image)

        # Update the label to display the generated image
        image_label.config(image=photo)
        image_label.image = photo

        # Update the status label
        status_label.config(text='Image Downloaded successfully.')
    except:
        status_label.config(text='Image Could not be downloaded!')

# Create the main application window
root = tk.Tk()
root.title('Text to Image Generator')
root.geometry("500x500")

# Create and place widgets
text_entry = ttk.Entry(root, width=30)
text_entry.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

generate_button = ttk.Button(root, text='Download Image', command=generate_image)
generate_button.grid(row=0, column=2, padx=10, pady=10)

image_label = ttk.Label(root, text='Downloaded image will appear here.')
image_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

status_label = ttk.Label(root, text='')
status_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

# Start the GUI event loop
root.mainloop()
