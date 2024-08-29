import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageTk

global original_image, last_processed_image
original_image = None
last_processed_image = None

def open_image():
    global original_image
    file_path = filedialog.askopenfilename(
        title="Select an image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if file_path:
        try:
            original_image = Image.open(file_path)
            selected_file_label.config(text=f"Selected image: {file_path}")
            preview_image()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open image: {str(e)}")

def add_text_watermark():
    if 'original_image' not in globals():
        messagebox.showwarning("Warning", "Please select an image first.")
        return

    text = text_entry.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter watermark text.")
        return

    image_copy = original_image.copy()
    draw = ImageDraw.Draw(image_copy)
    
    # You may need to adjust the font path or use a different font
    font = ImageFont.truetype("arial.ttf", 36)
    
    # Get the bounding box of the text
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    position = (image_copy.width - text_width - 10, image_copy.height - text_height - 10)
    
    # Draw the text with a semi-transparent white color
    draw.text(position, text, font=font, fill=(255, 255, 255, 128))
    
    preview_image(image_copy)

def add_logo_watermark():
    global original_image, last_processed_image
    if 'original_image' not in globals() or original_image is None:
        messagebox.showwarning("Warning", "Please select an image first.")
        return

    logo_path = filedialog.askopenfilename(
        title="Select logo image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            image_copy = original_image.copy()
            
            # Resize logo to be 1/4 the width of the original image
            logo_width = image_copy.width // 4
            logo_height = int(logo.height * (logo_width / logo.width))
            logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
            
            position = (image_copy.width - logo_width - 10, image_copy.height - logo_height - 10)
            image_copy.paste(logo, position, logo)
            
            last_processed_image = image_copy
            preview_image(image_copy)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add logo: {str(e)}")

def preview_image(img=None):
    global last_processed_image
    if img is None:
        img = original_image
    last_processed_image = img.copy()  # Store a copy of the processed image
    img_copy = img.copy()
    img_copy.thumbnail((300, 300))  # Resize for preview
    photo = ImageTk.PhotoImage(img_copy)
    preview_label.config(image=photo)
    preview_label.image = photo

def save_image():
    global last_processed_image
    if last_processed_image is None:
        messagebox.showwarning("Warning", "No image to save.")
        return
    
    file_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
    )
    if file_path:
        try:
            last_processed_image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {str(e)}")

# Create the main window
root = tk.Tk()
root.title("Image Watermark App")

# Create and pack widgets
open_button = tk.Button(root, text="Open Image", command=open_image)
open_button.pack(pady=10)

selected_file_label = tk.Label(root, text="No image selected")
selected_file_label.pack()

text_entry = tk.Entry(root, width=30)
text_entry.pack(pady=5)

text_watermark_button = tk.Button(root, text="Add Text Watermark", command=add_text_watermark)
text_watermark_button.pack(pady=5)

logo_watermark_button = tk.Button(root, text="Add Logo Watermark", command=add_logo_watermark)
logo_watermark_button.pack(pady=5)

save_button = tk.Button(root, text="Save Image", command=save_image)
save_button.pack(pady=10)

preview_label = tk.Label(root)
preview_label.pack(pady=10)

root.mainloop()
