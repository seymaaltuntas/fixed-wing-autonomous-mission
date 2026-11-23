# İHA TÜRLERİ:
## multirotor sınıfı: birden çok motorla çalışır.
Motorların bulunduğu konuma göre ve motor sayısına göre isimlendirilir.
### tricopter:
Y şeklindedir. 3 motoru vardır. FBV gibi sistemlerde kullanılır.
### quadcopter - hexacopter - octocopter
4,6,8 motoru vardır. motor sayısı etkiyi belirler.ne kadar ağır bir durumun havaya kalkabileceğini belirtir.
- quadcopter genel görevlerde kullanılır.
- hexacopter, octocopter'de çok ağır yükler kaldırılabilir.
* motor sayısı arttıkça bataryaya ihtiyaç artar. batarya ekledikçe de ağırlık artar. 

-> x8: birden fazla motor aynı kanada konulur.

+ dönen kanatlarda 1/2 oranında ağırlık olur. Yani 4 motorun havaya kaldırma kuvveti, dronun toplam ağırlığının 2 katı olur.

#### MULTİROTOR İHA NASIL ÇALIŞIR?
- LİFT KUVVETİ < WEİGHT -> DRONE SABİT KALIR.
- LİFT KUVVETİ == WEİGHT -> YERDEYSE KALKMAZ, HAVADA İSE SABİT KALIR BUNA HOWERİNG DENİR.

LİFT KUVVETİ > WEİGHT -> DRONE YÜKSELİR.

cg: ağırlık merkezi.

Bir motor bir pervaneyi döndürdüğünde, newton'un 3. yasası(etki - tepki) gereği pervane de motora zıt yönde bir tepki torku uygular.

Diyelim ki bir pervane saat yönünde (CW)dönüyor,
-> motor ve gövdeye saat yönünün tersine (CCW) bir tepki uygular.
Tek bir pervane olsa, drone gövdesi bu tepkiyle dönmeye başlardı. ama 4 motorlu (quadcopter) bir drone da bu torklar karşılıklı olarak iptal edilir.

** YAW PARAMETRESİ:  DRONE'NUN SAĞA VE SOLA DÖNMEYİ SAĞLAR.
** ROLL PARAMETRESİ: DRONUN YANAL EKSENDE SAĞA VE SOLA DÖNMESİNİ SAĞLAR
** PITCH PARAMETRESİ: DRONUN ÖNE VEYA ARKAYA HAREKET ETMESİNİ SAĞLAR.
-> örneğin motorun öne eğilmesi için öndeki motorların daha az çalışması gerekir.
-> roll de dronun sağa yatması için sağ taraftaki motorların daha az çalışması gerekir.

motorların takılış biçimi: [3 1]  
                           [2 4]
** sağ üst ve sol alttakiler saat yönünün tersine döner.
** sol üst ve sağ alttaki motorlar saat yönünde döner.
 Buradaki amaç torku sıfırlamaktır.

## sabit kanat : kanatların kaldırma kuvvetiyle çalışan ihalardır.
Burada istenen, daha uzun sürelerde/ uzak mesafelere uçuşu gerçekleştirebilmektir.
İniş ve kalkış için bir piste ihtiyaçları vardır.
Bir batarya tek kanata güç verir.

#### Titrator: 
kanatların üzerinde gövdeye gelecek şekilde 2 öne 1 arkaya titrator (döner pervane) yapılıyor, daha hafif.


#### SABİT KANATLI İHA NASIL ÇALIŞIR?
Fixed-wing (sabit kanat) İHA'larda kaldırma kuvveti nasıl oluşur?
1.Temel Prensip:
- Uçağın kanadı havayı ikiye böler.
- Bir kısmı kanadın üstünden, bir kısmı altından geçer.
- Kanadın üst yüzeyi bombelidir.(kavisli)
- Alt yüzey daha düzdür.
- Uçak ileri hareket ederken (motor itkiyle), hava üstten daha hızlı akar.


2. Bernoulli ve Newton Etkisi:
Bu iki fizik yasası birlikte çalışır.
* Bernoulli prensibi:
- Üstten akan hava hızlı olduğu için basıncı düşer.
- Alttaki hava daha yavaş  -> basıncı yükselir.
-> Basınç farkı oluşur -> kanat yukarı itilir.(LİFT)

* Newton'un 3. Yasası:
- Kanat, havayı aşağıya doğru yönlendirir.
-> Hava aşağı itilirse, tepki olarak kanat yukarı itilir.(etki - tepki prensibi.)


# İHA'NIN TEMEL BİLEŞENLERİ:
- Companion Computer (GÖREV İKSİRİ): linux işletim sistemi bulundurur, raspberry pi gibi cihazlardan oluşur. İÇERDİĞİ İŞLETİM SİSTEMİYLE BERABER KOD ÇALIŞTIRMA GÖREVİNİ SAĞLAR. (İHA'nın içinde emir verme görevleri.)

- Flight Controller: Amaç: ihaya komut verdiğimizde, bu komutu çıktıya dönüştürmektir.

- Ground Control Station: telemetry cihazına bağlandığımız yazılım/yerdir. Bununla iha üzerinde bulunan parametreleri de değiştirebiliriz. Görev tasarlayabiliriz yer istasyonundan...

- Telemetry System : iha ile yer istasyonu arasında bağlantı sağlar.(pc'miz bu sayede iha ya bağlanabilir.)

- Sensors : airsbiti özellikle sabit kanatlılarda kullanıyoruz.(yanal ilerlerkenki hızını verir.) GPS: ihanın konumunu verir. kamera: görüntü alır.

- çoğu sensör flight controller'a bağlıdır.



## MOTORLAR:

1. 4 HANELİ RAKAMLARIN ANLAMI: (ÖR: 2212, 2820)
 rakamları genellikle 2şerli gruplara ayırarak okuruz:
 İlk 2 rakam (genişlik): Statorun milimetre cinsnden çarpılır.
 Son 2 rakam(yükseklik): Statorun milimetre cinsinden yüksekliğidir.

2. KV DEĞERİ NEDİR?
 KV değeri, motorun verilen her 1 volt başına yüksüz(pervane takılı değilken) dakikada kaç devir (RPM) döneceğini ifade eder.

 KV seçerken dikkat etmemiz gerekenler:
 Yüksek KV(ör: 2300 - 3500KV): Motor çok hızlı döner ancak torku düşüktür. Buyüzden küçük pervanelerde kullanılır. Yarış droneları için idealdir.

 Düşük KV(ör: 300 - 900 KV): Motor daha yavaş döner ama torku çok yüksektir. Bu yüzden büyük pervaneleri rahatça çevirebilir, büyük dronelar için idealdir.

Sıcaklık İlişkisi: KV Neden Isı Üretir?
 Yüksek KV değerli bir motorun içindeki bakır sargılar daha kalındır ve sarım sayısı daha azdır. Bu durum direnci düşürür ancak motorun çok daha yüksek akım (amper) çekmesine neden olur.

 Yüksek KV ve Isı: Yüksek KV motorlar, aynı işi yapmak için daha fazla akım çeker. Isınma, akımın karesiyle doğru orantılıdır. Bu yüzden yüksek KV motorlar, özellikle zorlandıklarında veya büyük pervane takıldığında çok hızlı ısınırlar.

Verimlilikile İlişkisi: Enerji Nereye Gidiyor?
 Verimliklik, pilden çekilen enerjinin ne kadarının harekete(itiş gücüne), ne kadarının boşa(ısıya) gittiğidir.


DÜŞÜK KV = YÜKSEK VERİMLİLİK: 
 Düşük KV motorlar genellikle büyük pervaneleri yavaş ama güçlü bir şekilde çevirir. Büyük bir pervaneyi düşük devirde çevirmek, küçük bir pervaneyi çok yüksek devirde çevirmekten (aerodinamik olarak) daha verimlidir. Bu yüzden uzun süre havada kalması gereken dronelarda (endüstriyel/ tarım) hep düşük KV tercih edilir.

YÜKSEK KV = DÜŞÜK VERİMLİLİK: 
 Motor çok yüksek devirlere çıktığında sürtünme, hava direnci ve manyetik kayıplar artar. Enerjinin önemli bir kısmı iş yapmak yerine ısıya dönüşür. Yarış droneları yüksek KV kullanır çünkü verimlilikten ziyade anlık tepki ve maksimum sürat önemlidir.


- Farklı itki değerine sahip motorlar bulunur bunun sebebi farklı mıknatıs sayısına, boyutuna ve bobin sarım sayısına sahip olmalarıdır. Bize gerekli olan itki büyüklüğünü hesaplayarak motor modeline karar vermemiz gereklidir.  Her motora uygun genellikle en az 2 adet olacak şekilde pervane büyüklüğü vardır. Pervanenin büyümesi çekilecek akımı artırırken aynı zamanda itkide artış sağlar. 

! quadcopter için 4 motorun toplam itkisi drone ağırlığının 2 katı olması önerilir.

Motorun çekeceği max akım miktarına uygun esc(motor hızını belirler, manyetik alanı değiştirerek yapr bunu.) almak şarttır.

Esc'yi, Flight controller'a bağlarken power modül kullanılır veya direkt power modüle kablosu güç kontrol kartına lehimlenir.

### ESC'nin Tanımı ve Çlışma Prensibi:
 Elektronik Hız Kontrolcü(ESC), fırçasız motor sistemlerinin yönetim merkezidir. Teml görevi, bataryadan gelen doğru akımı(dc), motorun dönebilmesi için üç fazlı alternatif akıma(ac) dönüştürmektir.
 
 - Komütasyon: ESC, motorun içindeki mıknatısların konumunu saniyede binlerce kez takip eder. Doğru bobine doğru mikrosaniyede akım göndererek elektromanyetik itme ve çekme kuvveti oluşturur.

 - Hız Yönetimi: KOntrol ünitesinden gelen komutları alarak motorun devrini(RPM) ayarlar. Bu işlem günümüzde yüksek frekanslı sinyallerle(PWM,..) yapılır.

ESC Yazılımları(Firmware) ve Modern Standartlar: 
 ESC'nin içindeki işlemcinin motoru nasıl süreceğini belirleyen yazılımlar, sistemin verimliliğini ve uçuş karakteristiğini doğrudan belirler.

BLHeli_32:
 Günümüzün en gelişmiş, 32-bit işlemci mimarisine sahip kapalı kaynak yazılımıdır.Yüksek veri işleme kapasitesi, telemetri desteği ve düşük enerji kaybı sunar. Profesyonel ve yarış odaklı sistemlerin standartıdır. 
Bluejay(Açık Kaynak): 
 8-bit işlemcili (BLHeli_S tabanlı) ekonomik ESC'leri modernize etmek için geliştirilmiştir. "Bidirectional DShot" özelliği sayesinde motor devirverisini kontrol kartına ileterek, yazılımsal filtreleme(RPM Filter) yapılmasına olanak tanır.

### ESC Seçiminde Kritik Teknik Kriterler:
Amper Kapasitesi(Sürekli ve Burst):
 ESC, motorun tam yükte çekeceği akımdan en az %20-25 daha yüksek kapasiteli olmalıdır. "Burst" değeri, anlık (genelde 10 sn) dayanabileceği maks akımı ifade eder.

Giriş Voltajı(S Sayısı):
 ESC'nin devresi, kullanılan bataryanın voltajına dayanıklı olmalıdır.(Ör: 2S-4S veya 3S-6S gibi).

Protokol Desteği(DShot):
 Güncel sistemlerde veri iletim hızı ve hatasızlığı için DShot600 protokolünü destekleyen işlemciler tercih edilmelidir.

Mosfet kalitesi ve Soğutma:
 Yüksek güç gerektiren endüstriyel sistemlerde (P80 gibi), ESC üzerindeki soğutucu blokların (Heatsink) varlığı kritik önem taşır.

=========================================================================
=========================================================================

## Flight Controller:
Uçuş Kontrol cihazı.
entegre sensörlerden gelen veriler sayesinde EKF gibi yazılımlarla İHA anlık durumunu en doğru değerlendirirken buradan gelen verilerle PID controller'e input sağlayarak motorlara verilecek gücü belirler ve stabilite sağlanır.
 Stabilizasyon: Eğim, yalpa ve sapma kontrolü.
 Navigasyon: GPS ve manyetometre entegrasyonu 
 Motor Yönetimi: ESC'ler ile iletişim.(esc: elektronik hız kontrolcü)
 Güvenlik Protokolleri: Failsafe ve acil durum inişleri.

## sensörler:
Ataletsel ölçüm birimi:(IMU) (FC'nin içerisinde)
 İHA'nın ivmesini(ivmeölçer ile yerçekimi vektörünü kullanarak), dönüşünü(Jiroskop ile açısal hıza bakarak hızını) ve yönelimini ölçer. Denge ve stabilite için kritiktir.
 Genellikle FC içerisinde birden fazla bulunur ve bu verilerin füzyon ile birleştirilmesi ile daha doğru sonuç verir.

lidar: haritalama ve (kızılötesi ışınlarla)yere olan uzaklığımızı buluyor.

manyetometre: aracın manyetik alan yoğunluğunu ölçüp, jiroskop verisindeki "yaw"(sapma) eskenindeki sürüklenmeyi (drift) kompanse eder.

PID Kontrolü: 
 PID, drone'un dengesini sürekli koruyan matematiksel kontrol sistemidir. Bu ölçümle hedef açı arasındaki farkı hesaplar.
 P: anlık hataya tepki verir. ne kadar eğikse o kadar düzelt.
 I: zamanla biriken hatayı sıfırlar. uzun süre eğiksem düzeltmeye devam et.
 D: hata değişim hızını izler. çok hızlı eğiliyorsa yavaşla.


GPS - GNSS:
küresel navigasyon uydu sistemleri.çalışma prensibi Trilaterasyon.
Uydular ile alıcı(iha) arasındaki mesafeyi ölçerek çalışır. Uydular sinyal gönderir. iha üzerindeki alıcı,sinyalin gönderiliş zamanıyla alış zamanı arasındaki farkı hesaplayarak uyduya olan mesafeyi bulur.

GPS'nin İHA'daki rolü: navigasyon ve biraz da denge (konum sabitleme, otonom sabitleme ve eve dönüş kısımlarından oluşur.) sağlar. 

RTK: real time kinematic:
 GPS nin daha hassas versiyonu.
 bir referands istasyonu (base) ile drone üzerindeki rtk alıcısı(rover) arasında düzeltme verisi gönderilir.
 Haritalama, ölçüm, tarım, inşaat vs alanlarda milimetrik hesaplamalar için kullanılır.
fiziksel yer istasyonuna sahip olma zorunluluğu olmayanlara NTRIP veya ağ tabanlı rtk denir.

EKF - sensör füzyonu ve genişletilmiş kalman filtresi:
 ihalardaki hiçbir sensör, aracın konumunu ve yönelimini tek başına hatasız bir şekilde raporlayamaz.
 sensör füzyonu, farklı frekanslarda ve farklı hata karakteristiklerine sahip sensör verilerini istatistiksel yöntemlerle birleştirerek en olası durum tahminini üretme sürecine denir.
 - ımu ve gps deki ufak hatalardan dolayı bunu kullanırız.
 - genişletilmiş ekf: nonlinear drumlarda tahmin yapma için kullanılan matematiksel algoritmadır.
 - ekf'nin çözümlediği durumlar: jiroskop sapması kestirimi, ivme kontrolü, yükseklik füzyonu.

çoklu EKF mimarisi:
 2-3 ekf hattı bulunur genelde.
 EKF1: IMU1 ve GPS
 EKF2: IMU2 ve GPS
 Sistem Seçici: bu 2 ya da 3 hattı sürekli denetler. verilerde tutarsızlık varsa diğer sağlıklı şeride geçer.


## TELEMETRY:
iletişim haberleşmede kullanılır.
veri iletimi, performans izleme, şifreli haberleşme.
ihadan yer kontrol istasyonuna, hız- yükseklik- pil durumu.. , güvenli iletişimin sağlanması.

en yaygınları 433,868, 915MHz, 2.4GHz dir.
menzil: 1-40 km+
çıkış gücü:
 - daha yüksek güç = daha uzun mesafe, ama daha çok enerji harcaması
 - görüş alanı temizse 100mw => +- 300 - 400 metre
                       500 mw => +- 1km

uçuş kontrolcüsü uyumluluğu: ArduPlot, PX4 vs destekliyor mu?, QGround vs yazılımlarla uyumlu mu?

----------------------------------------------------------------

## GÖRÜNTÜ AKTARIM SİSTEMLERİ:

1. Analog Görüntü Aktarım Sistemleri
 Daha çok FPV(first person view) yarış dronelarında ve hobi amaçlı kullanımlarda tercih edilir.
 Görüntüyü radyo dalgaları üzerinden şifrelemeden, doğrudan iletir.
 Çalışma Mantığı: PAL veya NTSC formatındaki video sinyali, genellikle 5.8GHz frekansında yayınlanır.
 Avantajları: gecikmesi neredeyse sıfır, düşük maliyetli ve hafiftir.
 Dezavantajları: düşük görüntü çözünürlüğü
 Popüler Modellr:
  - TBS Unify Pro Serisi: yüksek çıkış gücü ve dayanıklılığıyla bilinir.
  - ImmersionRC Tramp HV: yarışçılar arasında standart haline gelmiştir.
  - Foxeer Reaper: uygun fiyatlı ve yüksek performanslı bir alternatif.

2. Dijital Görüntü Aktarım Sistemleri:
 Modern endüstriyel ve tüketici İHA'larında standart haline gelen sistemlerdir. Veriyi paketler halinde kodlayarak gönderir.
 Çalışma Mantığı: Görüntü önce sıkıştırılır.(H.264/H.265), ardından dijital olarak ileilir.
 Avantajları: yüksek çözünürlük, parazitsiz net görüntü, yüksek menzil.
 Dezavantajları: az da olsa gecikme, daha maliyetli.
 POpüler Modeller:
  - DJI O3Air Unit: piyasadaki en gelişmiş dijiytal sistemlerden biridir; 1080p/100fps görüntü iletirken aynı zamanda 4k kayıt yapabilir.
  - Walksnail Avatar: DJI'ya en büyük rakip. düşük gecikmeli gece görüş kabiliyeti var. 
  - HDZero: dijital olmasına rağmen analog gibi düşük gecikme sunan hibrit bir yapıdadır.


## Companion Computer: İHA'nın Beyni:(Görev Bilgisayarları)
İHA'nın karmaşık hesaplama ve otonom karar verme yeteneklerini sağlar. yüksek işlemci ve ram kapasiteleri vardır. Aynı zamanda daha minimal boyutları çıkmıştır.
En önemli özelliği: yer istasyonu gibi uzaklık kaynaklı gecikmeler dahil olmadan, işlediği verilerden gelen sonuçlara göre İHA ya anlık otonom komutlar verebilir.
 - görüntü işleme, görev planlama, veri analizi vs. yapabilir.

 jetson, raspberry pi bunlara örnektir.


## Yer Kontrol İstasyonu - Ground Control Station (Operasyonel Merkez):
İşlevleri:
 Görev planlama: önceden tanımlanmış rotalar ve ara noktalar.
 Canlı görüntü: İHA kameralarından gerçek zamanlı akış
 Uçuş Parametreleri: Yükseklik, hız ve yön kontrolü.
 Acil Durum Yönetimi: Failsafe ve manuel geçersiz kılma.
 Veri Kaydı: Uçuş günlükleri ve sensör verileri depolama.

==========================================================================

# Autopilot Yazılımının Temel İşlevleri:

1. Sensor Fusion & State Estimation:
 Drone'un nerede olduğunu, ne kadar hızlı hareket ettiğini, nasıl döndüğünü anlar.
 EKF2/ EKF3 ile IMU, GPS, barometre, manyetometre, lidar, airspeed, accelerometre gibi verileri birleştirerek drone'un POZİSYONUNU, YÖNÜNÜ ve HIZINI tahmin eder.

2. Flight Control:
 attitude -> Rate -> Motor
 PID ile yapılan kısım. Drone'un yönünü, hızını ve pozisyonunu istenilen değerlere göre ayarlar.
  - Cascaded control yapısı vardır:
   ör:
    sağa dön komutu gelir.
    PID kontrol döngüsü roll açısını belirler.
    Roll PID -> ESC'lerden Motorlara sinyal yollar.(yani sağ motoru yavaşlatır..)