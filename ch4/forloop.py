smoothies=['coconut', 'strawberry', 'banana', 'tropical', 'acai berry']
has_coconut=[True, False, False, True, False]

for i in range(len(has_coconut)):
  if has_coconut[i]:
    print(smoothies[i], 'contains coconut')