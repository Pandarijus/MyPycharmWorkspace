from autocorrect import Speller

sp = Speller(lang='en')

word = "Hello I was loking for a wife to fuk"
correct = sp(word)

print(word)
print(correct)



