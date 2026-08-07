import qrcode

url =  input("Enter the URL:").strip()
file_path = "C:\\Users\\HANNAN AHMED\\Desktop\\STUDY MATERIAL\\Python-mini-projects\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

img = qr.make_image()
img.save(file_path)

print("QR code Generated.")