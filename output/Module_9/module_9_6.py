def all_variants(text):
  for i in range(len(text) + 1):
    for j in range(i):
        yield text[j:i]

a = all_variants("abc")
for i in a:
  print(i)
