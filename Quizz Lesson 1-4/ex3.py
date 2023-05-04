n = int(input("n:"))
num_positives = 0
num_negatives = 0

for i in range(n):
    x = int(input(f"value({i}):"))
    if x > 0:
        num_positives += 1
    elif x < 0:
        num_negatives += 1
        
total = num_positives + num_negatives
percent_positives = (num_positives / total) * 100 if total > 0 else 0
percent_negatives = (num_negatives / total) * 100 if total > 0 else 0
    
print(f"% positive values = {percent_positives:.1f}%")
print(f"% negative values = {percent_negatives:.1f}%")