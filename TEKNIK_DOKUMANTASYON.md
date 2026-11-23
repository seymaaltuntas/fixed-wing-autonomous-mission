# Teknik Dokümantasyon: PX4, Simülasyon ve Haberleşme Mimarisi

## 1. PX4, SITL ve Gazebo Nedir?
* **PX4:** İnsansız hava araçları için geliştirilmiş açık kaynaklı otopilot yazılımıdır. Sensör verilerini (EKF2/EKF3) işleyerek aracın dengesini, konumunu ve otonom görevlerini yönetir.
* **SITL (Software-In-The-Loop):** Fiziksel bir uçuş kartına ihtiyaç duymadan PX4 otopilot kodunun doğrudan bilgisayar üzerinde çalıştırılmasını sağlayan simülasyon yaklaşımıdır.
* **Gazebo:** Yerçekimi, aerodinamik kuvvetler ve sensör verilerini (IMU, GPS, barometre) gerçek zamanlı simüle ederek PX4 SITL'a sanal uçuş ortamı sunan 3B simülatördür.

## 2. QGroundControl Ne İşe Yarar?
İHA ile operatör arasındaki bağlantıyı sağlayan **Yer Kontrol İstasyonu (GCS)** yazılımıdır. Uçuş öncesi parametre ayarlarını yapmaya, harita üzerinde otonom uçuş rotası (Takeoff, Waypoint, Landing) çizip araca yüklemeye ve uçuş boyunca telemetri verilerini canlı takip etmeye yarar.

## 3. MAVLink ve MAVSDK Nedir?
* **MAVLink:** Otopilot, yer kontrol istasyonu ve görev bilgisayarı arasında düşük gecikmeli komut ve telemetri alışverişi sağlayan haberleşme protokolüdür.
* **MAVSDK:** Ham MAVLink paketleriyle uğraşmadan Python veya C++ üzerinden yüksek seviyeli komutlarla (`arm`, `start_mission` vb.) İHA'yı otonom kontrol etmeyi sağlayan yazılım geliştirme kütüphanesidir.

## 4. ROS 2 ve PX4 Nasıl Birlikte Çalışır?
PX4 düşük seviyeli gerçek zamanlı uçuş kontrolünü yürütürken; **ROS 2** görüntü işleme, engel algılama ve üst seviye rota planlama gibi görevleri üstlenir. İkisi arasındaki iletişim **uXRCE-DDS** köprüsü ile sağlanır; PX4'ün iç mesajlaşma yapısı (uORB) doğrudan ROS 2 topic'lerine dönüştürülerek gerçek zamanlı veri aktarımı yapılır.
