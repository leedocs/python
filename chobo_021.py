# 021
letters = 'python'
print(letters[0], letters[2])

# 022
license_plate = "24가 2210"
print(license_plate[4:])
print(license_plate[-4:])

# 023
string = "홀짝홀짝홀짝"
print(string[::2])
print(string.replace('짝',''))

# 024
string = "PYTHON"
print(string[::-1])

# 025
phone_number = "010-1111-2222"
print(phone_number.replace('-',' '))

# 026
print(phone_number.replace('-',''))

# 027
url = "https://wikidocs.net"
print(url[url.find('.')+1:])
print(url.split('.')[-1])

# 028
lang = "python"
# lang[0] = "P"
# print(lang)
# 에러 : 문자열은 수정할 수 없음

# 029 
string = "abcdef2a254a32a"
print(string.replace('a','A'))

# 030
string = "abcd"
string.replace("b","B")
print(string);
