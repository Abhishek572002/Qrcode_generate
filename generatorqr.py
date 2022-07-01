import qrcode
import image

qr=qrcode.QRCode(
    version=18,
    box_size=3,
    border=2
)
data="https://www.youtube.com/playlist?list=PLDzeHZWIZsTryvtXdMr6rPh4IDexB5NIA"

qr.add_data(data)
qr.make(fit = True)
img=qr.make_image(fill="blue",back_color="pink")
img.save("c++_playlist.png")