text = "X-DSPAM-Confidence:    0.8475"
d = text.find("0")
e = text.find("5")
g = text[23:e+1]
g = float(g)
print(g)
