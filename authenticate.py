import pyotp
import qrcode


def authenticate (generated_code):
    
    '''generate qr code and compare user's input wih Google authenticator's token'''

    totp = pyotp.TOTP('base32secret3232')
    auth_str = totp.provisioning_uri(name ='KMS User', issuer_name='CS 555 Team 7')
    img = qrcode.make(auth_str)

    # qr code image to be scanned by user
    img.save('MyQRCode.png')

    if generated_code == totp.now():
        return True
    else:
        return False
