from pyzbar.pyzbar import decode


def read_qr(image):

    decoded = decode(image)

    data = {
        "qr_code_barcode": "",
        "price1_qr": "",
        "price2_qr": "",
        "action_price_qr": "",
        "action_code_qr": ""
    }

    if decoded:

        qr_text = decoded[0].data.decode("utf-8")

        data["qr_code_barcode"] = qr_text

    return data