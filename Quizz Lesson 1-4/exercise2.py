nbits = int(input("nbits:"))

totalbytes = nbits // 8
totalkbytes = totalbytes // 1024
mbytes = totalkbytes // 1024

kbytes = totalkbytes - (mbytes*1024)
bytes = totalbytes - (kbytes*1024) - (mbytes*1024*1024)

print(f"nbits: {nbits}")
print(f"{mbytes:.0f} Mbytes, {kbytes:.0f} Kbytes, {bytes:.0f} bytes" )

