import qrcode

# Data to encode
data = "https://www.linkedin.com/in/javiercuevas"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size of QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save to a file
img.save("linkedin_qr.png")
