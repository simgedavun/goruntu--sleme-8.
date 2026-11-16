import cv2
import numpy as np

KAYNAK = "tenrengi.bmp"       # içinde insan olan renkli resim
RENK = (255, 0, 0)            # OpenCV BGR sırası: tam mavi (ten olmayan bölgeler)

img = cv2.imread(KAYNAK, cv2.IMREAD_COLOR)
if img is None:
    raise FileNotFoundError(f"{KAYNAK} okunamadı")

def ten_disini_boya(bgr, maske):
    """maske: ten pikselleri 255, diğerleri 0. Ten olmayanlar RENK ile boyanır."""
    sonuc = bgr.copy()
    sonuc[maske == 0] = RENK
    return sonuc

# ---------- 1) RGB uzayında ten tespiti (kural tabanlı) ----------
B, G, R = cv2.split(img.astype(np.int16))      # int16: çıkarmada taşma olmasın
en_buyuk = np.maximum(np.maximum(R, G), B)
en_kucuk = np.minimum(np.minimum(R, G), B)

maske_rgb = (
    (R > 95) & (G > 40) & (B > 20) &
    ((en_buyuk - en_kucuk) > 15) &
    (np.abs(R - G) > 15) &
    (R > G) & (R > B)
).astype(np.uint8) * 255
sonuc_rgb = ten_disini_boya(img, maske_rgb)

# ---------- 2) YCbCr uzayında ten tespiti ----------
ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)  # OpenCV sırası: Y, Cr, Cb
maske_ycbcr = cv2.inRange(ycrcb, (0, 133, 77), (255, 173, 127))
sonuc_ycbcr = ten_disini_boya(img, maske_ycbcr)

# ---------- 3) HSV uzayında ten tespiti ----------
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)      # H: 0-179
maske_hsv = cv2.inRange(hsv, (0, 48, 80), (20, 255, 255))
sonuc_hsv = ten_disini_boya(img, maske_hsv)

# ---------- Kaydet ----------
cv2.imwrite("ten_rgb.bmp", sonuc_rgb)
cv2.imwrite("ten_ycbcr.bmp", sonuc_ycbcr)
cv2.imwrite("ten_hsv.bmp", sonuc_hsv)

# ---------- Ten oranlarını yazdır ----------
toplam = img.shape[0] * img.shape[1]
for ad, m in [("RGB", maske_rgb), ("YCbCr", maske_ycbcr), ("HSV", maske_hsv)]:
    print(f"{ad:6s}: ten olarak bulunan piksel oranı = %{cv2.countNonZero(m) / toplam * 100:.1f}")

# ---------- Göster ----------
def kucult(x, genislik=400):
    oran = genislik / x.shape[1]
    return cv2.resize(x, (genislik, int(x.shape[0] * oran)))

cv2.imshow("Orijinal", kucult(img));          cv2.moveWindow("Orijinal", 0, 0)
cv2.imshow("RGB", kucult(sonuc_rgb));         cv2.moveWindow("RGB", 420, 0)
cv2.imshow("YCbCr", kucult(sonuc_ycbcr));     cv2.moveWindow("YCbCr", 840, 0)
cv2.imshow("HSV", kucult(sonuc_hsv));         cv2.moveWindow("HSV", 1260, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()