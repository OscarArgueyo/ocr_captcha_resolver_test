import pytesseract
try:
    import Image
except ImportError:
    from PIL import Image


def resolve(path):
    try:
        return str(
            pytesseract.image_to_string(Image.open(path))
        ).strip()

    except Exception:
        return "ERROR"
