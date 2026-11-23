# Teknik Rapor: Sabit Kanatlı İHA Otonom Görev ve Telemetri Sistemi

## Sistem Mimarisi ve Çalışma Mantığı
* **Haberleşme:** PX4 SITL ve Gazebo (`rc_cessna`) simülasyonu başlatıldıktan sonra QGroundControl **UDP 14550**, Python MAVSDK betiği (`mission.py`) ise port çakışmasını önlemek için **UDP 14540** portu üzerinden MAVLink protokolüyle bağlanır.
* **İniş Yapılandırması:** Gazebo `rc_cessna` modelinde mesafe sensörü bulunmadığından sabit kanatlı inişin iptal edilmemesi için PX4 üzerinde `FW_LND_USETER=0` parametresi yapılandırılmıştır.
* **Yazılım Akışı (`mission.py`):** `asyncio` tabanlı asenkron yapıyla konum, NED hız bileşenlerinden hesaplanan yer hızı ve uçuş modu saniyede bir terminale yazdırılırken; sağlık kontrolleri (`is_global_position_ok`, `is_home_position_ok`) tamamlandığında araç arm edilir ve QGroundControl'den yüklenen görev başlatılır.
