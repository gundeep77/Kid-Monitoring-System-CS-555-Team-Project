import pyotp
import qrcode


def authenticate (generated_code):
    """
    **Description**:
    
    Generate QR Code and compare user's input with Google Authenticator's token
    
    **Args**:

    `generated_code` *(string)*: Code generated from the app to check against

    **Returns**:
    
    True if passes, False otherwise
    """

    totp = pyotp.TOTP('base32secret3232')
    auth_str = totp.provisioning_uri(name ='KMS User', issuer_name='CS 555 Team 7')
    img = qrcode.make(auth_str)

    # qr code image to be scanned by user
    img.save('MyQRCode.png')

    if generated_code == totp.now():
        return True
    else:
        return False
