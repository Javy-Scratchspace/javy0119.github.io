from PIL import Image, ImageDraw, ImageFont

# Create blank white image (business card size)
card = Image.new('RGB', (1000, 600), color='white')
draw = ImageDraw.Draw(card)

# Load a font (adjust the path or use default)
font_title = ImageFont.truetype("arial.ttf", 60)
font_text = ImageFont.truetype("arial.ttf", 40)

# Add your details
draw.text((50, 50), "Javier Arturo Cuevas Chabrier", fill="black", font=font_title)
draw.text((50, 150), "Mechanical Engineering | UCF", fill="black", font=font_text)
draw.text((50, 250), "Email: javier@example.com", fill="black", font=font_text)
draw.text((50, 320), "LinkedIn: linkedin.com/in/javiercuevas", fill="black", font=font_text)

# Save as PNG or PDF
card.save("business_card.png")
