bits = int(input("nbits:"))

bytes = bits / 8
kbytes = bytes / 1024
mbytes = kbytes / 1024

print(mbytes, "Mbytes,", kbytes, "Kbytes", bytes, "bytes" )