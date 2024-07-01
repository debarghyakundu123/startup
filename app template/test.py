import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO
from bs4 import BeautifulSoup

def search_image():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}&source=lnms&tbm=isch"
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content for image URLs
        soup = BeautifulSoup(response.text, 'html.parser')
        images = soup.find_all('img')[1:7]  # Get the first 6 images

        # Clear the previous images
        for widget in image_frame.winfo_children():
            widget.destroy()

        # Display the images
        for img in images:
            img_url = img['src']
            img_response = requests.get(img_url)
            img_data = img_response.content
            image = Image.open(BytesIO(img_data))
            image.thumbnail((1000, 1000))  # Resize for better display
            img_tk = ImageTk.PhotoImage(image)
            img_label = ttk.Label(image_frame, image=img_tk)
            img_label.image = img_tk
            img_label.pack(side='left', padx=10, pady=10)
    else:
        error_label.config(text="Failed to retrieve images")

# Create the GUI window
root = tk.Tk()
root.title("Image Search")
root.geometry("1200x800")  # Set the window size to medium

# Create and place the entry box
entry = ttk.Entry(root, width=50)
entry.pack(pady=20)

# Create and place the search button
search_button = ttk.Button(root, text="Search", command=search_image)
search_button.pack(pady=20)

# Create a frame to hold the images
image_frame = ttk.Frame(root)
image_frame.pack(pady=20)

# Create and place the error label
error_label = ttk.Label(root, text="")
error_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
