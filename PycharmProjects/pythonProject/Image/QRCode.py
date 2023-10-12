import pyqrcode

s = "Atmecs Technologies Pvt Ltd"
url = pyqrcode.create(s)
url.svg("atmecs.svg", scale=8)
url.png("atmecs.png", scale=6)
