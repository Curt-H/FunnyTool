import qrcode

if __name__ == '__main__':
    qr = qrcode.QRCode(
        # size 1~40, 1 is 21*21
        version=3,
        # L, M, Q, H
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        # QR pixels
        box_size=10,
        # Border's thickness, must bigger than 4
        border=4,
    )
    qr.add_data('Some data')
    # gen the qr code
    qr.make()

    # gen the img file object
    img = qr.make_image()
    img.save('1.png')
    print(img)