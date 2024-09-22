text = "გამარჯობა, როგორ ხარ?"
vowels = "აეიოუ"
count = sum(1 for char in text if char in vowels)
print("ხმოვანების რაოდენობა:", count)
