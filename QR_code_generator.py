import qrcode

# Enter url of any website here.
input_URL = "https://www.youtube.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=20,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

# convert into image
img = qr.make_image(fill_color="blue", back_color="pink")
img.save("url_qrcode.png")

print(qr.data_list)
