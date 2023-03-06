# 041
ticker = "btc_krw"
ticker = ticker.upper()
print(ticker)

# 042
ticker = "BTC_KRW"
ticker = ticker.lower()
print(ticker)

# 043
text = 'hello'
print(text.capitalize())

# 044
file_name = "filename.xlsx"
print(file_name.endswith('xlsx')) # bool

# 045
print(file_name.endswith(('xlsx','xls')))

# 046
print(file_name.startswith('file'))

# 047
a = "Hello World"
print(a.split())

# 48
ticker = "btc_krw"
print(ticker.split('_'))

# 49
ticker = "2023-03-06"
print(ticker.split('-'))

# 50
data = "039390     "
print(data.rstrip())
