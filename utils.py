import re


def parse_fields(text):

    fields = {
        "product_name": "",
        "price_default": "",
        "price_card": "",
        "barcode": ""
    }

    # ищем цены
    prices = re.findall(r"\d+[.,]\d+", text)

    if len(prices) > 0:
        fields["price_default"] = prices[0]

    if len(prices) > 1:
        fields["price_card"] = prices[1]

    # ищем barcode
    barcode = re.findall(r"\d{13}", text)

    if barcode:
        fields["barcode"] = barcode[0]

    fields["product_name"] = text[:100]

    return fields