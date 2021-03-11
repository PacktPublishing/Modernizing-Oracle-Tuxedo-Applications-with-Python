import tuxedo as t

txn = {
    "AMOUNT": 12300,
    "CURRENCY": "USD",
    "MERCHANT_NAME": "PACKTPUB",
    "CARD_NETWORKS": [
        "VISA",
        "MASTERCARD",
        "AMEX",
    ],
}

print(t.Fboolev32(txn, "MERCHANT_NAME %% '^PACKT.*'"))
print(t.Fboolev32(txn, "MERCHANT_NAME !% '^PACKT.*'"))

if t.Fboolev32(txn, "CURRENCY == 'USD' && CARD_NETWORKS[?] == 'AMEX'"):
    print(t.Ffloatev32(txn, "AMOUNT * 0.82 / 100."), "EUR")
