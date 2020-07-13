import qrcode
data="my name is hitansh"
filename="name.png"
img=qrcode.make(data)
img.save(filename)