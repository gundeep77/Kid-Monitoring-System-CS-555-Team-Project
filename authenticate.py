import pyotp
import qrcode


def authenticate (user_input):
    
    '''generate qr code and compare user's input wih Google authenticator's token'''

    totp = pyotp.TOTP('base32secret3232')
    auth_str = totp.provisioning_uri(name ='BabyMonitorUser', issuer_name='Team 7')
    img = qrcode.make(auth_str)

    # qr code image to be scanned by user
    img.save('MyQRCode1.png')

    if user_input == totp.now():
        print("Welcome")
    else:
        print("login failed")

