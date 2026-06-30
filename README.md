# SANCAK - Sürü İHA Görev ve Kontrol Sistemi

## Proje Tanımı

SANCAK, ROS2 Jazzy, Gazebo Harmonic ve ArduPilot SITL altyapıları kullanılarak geliştirilen sürü İHA görev ve kontrol sistemidir.

Projenin amacı;

- Çoklu İHA simülasyonu
- QR tabanlı görev atama
- Otonom görev yönetimi
- Formasyon uçuşları
- Yer Kontrol İstasyonu (GCS)
- ROS2 tabanlı modüler mimari

oluşturmaktır.

---

# Kullanılan Teknolojiler

## Simülasyon

- Gazebo Harmonic 8.11
- ROS2 Jazzy
- ArduPilot SITL
- MAVLink

## Yazılım

- Python
- ROS2
- OpenCV
- Drone Mission Framework

## Planlanan Arayüz

- Electron
- React
- TypeScript

---

# Sistem Mimarisi

```text
+----------------------+
|      GCS UI          |
| (React / Electron)   |
+----------+-----------+
           |
           v
+----------------------+
|  Mission Layer       |
|  (QR Görevleri)      |
+----------+-----------+
           |
           v
+----------------------+
|  Control Layer       |
|  Drone Komutları     |
+----------+-----------+
           |
           v
+----------------------+
|      ROS2            |
+----------+-----------+
           |
           v
+----------------------+
|    ArduPilot SITL    |
+----------+-----------+
           |
           v
+----------------------+
|   Gazebo Harmonic    |
+----------------------+
```

---

# Workspace Yapısı

```text
sancak_ws
│
├── src
│   ├── sancak_bringup
│   ├── sancak_control
│   ├── sancak_interfaces
│   ├── sancak_mission
│   └── sancak_simulation
│
├── worlds
│   ├── sancak_world.sdf
│   └── test_world.sdf
│
├── models
│   ├── red_pad
│   ├── blue_pad
│   ├── qr_plaka_1
│   ├── qr_plaka_2
│   ├── qr_plaka_3
│   ├── qr_plaka_4
│   ├── qr_plaka_5
│   └── qr_plaka_6
│
└── external
    ├── ardupilot
    └── ardupilot_gz
```

---

# Kurulum

## 1. Ubuntu

Proje Ubuntu 24.04 üzerinde geliştirilmektedir.

Kontrol:

```bash
lsb_release -a
```

---

## 2. ROS2 Jazzy

ROS2 kurulumu:

```bash
sudo apt update
sudo apt install ros-jazzy-desktop -y
```

Terminal ortamı:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Kontrol:

```bash
ros2 --version
```

---

## 3. Gazebo Harmonic

Kurulum:

```bash
sudo apt install ros-jazzy-ros-gz -y
```

Kontrol:

```bash
gz sim --versions
```

Beklenen:

```text
8.11.0
```

---

## 4. Workspace Oluşturma

```bash
mkdir -p ~/sancak_ws/src
cd ~/sancak_ws
```

---

## 5. Workspace Derleme

```bash
cd ~/sancak_ws

colcon build

source install/setup.bash
```

---

# Gazebo Testi

Boş dünya açmak için:

```bash
gz sim empty.sdf
```

---

# SANCAK World

Mevcut dünya:

```text
worlds/sancak_world.sdf
```

İçerik:

- Ground Plane
- Red Pad
- Blue Pad
- 6 QR Görev Alanı

---

## Dünya Çalıştırma

```bash
gz sim ~/sancak_ws/worlds/sancak_world.sdf
```

veya

```bash
ros2 launch sancak_simulation simulation.launch.py
```

---

# ROS2 Paketleri

## sancak_simulation

Gazebo dünya yönetimi.

Launch:

```bash
ros2 launch sancak_simulation simulation.launch.py
```

---

## sancak_bringup

Sistem başlangıç katmanı.

Launch:

```bash
ros2 launch sancak_bringup full_system.launch.py
```

---

## sancak_control

Drone kontrol katmanı.

Planlanan görevler:

- Arm
- Disarm
- Takeoff
- RTL
- Formation

---

## sancak_mission

Görev yönetimi.

Planlanan:

- QR görev çözümleme
- Görev dağıtımı
- Formasyon komutları

---

## sancak_interfaces

ROS2 mesaj ve servisleri.

---

# ArduPilot Kurulumu

## Klonlama

```bash
cd ~/sancak_ws/external

git clone https://github.com/ArduPilot/ardupilot.git
```

---

## Alt Modüller

```bash
cd ~/sancak_ws/external/ardupilot

git submodule update --init --recursive
```

---

## SITL Derleme

```bash
./waf configure --board sitl

./waf copter
```

---

# ArduPilot GZ

Kurulum:

```bash
cd ~/sancak_ws/external

git clone https://github.com/ArduPilot/ardupilot_gz.git
```

Derleme:

```bash
cd ~/sancak_ws

colcon build \
  --packages-select \
  ardupilot_gz_application \
  ardupilot_gz_bringup \
  ardupilot_gz_description \
  ardupilot_gz_gazebo
```

---

# Micro XRCE DDS Gen

ArduPilot DDS desteği için kuruldu.

## Kurulum

```bash
git clone https://github.com/eProsima/Micro-XRCE-DDS-Gen.git

cd Micro-XRCE-DDS-Gen

./gradlew assemble
```

---

## Java

Java 17 kullanılmıştır.

Kontrol:

```bash
java -version
```

Beklenen:

```text
openjdk 17
```

---

# Şu Ana Kadar Tamamlananlar

## Altyapı

- [x] Ubuntu 24.04
- [x] ROS2 Jazzy
- [x] Gazebo Harmonic
- [x] Colcon Workspace

## Simülasyon

- [x] SANCAK World
- [x] QR Alanları
- [x] Red Pad
- [x] Blue Pad

## Yazılım Mimarisi

- [x] sancak_bringup
- [x] sancak_control
- [x] sancak_interfaces
- [x] sancak_mission
- [x] sancak_simulation

## GitHub

- [x] Repository oluşturuldu
- [x] İlk commit gönderildi

---

# Devam Eden Çalışmalar

## Aşama 1

ArduPilot ↔ Gazebo bağlantısı

Durum:

```text
LINK1 DOWN
```

Hedef:

```text
LINK1 OK
Heartbeat
```

---

## Aşama 2

3 Drone SITL

```text
drone1
drone2
drone3
```

---

## Aşama 3

MAVROS Entegrasyonu

```text
/drone1/mavros
/drone2/mavros
/drone3/mavros
```

---

## Aşama 4

QR Görev Sistemi

- QR Tespiti
- JSON Ayrıştırma
- Görev Üretimi

---

## Aşama 5

Formasyon Kontrolü

- Line
- Triangle
- Arrow
- Diamond

---

## Aşama 6

Yer Kontrol İstasyonu

- Harita
- Drone Durumu
- Görev Yönetimi
- Telemetri

---

# Hedef

Teknofest için;

- Çoklu İHA
- QR Tabanlı Görev Yönetimi
- Otonom Formasyon Uçuşu
- Yer Kontrol İstasyonu
- Simülasyon ve Gerçek Sistem Entegrasyonu

geliştirilmektedir.
