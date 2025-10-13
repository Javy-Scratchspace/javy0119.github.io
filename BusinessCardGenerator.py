from PIL import Image, ImageDraw, ImageFont

# Create blank white image (business card size)
card = Image.new('RGB', (1000, 600), color='black')
draw = ImageDraw.Draw(card)
draw.rectangle([(50, 50), (950, 550)], fill='white')

# Load qr code
qr_code = Image.open("JACC_website_qr.png")

# Resize and paste image
qr_code.thumbnail((200, 200), Image.Resampling.LANCZOS)
card.paste(qr_code, (725, 325))

# Load a font (adjust the path or use default)
font_title = ImageFont.load_default(size=40)
font_text = ImageFont.load_default(size=25)

# Add your details
draw.text((60, 50), "Javier Arturo Cuevas Chabrier", fill="black", font=font_title)
draw.text((60, 100), "Mechanical Engineering and Computer Science | UCF", fill="black", font=font_text)
draw.text((60, 450), "Email: javier@example.com", fill="black", font=font_text)
draw.text((60, 500), "LinkedIn: linkedin.com/in/javiercuevas", fill="black", font=font_text)

# Save as PNG or PDF
card.save("business_card.png")
