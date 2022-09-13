text = "X-DSPAM-Confidence:    0.8475"
fN = text.find("0")
print(fN)
lN = text.find("5")
print(lN)
dN = text[fN : lN + 1]
print(float(dN))
