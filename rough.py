try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract as tess
tess.pytesseract.tesseract_cmd= r"tesseract"
# import tesseract
y="page.png"
x=tess.image_to_string(Image.open(y))
print(x)
