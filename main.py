from fastapi import FastAPI
import qrcode
from io import BytesIO
from PIL import Image
from starlette.responses import StreamingResponse


app = FastAPI()


@app.get("/qr/")
async def qr_generate(param: str):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=5,
        border=1,
    )
    qr.add_data(param)
    qr.make(fit=True)

    # Crea una imagen QR
    img = qr.make_image(fill_color="black", back_color="white")
    img.thumbnail((350, 350), Image.LANCZOS)

    # Convierte la imagen a bytes
    img_bytes = BytesIO()
    img.save(img_bytes, format='PNG')
    img_bytes.seek(0)

    return StreamingResponse(img_bytes, media_type="image/png")
