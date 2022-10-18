import pandas as pd
import code128
from PIL import Image, ImageDraw, ImageFont

def generate_barcode(bc):
    return bc

def generate_name(name):
    return name

df = pd.read_excel("Template.xlsx")
df.dropna(how='all', inplace=True)

barcode_list = []
name_list = []
image_list = []
barcode_list = df['barcode'].apply(lambda x: generate_barcode(x))
name_list = df['name'].apply(lambda x: generate_name(x))

for i, bc in enumerate(barcode_list):
    barcode_image = code128.image(f"{bc}", height=100)

    # Create empty image for barcode + text
    top_bott_margin = 35
    l_r_margin = 10
    new_height = barcode_image.height + (2 * top_bott_margin)
    new_width = barcode_image.width + (2 * l_r_margin)
    new_image = Image.new( 'RGB', (new_width, new_height), (255, 255, 255))

    # put barcode on new image
    barcode_y = 42
    new_image.paste(barcode_image, (0, barcode_y))

    # object to draw text
    draw = ImageDraw.Draw(new_image)

    # Define custom text size and font
    h1_size = 24
    h2_size = 28
    h3_size = 12
    footer_size = 18

    h1_font = ImageFont.truetype("arial.ttf", h1_size)
    h2_font = ImageFont.truetype("arial.ttf", h2_size)
    h3_font = ImageFont.truetype("arial.ttf", h3_size)
    footer_font = ImageFont.truetype("arial.ttf", footer_size)

    # Define custom text
    company_name = 'CENTRAL DE ALUMINIOS DEL VALLE'
    product_type = f'{name_list[i]}'
    center_product_type = (barcode_image.width / 2) - len(product_type) * 5
    center_barcode_value = (barcode_image.width / 2) - len(f"{bc}") * 8

    # Draw text on picture
    draw.text( (l_r_margin, 0), company_name, fill=(0, 0, 0), font=h3_font)
    draw.text( (center_product_type, (20)), product_type, fill=(0, 0, 0), font=footer_font)
    draw.text( (center_barcode_value, (new_height - 30)), f"{bc}", fill=(0, 0, 0), font=h1_font)
    image_list.append(new_image)

image_list[0].save("BarcodeList.pdf", save_all=True, append_images=image_list)