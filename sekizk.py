import os
import time
import cv2
import numpy as np

W, H = 7680, 4320                 # 8K (7680 x 4320)
KAYNAK = "resim_8k.bmp"
CIKTI = "resim_8k_yarim.bmp"

# 1) 8K, 3 kanallı (BGR) BMP oluştur (yoksa)
if not os.path.exists(KAYNAK):
    rng = np.random.default_rng(0)
    olusan = rng.integers(0, 256, size=(H, W, 3), dtype=np.uint8)
    cv2.imwrite(KAYNAK, olusan)
    print("8K resim oluşturuldu:", KAYNAK)

# 2) OpenCV ile aç
img = cv2.imread(KAYNAK, cv2.IMREAD_COLOR)
if img is None:
    raise FileNotFoundError(f"{KAYNAK} okunamadı")
print("Shape:", img.shape, "| dtype:", img.dtype)      # (4320, 7680, 3) uint8

# 3) Her piksel değerini 2'ye böl (SADECE bu kısım ölçülür)
t0 = time.perf_counter()
sonuc = img // 2                  # tamsayı bölme, uint8 kalır
t1 = time.perf_counter()

gecen = t1 - t0
print(f"\nİşlem süresi: {gecen:.6f} sn")
print(f"İşlem süresi: {gecen*1000:.3f} ms")
print(f"İşlem süresi: {gecen*1e9:.0f} ns")

# 4) BMP olarak kaydet
cv2.imwrite(CIKTI, sonuc)

# 5) Doğrulama
print("\nÖrnek piksel (önce):", img[0, 0], "-> (sonra):", sonuc[0, 0])
print("Çıktı dosya boyutu:", f"{os.path.getsize(CIKTI):,} bayt")
