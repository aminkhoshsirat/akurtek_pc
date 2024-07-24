from django.http import HttpRequest
import ghasedakpack


def get_client_ip(request: HttpRequest):
    x_forward_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forward_for:
        ip = x_forward_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def send_otp(phone, message):
    sms = ghasedakpack.Ghasedak("4739b9aa5a91a5f7ce17b61ce6affc466f079f65e2b6919444cbd45df71e0253")
    sms.send({
        'message': message,
        'receptor': phone,
        'linenumber': 10008566
    })
