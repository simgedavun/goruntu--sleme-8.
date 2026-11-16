"""
ÖDEV 1 - Görüntü İşlemede Yaygın Renk Uzayları

1. RGB (Red-Green-Blue)
   Kırmızı, yeşil ve mavi kanallardan oluşan toplamsal bir uzaydır.
   Kamera sensörleri ve ekranlar bu uzayı kullanır.
   Avantajları:
     - Basit ve çok yaygındır.
     - Donanımla doğrudan uyumludur, dönüşüm gerektirmez.
   Dezavantajları:
     - Parlaklık ve renk bilgisi birbirine karışıktır.
     - Aydınlanma değişince üç kanal birlikte değişir.
     - Algısal olarak düzgün değildir, cihaza bağımlıdır.
   Tercih edildiği problemler:
     - Görüntü gösterimi, görüntü okuma/yazma, derin öğrenme girişleri
       ve genel amaçlı işlemler.

2. CMY / CMYK
   Camgöbeği, eflatun ve sarı kanallarından oluşan çıkarımsal bir uzaydır.
   K kanalı siyahtır.
   Avantajları:
     - Baskı süreçleriyle doğrudan uyumludur.
     - K kanalı mürekkep tasarrufu sağlar.
   Dezavantajları:
     - Yalnızca baskıya yöneliktir, cihaza bağımlıdır.
     - Ekran renklerinin tamamını temsil edemez.
   Tercih edildiği problemler:
     - Yazıcı, matbaa ve baskı öncesi renk yönetimi.

3. HSV / HSL / HSI
   Renk tonu (Hue), doygunluk (Saturation) ve parlaklık
   (Value / Lightness / Intensity) bileşenlerini ayırır.
   Avantajları:
     - İnsanın renk algısına yakın ve sezgiseldir.
     - Renk bilgisi parlaklıktan ayrıldığı için aydınlanma değişimlerine
       karşı kısmen dayanıklıdır.
   Dezavantajları:
     - H kanalı dairesel olduğundan 0 ile 360 derece arasında
       süreksizlik vardır.
     - Düşük doygunlukta ve çok karanlık bölgelerde H kararsızdır.
     - Algısal olarak tam düzgün değildir.
     - RGB'den dönüşüm doğrusal değildir.
   Tercih edildiği problemler:
     - Renge dayalı segmentasyon, nesne takibi (renk eşikleme),
       cilt tespiti, renk bazlı filtreleme ve renk düzenleme araçları.

4. YUV / YCbCr / YIQ
   Parlaklık (Y) ile renk farkı bileşenlerini (Cb, Cr) ayırır.
   Avantajları:
     - İnsan gözü parlaklığa renkten daha duyarlıdır. Bu yüzden renk
       kanalları örneklenerek azaltılabilir (4:2:0), bu da yüksek
       sıkıştırma sağlar.
     - Gri tonlamaya doğrudan erişim verir.
     - Cilt rengi Cb-Cr düzleminde belirli bir bölgede toplanır.
   Dezavantajları:
     - Algısal olarak düzgün değildir, cihaza bağımlıdır.
     - Standarda göre (BT.601, BT.709) katsayılar değişir.
   Tercih edildiği problemler:
     - JPEG ve MPEG gibi görüntü/video sıkıştırma, televizyon
       yayıncılığı, cilt tespiti ve yüz algılama.

5. CIE XYZ
   Görünür tüm renkleri kapsayan, cihazdan bağımsız temel standart uzaydır.
   Avantajları:
     - Cihazdan bağımsızdır.
     - Diğer uzaylar arasında dönüşüm için köprü görevi görür.
   Dezavantajları:
     - Algısal olarak düzgün değildir.
     - Değerleri sezgisel yorumlamak zordur.
   Tercih edildiği problemler:
     - Renk yönetimi, cihazlar arası renk dönüşümü ve renk bilimi
       araştırmaları.

6. CIE Lab (L*a*b*)
   L parlaklığı, a yeşil-kırmızı eksenini, b mavi-sarı eksenini temsil eder.
   Avantajları:
     - Algısal olarak düzgündür: iki renk arasındaki Öklid mesafesi (ΔE)
       gözün algıladığı farka yaklaşık eşittir.
     - Cihazdan bağımsızdır.
     - Parlaklık ve renk ayrıdır.
   Dezavantajları:
     - RGB -> XYZ -> Lab dönüşümü hesaplama açısından ağırdır.
     - Referans beyaz noktası gerekir.
     - Gerçek zamanlı uygulamalarda maliyetlidir.
   Tercih edildiği problemler:
     - Renk farkı ölçümü, renk tabanlı kümeleme ve segmentasyon,
       görüntü benzerliği, kalite kontrol ve renk düzeltme.

7. Gri tonlama (Grayscale)
   Tek kanallı bir uzaydır.
   Yaygın dönüşüm formülü: Y = 0.299*R + 0.587*G + 0.114*B
   Avantajları:
     - Veri boyutu 3 kat azalır.
     - Hesaplama hızlıdır ve algoritmalar basittir.
     - Renk bilgisinin gerekmediği işlemlerde yeterlidir.
   Dezavantajları:
     - Renk bilgisi kaybolur.
     - Farklı renkler aynı gri değere eşlenebilir ve ayırt edilemez hale gelir.
   Tercih edildiği problemler:
     - Kenar tespiti, histogram eşitleme, eşikleme, OCR, doku analizi,
       özellik çıkarımı (SIFT, HOG) ve tıbbi görüntüleme.
"""