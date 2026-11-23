# Fixed-Wing Autonomous Mission with PX4 & MAVSDK

Bu proje, **PX4 SITL** ve **Gazebo** ortamında simüle edilen sabit kanatlı (`rc_cessna`) bir İHA'nın **QGroundControl** üzerinden planlanan rotasını **Python (MAVSDK)** ile otonom olarak uçmasını ve canlı telemetri verilerini izlemesini sağlar.

## Klasör İçeriği
* `mission.py`: Otonom görev başlatma ve canlı telemetri izleme kodu.
* `README.md`: Kurulum ve kullanım dokümantasyonu.
* `TEKNIK_RAPOR.md`: Proje mimarisi ve uygulama raporu.
* `TEKNIK_DOKUMANTASYON.md`: PX4, SITL, Gazebo, QGC, MAVLink, MAVSDK ve ROS 2 kavramsal dokümantasyonu.
* `flight_video.webm`: Simülasyon uçuş kaydı.
* `video_notlari.md`: Eğitim süreci çalışma notları.

## Kurulum ve Çalıştırma
1. Gerekli kütüphaneyi kurun: `pip install "mavsdk<4"`
2. Simülasyonu başlatın: `cd ~/PX4-Autopilot && make px4_sitl gz_rc_cessna` (PX4 konsolunda `param set FW_LND_USETER 0` ayarlayın).
3. QGroundControl **Plan** sekmesinden Takeoff, Waypoint ve Landing rotasını çizip **Upload** edin.
4. Kodu çalıştırın: `cd ~/fixed_wing_mission && python3 mission.py`
