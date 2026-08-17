import cv2
import easyocr


reader = easyocr.Reader(["en"])


def extract_text_from_receipt(image_path):

    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError("Could not open the receipt image.")

    # Increase image size
    image = cv2.resize(
        image,
        None,
        fx=2,
        fy=2,
        interpolation=cv2.INTER_CUBIC
    )

    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Improve contrast
    gray = cv2.equalizeHist(gray)

    # OCR
    results = reader.readtext(gray)

    extracted_text = []

    for result in results:
        text = result[1]
        extracted_text.append(text)

    return extracted_text