import pyotp
import qrcode


def authenticate (user_input):
    
    '''generate qr code and compare user's input wih Google authenticator's token'''

    totp = pyotp.TOTP('base32secret3232')
    auth_str = totp.provisioning_uri(name ='KMS User', issuer_name='CS 555 Team 7')
    img = qrcode.make(auth_str)

    # qr code image to be scanned by user
    img.save('MyQRCode.png')

    if user_input == totp.now():
        return 1
    else:
        return 0