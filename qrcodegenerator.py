# 1.) install library qrcode = pip instal qrcode
# 2.) install library image = pip install image
# 3.) code . untuk membuka viscode lewat terminal
# 4.) install phyton 3.12 di microsoft store yang eror di pip

import qrcode #import library yang akan dipakai
import image
qr = qrcode.QRCode(
    version = 15, # untuk versi qr codenya
    box_size = 10, #ukuran putih putihnya qr code
    border = 5, #untuk build qr ke cmd
)

data = "https://www.instagram.com/apskks22_/" #link

qr.add_data(data)
qr.make(fit= True)
image = qr.make_image(fill="black",back_color ="white")#setting warna qr code
image.save("link.png") #untuk build qr ke gambar png