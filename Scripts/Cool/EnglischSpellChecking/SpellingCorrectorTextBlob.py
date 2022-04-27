from textblob import TextBlob
wrong ="I am loking for a wife to fuk"
right = TextBlob(wrong).correct()
print(wrong)
print(right)