# FS-i6X Kumanda Uçuş Simülasyonu

Bu repo, Gazebo ortamında ArduPilot SITL çalıştırılırken FS-i6X tipi fiziksel kumanda ile dronu manuel olarak uçurmak için hazırlanmıştır.

Amaç:

- Gazebo üzerinde drone simülasyonu başlatmak
- FS-i6X kumandayı bilgisayara bağlamak
- QGroundControl ile radio kalibrasyonu yapmak
- Manuel uçuş testi gerçekleştirmek

Bu proje, yarışma, takım, otonom sürü görevi ya da geniş kapsamlı sistem mimarisi anlatımı ile değil; doğrudan fiziksel kumanda ile uçuş simülasyonu odaklıdır.

---

## Gerekenler

### Yazılım

- Ubuntu 24.04
- ROS2 Jazzy
- Gazebo Harmonic
- ArduPilot SITL
- QGroundControl
- colcon
- Git
- Python 3

### Donanım

- FS-i6X veya benzeri RC kumanda
- bilgisayar
- gerekli USB bağlantı / joystick adaptörü

---

## Klasör yapısı

```text
sancak_ws/
├── README.md
├── worlds/
├── models/
├── src/
│   ├── sancak_bringup/
│   ├── sancak_simulation/
│   ├── sancak_control/
│   ├── sancak_interfaces/
│   └── sancak_mission/
├── external/
├── build/
├── install/
├── log/
└── models_backup/
```

---

## Kurulum adımları

### 1) Ubuntu 24.04 kurulumu

```bash
lsb_release -a
```

### 2) ROS2 Jazzy kurulumu

```bash
sudo apt update
sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list

sudo apt update
sudo apt install -y ros-jazzy-desktop
```

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Kontrol:

```bash
ros2 --version
```

### 3) Gazebo Harmonic kurulumu

```bash
sudo apt install -y ros-jazzy-ros-gz
```

Kontrol:

```bash
gz sim --versions
```

### 4) colcon kurulumu

```bash
sudo apt install -y python3-colcon-common-extensions python3-rosdep build-essential
```

### 5) Projeyi klonlama

```bash
git clone https://github.com/R-Tunahan-Kayahan/20044342.git ~/sancak_ws
cd ~/sancak_ws
```

### 6) Derleme

```bash
source /opt/ros/jazzy/setup.bash
colcon build
source install/setup.bash
```

Eğer eksik bağımlılık varsa:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

---

## QGroundControl kurulumu

```bash
cd ~/Downloads
wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.4.4/QGroundControl.AppImage
chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
```

---

## Gazebo simülasyonunu başlatma

Aşağıdaki komut daha önce başarıyla kullanılan başlatma yöntemidir:

```bash
source /opt/ros/jazzy/setup.bash
source /home/$USER/sancak_ws/install/setup.bash
export PATH=$PATH:/home/$USER/sancak_ws/external/Micro-XRCE-DDS-Gen/scripts
cd /home/$USER/sancak_ws
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
```

Bu komut, Gazebo içinde Iris modelini başlatır. ArduPilot SITL ve Gazebo birlikte çalışır.

---

## FS-i6X kumandayı bağlama ve kalibrasyon

1. FS-i6X kumandayı bilgisayara bağlayın.
2. QGroundControl’ı açın.
3. Vehicle Setup > Radio bölümüne girin.
4. Tüm kanalları kalibre edin.
5. Roll, pitch, yaw ve throttle için doğru çalıştığını doğrulayın.

---

## Manuel uçuş adımları

1. Gazebo simülasyonunu başlatın.
2. QGroundControl’ı açın.
3. Drone bağlantısını kontrol edin.
4. RC kumandayla arm edin.
5. Stabilize veya Manual moda geçin.
6. Throttle ile kalkış yapın.
7. Uçuş sırasında roll/pitch/yaw kontrolünü manuel olarak kullanın.
8. İniş yapın ve disarm edin.

---

## Hızlı başlatma komutu

```bash
source /opt/ros/jazzy/setup.bash
source ~/sancak_ws/install/setup.bash
cd ~/sancak_ws
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
```

---

## Sorun giderme

### Gazebo çalışmıyor

- ROS2 ortamı yüklü mü?
- Gazebo Harmonic kurulu mu?
- `source install/setup.bash` yapıldı mı?

### RC kumanda çalışmıyor

- USB bağlantı doğru mu?
- QGroundControl radio kalibrasyonu yapıldı mı?
- Kanallar doğru tanınıyor mu?

### ArduPilot bağlantısı yok

- Gazebo başlatıldı mı?
- launch komutu doğru çalışıyor mu?
- QGroundControl’ta drone bağlantısı kuruldu mu?

---

## Son not

Bu repo, geniş bir takım projesi ya da yarışma dosyaları değildir. Bu çalışma doğrudan FS-i6X ile Gazebo’da manuel uçuş simülasyonu için hazırlanmıştır.

Gelecekte daha büyük bir sistem kurulacaksa, bu repo temel doğrulama ve kontrol ortamı olarak kullanılabilir.

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
