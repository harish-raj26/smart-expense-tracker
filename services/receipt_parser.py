def extract_amount(texts):
    for index, text in enumerate(texts):
        if text.upper()=="TOTAL":
             if index + 1 < len(texts):
                 amount_text = texts[index + 1]
                 amount_text = amount_text.strip()
             
                 try:
                    amount = float(amount_text)
                 except ValueError:
                    continue
                 return amount 




texts = ["KFC", "Burger", "TOTAL", "450.00"]

amount = extract_amount(texts)

print("Amount:", amount)