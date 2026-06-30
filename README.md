# SANCAK - Sürü İHA Görev ve Kontrol Sistemi

## Proje Hakkında

SANCAK, ROS2 Jazzy, Gazebo Harmonic ve ArduPilot altyapıları kullanılarak geliştirilen sürü İHA görev yönetim sistemidir.

Sistemin amacı;

* Çoklu İHA simülasyonu
* Görev tabanlı sürü koordinasyonu
* QR kod tabanlı görev dağıtımı
* Formasyon uçuşları
* Yer Kontrol İstasyonu (GCS)
* Otonom görev yönetimi

özelliklerini tek bir çatı altında toplamaktır.

---

## Kullanılan Teknolojiler

### Simülasyon

* Gazebo Harmonic 8.11
* ROS2 Jazzy
* ArduPilot SITL

### Yazılım

* Python
* ROS2 Nodes
* MAVROS
* OpenCV
* Drone Mission Framework

### Gelecek Arayüz

* Electron
* React
* TypeScript

---

## Workspace Yapısı

```bash
sancak_ws/
```

### Paketler

#### sancak_simulation

Gazebo dünya ve model yönetimi.

#### sancak_control

Drone kontrol katmanı.

#### sancak_mission

Görev yönetim katmanı.

#### sancak_interfaces

ROS2 mesaj ve servis tanımları.

#### sancak_bringup

Sistem başlatma katmanı.

---

## Kurulum

### ROS2 Jazzy

Ubuntu 24.04 üzerine ROS2 Jazzy kurulmalıdır.

```bash
sudo apt install ros-jazzy-desktop
```

### Gazebo Harmonic

```bash
sudo apt install ros-jazzy-ros-gz
```

Kontrol:

```bash
gz sim --versions
```

Beklenen çıktı:

```text
8.11.0
```

### ArduPilot

```bash
git clone https://github.com/ArduPilot/ardupilot.git
```

Bağımlılıklar:

```bash
Tools/environment_install/install-prereqs-ubuntu.sh -y
```

---

## Simülasyon Dünyası

Mevcut dünya:

```text
sancak_world.sdf
```

İçerik:

* Ground Plane
* Red Landing Pad
* Blue Landing Pad
* 6 QR Görev Paneli

---

## Tamamlanan Özellikler

* ROS2 Workspace oluşturuldu
* Gazebo Harmonic çalıştırıldı
* SANCAK World oluşturuldu
* QR paneller eklendi
* Görev bölgeleri oluşturuldu
* ArduPilot entegrasyon çalışmaları başlatıldı
* ardupilot_gz kurulumu tamamlandı

---

## Devam Eden Çalışmalar

* ArduPilot ↔ Gazebo bağlantısı
* Çoklu drone entegrasyonu
* MAVROS entegrasyonu
* QR görev sistemi
* Formasyon algoritmaları
* Yer Kontrol İstasyonu (GCS)

---

## Hedefler

### Faz 1

* Gazebo + ArduPilot entegrasyonu

### Faz 2

* 3 Drone sürü simülasyonu

### Faz 3

* QR görev sistemi

### Faz 4

* Formasyon uçuşları

### Faz 5

* GCS Arayüzü

### Faz 6

* Teknofest görev senaryoları
