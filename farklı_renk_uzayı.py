import os
import cv2
import numpy as np

KAYNAK = "meyve.bmp"      # renkli RGB BMP

img = cv2.imread(KAYNAK, cv2.IMREAD_COLOR)    # OpenCV BGR okur
if img is None:
    raise FileNotFoundError(f"{KAYNAK} okunamadı")
print("Orijinal shape:", img.shape)

# --- HSV (hazır) ---
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)    # H: 0-179, S: 0-255, V: 0-255

# --- YUV (hazır) ---
yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

# --- CIE Lab (hazır) ---
lab = cv2.cvtColor(img, cv2.COLOR_BGR2Lab)

# --- HSI (OpenCV'de yok, formülle) ---
def bgr_to_hsi(bgr):
    bgr = bgr.astype(np.float64) / 255.0
    B, G, R = bgr[:, :, 0], bgr[:, :, 1], bgr[:, :, 2]
    eps = 1e-10

    I = (R + G + B) / 3.0                                        # Intensity
    S = 1.0 - (3.0 * np.minimum(np.minimum(R, G), B)) / (R + G + B + eps)

    pay = 0.5 * ((R - G) + (R - B))
    payda = np.sqrt((R - G) ** 2 + (R - B) * (G - B)) + eps
    teta = np.arccos(np.clip(pay / payda, -1.0, 1.0))
    H = np.where(B <= G, teta, 2 * np.pi - teta)                 # 0 - 2π

    # BMP olarak kaydetmek için 0-255 aralığına ölçekle
    H8 = (H / (2 * np.pi) * 255).astype(np.uint8)
    S8 = (S * 255).astype(np.uint8)
    I8 = (I * 255).astype(np.uint8)
    return cv2.merge([H8, S8, I8])

hsi = bgr_to_hsi(img)

# --- BMP olarak kaydet ---
cikti = {
    "meyve_hsv.bmp": hsv,
    "meyve_hsi.bmp": hsi,
    "meyve_yuv.bmp": yuv,
    "meyve_lab.bmp": lab,
}
for ad, goruntu in cikti.items():
    cv2.imwrite(ad, goruntu)
    print(f"{ad} kaydedildi | shape: {goruntu.shape} | boyut: {os.path.getsize(ad):,} bayt")

# --- Ekranda göster ---
cv2.imshow("Orijinal (BGR)", img);  cv2.moveWindow("Orijinal (BGR)", 0, 0)
cv2.imshow("HSV", hsv);             cv2.moveWindow("HSV", 300, 0)
cv2.imshow("HSI", hsi);             cv2.moveWindow("HSI", 600, 0)
cv2.imshow("YUV", yuv);             cv2.moveWindow("YUV", 900, 0)
cv2.imshow("Lab", lab);             cv2.moveWindow("Lab", 1200, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()