import qrcode

# Data to encode
data = "https://javy-scratchspace.github.io/javy0119.github.io/"

# Generate QR code
qr = qrcode.QRCode(
    version=1,  # controls size of QR
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=2,
)
qr.add_data(data)
qr.make(fit=True)

# Create an image
img = qr.make_image(fill_color="black", back_color="white")

# Save to a file
img.save("JACC_website_qr.png")