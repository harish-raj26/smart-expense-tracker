from services.ocr_services import extract_text_from_receipt


image_path = input("Enter receipt image path: ")

texts = extract_text_from_receipt(image_path)

print("\n--- OCR RESULT ---")

for text in texts:
    print(text)