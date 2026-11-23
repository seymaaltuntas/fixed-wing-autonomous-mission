import asyncio
import math
from mavsdk import System

telemetry_data = {
    "lat": 0.0,
    "lon": 0.0,
    "alt": 0.0,
    "speed": 0.0,
    "mode": "UNKNOWN"
}

async def track_position(drone):
    async for pos in drone.telemetry.position():
        telemetry_data["lat"] = pos.latitude_deg
        telemetry_data["lon"] = pos.longitude_deg
        telemetry_data["alt"] = pos.relative_altitude_m

async def track_velocity(drone):
    async for vel in drone.telemetry.velocity_ned():
        telemetry_data["speed"] = math.sqrt(vel.north_m_s**2 + vel.east_m_s**2)

async def track_flight_mode(drone):
    async for mode in drone.telemetry.flight_mode():
        telemetry_data["mode"] = str(mode)

async def print_telemetry():
    while True:
        print(
            f"[TELEMETRİ] Mod: {telemetry_data['mode']:<12} | "
            f"İrtifa: {telemetry_data['alt']:>6.1f} m | "
            f"Hız: {telemetry_data['speed']:>5.1f} m/s | "
            f"Konum: ({telemetry_data['lat']:.5f}, {telemetry_data['lon']:.5f})"
        )
        await asyncio.sleep(1)

async def run():
    drone = System()
    print("PX4'e bağlanılıyor (udp://:14540)...")
    await drone.connect(system_address="udp://:14540")

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Bağlantı başarılı!")
            break

    print("GPS ve sistem sağlığı kontrol ediliyor...")
    async for health in drone.telemetry.health():
        if health.is_global_position_ok and health.is_home_position_ok:
            print("Sistem uçuşa hazır!")
            break

    tasks = [
        asyncio.create_task(track_position(drone)),
        asyncio.create_task(track_velocity(drone)),
        asyncio.create_task(track_flight_mode(drone)),
        asyncio.create_task(print_telemetry()),
    ]

    print("İHA arm ediliyor...")
    await drone.action.arm()

    print("QGroundControl'den yüklenen mission başlatılıyor...")
    await drone.mission.start_mission()

    async for progress in drone.mission.mission_progress():
        print(f"--> Görev İlerlemesi: {progress.current}/{progress.total}")
        if progress.current == progress.total and progress.total > 0:
            print("Tüm waypoint'ler tamamlandı, iniş bekleniyor...")
            break

    async for in_air in drone.telemetry.in_air():
        if not in_air:
            print("İHA başarıyla iniş yaptı! Görev bitti.")
            break

    for task in tasks:
        task.cancel()

if __name__ == "__main__":
    asyncio.run(run())

