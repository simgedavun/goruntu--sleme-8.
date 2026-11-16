
import os
import cv2
import numpy as np

KAYNAK = "resim.bmp"
GRI = "resim_gri.bmp"

# 0) Resim yoksa 1000x1000 renkli test resmi üret
if not os.path.exists(KAYNAK):
    x = np.linspace(0, 255, 1000, dtype=np.uint8)
    b = np.tile(x, (1000, 1))               # soldan sağa artan mavi
    g = np.tile(x[:, None], (1, 1000))      # yukarıdan aşağı artan yeşil
    r = 255 - b                             # kırmızı ters
    cv2.imwrite(KAYNAK, cv2.merge([b, g, r]))
    print("Test resmi oluşturuldu:", KAYNAK)

# 1) Renkli BMP'yi aç
img = cv2.imread(KAYNAK, cv2.IMREAD_COLOR)
if img is None:
    raise FileNotFoundError(f"{KAYNAK} okunamadı")
print("Renkli resim shape:", img.shape)     # (1000, 1000, 3)

# 2) Ekranda göster
cv2.imshow("Renkli (BGR)", img)

# 3) Gri tonluya dönüştür, göster, BMP olarak kaydet
gri = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print("Gri resim shape:", gri.shape)        # (1000, 1000)
cv2.imshow("Gri", gri)
cv2.imwrite(GRI, gri)

# 4) Diğer renk uzayları (ödevdeki araştırma kısmı için örnek)
uzaylar = {
    "HSV":   cv2.cvtColor(img, cv2.COLOR_BGR2HSV),
    "YCrCb": cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb),
    "Lab":   cv2.cvtColor(img, cv2.COLOR_BGR2Lab),
}
for ad, goruntu in uzaylar.items():
    cv2.imshow(ad, goruntu)

# 5) Disk boyutu karşılaştırması
b_renkli = os.path.getsize(KAYNAK)
b_gri = os.path.getsize(GRI)
h, w = img.shape[:2]

print("\n--- Disk Boyutu Karşılaştırması ---")
print(f"Çözünürlük      : {w} x {h} = {w*h:,} piksel")
print(f"Renkli (3 kanal): {b_renkli:,} bayt ({b_renkli/1024/1024:.2f} MB)")
print(f"Gri    (1 kanal): {b_gri:,} bayt ({b_gri/1024/1024:.2f} MB)")
print(f"Oran            : {b_renkli/b_gri:.2f} kat")
print(f"Teorik renkli   : {w*h*3:,} bayt + başlık")
print(f"Teorik gri      : {w*h*1:,} bayt + başlık + palet")

cv2.waitKey(0)
cv2.destroyAllWindows()