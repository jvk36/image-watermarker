import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageTk

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


# def add_text_watermark():
#     if 'original_image' not in globals():
#         messagebox.showwarning("Warning", "Please select an image first.")
#         return

#     text = text_entry.get()
#     if not text:
#         messagebox.showwarning("Warning", "Please enter watermark text.")
#         return

#     image_copy = original_image.copy()
#     draw = ImageDraw.Draw(image_copy)
    
#     # You may need to adjust the font path or use a different font
#     font = ImageFont.truetype("arial.ttf", 36)
    
#     # Get the bounding box of the text
#     bbox = draw.textbbox((0, 0), text, font=font)
#     text_width = bbox[2] - bbox[0]
#     text_height = bbox[3] - bbox[1]
    
#     position = (image_copy.width - text_width - 10, image_copy.height - text_height - 10)
    
#     # Draw the text with a semi-transparent white color
#     draw.text(position, text, font=font, fill=(255, 255, 255, 128))
    
#     preview_image(image_copy)

def add_text_watermark():
    global original_image, last_processed_image
    if original_image is None:
        messagebox.showwarning("Warning", "Please select an image first.")
        return

    text = text_entry.get()
    if not text:
        messagebox.showwarning("Warning", "Please enter watermark text.")
        return

    try:
        watermarked_image = create_subliminal_watermark(original_image, text, is_text=True)
        last_processed_image = watermarked_image
        preview_image(watermarked_image)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to add text watermark: {str(e)}")


# def add_logo_watermark():
#     global original_image, last_processed_image
#     if 'original_image' not in globals() or original_image is None:
#         messagebox.showwarning("Warning", "Please select an image first.")
#         return

#     logo_path = filedialog.askopenfilename(
#         title="Select logo image",
#         filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
#     )
#     if logo_path:
#         try:
#             logo = Image.open(logo_path).convert("RGBA")
#             image_copy = original_image.copy()
            
#             # Resize logo to be 1/4 the width of the original image
#             logo_width = image_copy.width // 4
#             logo_height = int(logo.height * (logo_width / logo.width))
#             logo = logo.resize((logo_width, logo_height), Image.Resampling.LANCZOS)
            
#             position = (image_copy.width - logo_width - 10, image_copy.height - logo_height - 10)
#             image_copy.paste(logo, position, logo)
            
#             last_processed_image = image_copy
#             preview_image(image_copy)
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to add logo: {str(e)}")

def add_logo_watermark():
    global original_image, last_processed_image
    if original_image is None:
        messagebox.showwarning("Warning", "Please select an image first.")
        return

    logo_path = filedialog.askopenfilename(
        title="Select logo image",
        filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
    )
    if logo_path:
        try:
            logo = Image.open(logo_path).convert("RGBA")
            watermarked_image = create_subliminal_watermark(original_image, logo, is_text=False)
            last_processed_image = watermarked_image
            preview_image(watermarked_image)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to add logo watermark: {str(e)}")


# def preview_image(img=None):
#     global last_processed_image
#     if img is None:
#         img = original_image
#     last_processed_image = img.copy()  # Store a copy of the processed image
#     img_copy = img.copy()
#     img_copy.thumbnail((300, 300))  # Resize for preview
#     photo = ImageTk.PhotoImage(img_copy)
#     preview_label.config(image=photo)
#     preview_label.image = photo

def preview_image(img=None):
    global last_processed_image
    if img is None:
        img = original_image
    last_processed_image = img.copy()  # Store a copy of the processed image
    img_copy = img.copy()
    img_copy.thumbnail((300, 300))  # Resize for preview
    if img_copy.mode == 'RGBA':
        img_copy = img_copy.convert('RGB')
    photo = ImageTk.PhotoImage(img_copy)
    preview_label.config(image=photo)
    preview_label.image = photo

# def save_image():
#     global last_processed_image
#     if last_processed_image is None:
#         messagebox.showwarning("Warning", "No image to save.")
#         return
    
#     file_path = filedialog.asksaveasfilename(
#         defaultextension=".png",
#         filetypes=[("PNG files", "*.png"), ("JPEG files", "*.jpg"), ("All files", "*.*")]
#     )
#     if file_path:
#         try:
#             last_processed_image.save(file_path)
#             messagebox.showinfo("Success", "Image saved successfully!")
#         except Exception as e:
#             messagebox.showerror("Error", f"Failed to save image: {str(e)}")

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
            if last_processed_image.mode == 'RGBA':
                rgb_image = Image.new('RGB', last_processed_image.size, (255, 255, 255))
                rgb_image.paste(last_processed_image, mask=last_processed_image.split()[3])
                rgb_image.save(file_path)
            else:
                last_processed_image.save(file_path)
            messagebox.showinfo("Success", "Image saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save image: {str(e)}")

# def create_subliminal_watermark(main_image, watermark, is_text=True):
#     # Create a new transparent image for the watermark
#     watermark_layer = Image.new('RGBA', main_image.size, (0, 0, 0, 0))
    
#     if is_text:
#         # Set up the font
#         font_size = int(main_image.width / 10)  # Adjust size as needed
#         font = ImageFont.truetype("arial.ttf", font_size)
        
#         # Create a draw object
#         draw = ImageDraw.Draw(watermark_layer)
        
#         # Calculate text size
#         bbox = draw.textbbox((0, 0), watermark, font=font)
#         text_width = bbox[2] - bbox[0]
#         text_height = bbox[3] - bbox[1]
        
#         # Calculate position (centered)
#         x = (main_image.width - text_width) / 2
#         y = (main_image.height - text_height) / 2
        
#         # Draw the text
#         draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 50))
#     else:
#         # Resize logo
#         aspect_ratio = watermark.width / watermark.height
#         new_width = int(main_image.width * 0.5)
#         new_height = int(new_width / aspect_ratio)
#         watermark = watermark.resize((new_width, new_height), Image.LANCZOS)
        
#         # Calculate position (centered)
#         x = (main_image.width - new_width) // 2
#         y = (main_image.height - new_height) // 2
        
#         # Paste the logo
#         watermark_layer.paste(watermark, (x, y), watermark)
    
#     # Rotate the watermark slightly for a diagonal effect
#     watermark_layer = watermark_layer.rotate(30, expand=1)
    
#     # Scale the watermark to be larger than the main image
#     scale = 1.5
#     watermark_layer = watermark_layer.resize((int(main_image.width * scale), int(main_image.height * scale)))
    
#     # Calculate position to center the oversized watermark
#     paste_x = (main_image.width - watermark_layer.width) // 2
#     paste_y = (main_image.height - watermark_layer.height) // 2
    
#     # Create a new image blending the main image and the watermark
#     result = Image.new('RGBA', main_image.size, (0, 0, 0, 0))
#     result.paste(main_image, (0, 0))
#     result.paste(watermark_layer, (paste_x, paste_y), watermark_layer)
    
#     # Adjust the brightness and contrast of the result
#     enhancer = ImageEnhance.Brightness(result)
#     result = enhancer.enhance(1.1)  # Slightly increase brightness
    
#     enhancer = ImageEnhance.Contrast(result)
#     result = enhancer.enhance(1.1)  # Slightly increase contrast
    
#     return result

# def create_subliminal_watermark(main_image, watermark, is_text=True):
#     # Convert main image to RGBA if it's not already
#     if main_image.mode != 'RGBA':
#         main_image = main_image.convert('RGBA')
    
#     # Create a new transparent image for the watermark
#     watermark_layer = Image.new('RGBA', main_image.size, (0, 0, 0, 0))
    
#     if is_text:
#         # Text watermark code (unchanged)
#         font_size = int(main_image.width / 10)
#         font = ImageFont.truetype("arial.ttf", font_size)
#         draw = ImageDraw.Draw(watermark_layer)
#         bbox = draw.textbbox((0, 0), watermark, font=font)
#         text_width = bbox[2] - bbox[0]
#         text_height = bbox[3] - bbox[1]
#         x = (main_image.width - text_width) / 2
#         y = (main_image.height - text_height) / 2
#         draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 50))
#     else:
#         # Image watermark
#         if watermark.mode != 'RGBA':
#             watermark = watermark.convert('RGBA')
        
#         # Resize logo
#         aspect_ratio = watermark.width / watermark.height
#         new_width = int(main_image.width * 0.5)
#         new_height = int(new_width / aspect_ratio)
#         watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
#         # Calculate position (centered)
#         x = (main_image.width - new_width) // 2
#         y = (main_image.height - new_height) // 2
        
#         # Paste the logo with reduced opacity
#         watermark = Image.blend(Image.new('RGBA', watermark.size, (0, 0, 0, 0)), watermark, 0.3)
#         watermark_layer.paste(watermark, (x, y), watermark)
    
#     # Rotate the watermark slightly for a diagonal effect
#     watermark_layer = watermark_layer.rotate(30, expand=1)
    
#     # Scale the watermark to be larger than the main image
#     scale = 1.5
#     new_size = (int(main_image.width * scale), int(main_image.height * scale))
#     watermark_layer = watermark_layer.resize(new_size, Image.Resampling.LANCZOS)
    
#     # Calculate position to center the oversized watermark
#     paste_x = (main_image.width - watermark_layer.width) // 2
#     paste_y = (main_image.height - watermark_layer.height) // 2
    
#     # Blend the watermark with the main image
#     result = Image.alpha_composite(main_image, Image.new('RGBA', main_image.size, (0, 0, 0, 0)))
#     result.paste(watermark_layer, (paste_x, paste_y), watermark_layer)
    
#     # Adjust the brightness and contrast of the result
#     enhancer = ImageEnhance.Brightness(result)
#     result = enhancer.enhance(1.1)  # Slightly increase brightness
    
#     enhancer = ImageEnhance.Contrast(result)
#     result = enhancer.enhance(1.1)  # Slightly increase contrast
    
#     return result

def create_subliminal_watermark(main_image, watermark, is_text=True):
    # Convert main image to RGBA if it's not already
    if main_image.mode != 'RGBA':
        main_image = main_image.convert('RGBA')
    
    # Create a new transparent image for the watermark
    watermark_layer = Image.new('RGBA', main_image.size, (0, 0, 0, 0))
    
    if is_text:
        # Text watermark code (unchanged)
        font_size = int(main_image.width / 10)
        font = ImageFont.truetype("arial.ttf", font_size)
        draw = ImageDraw.Draw(watermark_layer)
        bbox = draw.textbbox((0, 0), watermark, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        x = (main_image.width - text_width) / 2
        y = (main_image.height - text_height) / 2
        draw.text((x, y), watermark, font=font, fill=(255, 255, 255, 50))
    else:
        # Image watermark
        if watermark.mode != 'RGBA':
            watermark = watermark.convert('RGBA')
        
        # Resize logo
        aspect_ratio = watermark.width / watermark.height
        new_width = int(main_image.width * 0.8)  # Increased size
        new_height = int(new_width / aspect_ratio)
        watermark = watermark.resize((new_width, new_height), Image.Resampling.LANCZOS)
        
        # Calculate position (centered)
        x = (main_image.width - new_width) // 2
        y = (main_image.height - new_height) // 2
        
        # Adjust opacity of the logo
        watermark_with_opacity = Image.new('RGBA', watermark.size, (0, 0, 0, 0))
        for i in range(watermark.width):
            for j in range(watermark.height):
                r, g, b, a = watermark.getpixel((i, j))
                watermark_with_opacity.putpixel((i, j), (r, g, b, int(a * 0.3)))  # Adjust 0.3 for more/less opacity
        
        watermark_layer.paste(watermark_with_opacity, (x, y), watermark_with_opacity)
    
    # Rotate the watermark slightly for a diagonal effect
    watermark_layer = watermark_layer.rotate(30, expand=1)
    
    # Scale the watermark to be larger than the main image
    scale = 1.2  # Reduced scale
    new_size = (int(main_image.width * scale), int(main_image.height * scale))
    watermark_layer = watermark_layer.resize(new_size, Image.Resampling.LANCZOS)
    
    # Calculate position to center the oversized watermark
    paste_x = (main_image.width - watermark_layer.width) // 2
    paste_y = (main_image.height - watermark_layer.height) // 2
    
    # Blend the watermark with the main image
    result = Image.alpha_composite(main_image, Image.new('RGBA', main_image.size, (0, 0, 0, 0)))
    result.paste(watermark_layer, (paste_x, paste_y), watermark_layer)
    
    # Adjust the brightness and contrast of the result
    enhancer = ImageEnhance.Brightness(result)
    result = enhancer.enhance(1.05)  # Slightly increase brightness
    
    enhancer = ImageEnhance.Contrast(result)
    result = enhancer.enhance(1.05)  # Slightly increase contrast
    
    return result


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
