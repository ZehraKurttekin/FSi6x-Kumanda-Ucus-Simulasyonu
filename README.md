# FSi6X Kumanda Uçuş Simülasyonu

Bu repo, Ubuntu 24.04 üzerinde ROS 2 Jazzy ve Gazebo içinde ArduPilot SITL çalıştırırken, fiziksel FS-i6X kumandayı kullanarak dronu manuel olarak uçurmak için hazırlanmıştır.

Bu proje, yalnızca “kumanda ile uçuş testi” odaklıdır. Bu repoda amaç, otonom görev, takım çalışması, geniş sistem mimarisi ya da diğer geliştirme alanları değildir. Tek hedef: simülasyon ortamında gerçek RC kumanda ile manuel uçuş denemesi yapmaktır.

## Bu repo ne yapar?

- Gazebo içindeki drone simülasyonunu başlatır.
- ArduPilot SITL ile uçuş yazılımını çalıştırır.
- FS-i6X kumandayı bilgisayara bağlar.
- QGroundControl ile radio kalibrasyonu yapar.
- Manuel uçuş testi için gerekli ortamı hazırlar.

Bu repo, güvenli ve tekrar edilebilir bir manuel uçuş test ortamı sunar. Başka amaçlar için tasarlanmamıştır.

---

## Gerekli yazılım ve donanım

### Yazılım

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic
- ArduPilot SITL
- QGroundControl
- Git
- colcon
- Python 3

### Donanım

- FS-i6X veya benzeri RC kumanda
- Bilgisayar
- USB bağlantı / gerekli adaptör
- Kablo ve güç kaynağı

---

## Klasör yapısı

```text
sancak_ws/
├── README.md
├── worlds/
├── models/
├── terrain/
├── src/
│   ├── sancak_bringup/
│   ├── sancak_simulation/
│   ├── sancak_control/
│   ├── sancak_interfaces/
│   ├── sancak_mission/
│   ├── ardupilot_gazebo/
│   ├── ardupilot_gz/
│   └── SITL_Models/
├── external/
├── build/
├── install/
├── log/
├── models_backup/
├── mav.parm
├── set_sitl_params.py
├── worlds/
└── README.md
```

---

## Kurulum adımları

Aşağıdaki adımlar, Ubuntu kurulu ve sadece bir arkadaşının simülasyonda FS-i6X ile uçuş yapmasını amaçlayan kullanıcılar için yazılmıştır.

### 1) Ubuntu sürümünü kontrol et

```bash
lsb_release -a
```

Ubuntu 24.04 kullanman önerilir.

### 2) ROS 2 Jazzy kur

```bash
sudo apt update
sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list

sudo apt update
sudo apt install -y ros-jazzy-desktop
```

ROS 2 ortamını terminalde her açışta kullanmak için:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Kontrol et:

```bash
ros2 --version
```

### 3) Gazebo Harmonic kur

```bash
sudo apt install -y ros-jazzy-ros-gz
```

Kontrol et:

```bash
gz sim --versions
```

### 4) colcon ve gerekli araçları kur

```bash
sudo apt install -y python3-colcon-common-extensions python3-rosdep build-essential git
```

### 5) Projeyi klonla

```bash
git clone https://github.com/ZehraKurttekin/FSi6x-Kumanda-Ucus-Simulasyonu.git ~/sancak_ws
cd ~/sancak_ws
```

Eğer daha önce farklı bir remote varsa ve sen kendi GitHub hesabına yüklemek istiyorsan, aşağıdaki adım gerekli olabilir:

```bash
git remote -v
```

Eğer `origin` başkasına işaret ediyorsa:

```bash
git remote rename origin upstream
```

Sonra kendi GitHub repoya ekle:

```bash
git remote add origin https://github.com/ZehraKurttekin/FSi6x-Kumanda-Ucus-Simulasyonu.git
```

### 6) Derle

```bash
source /opt/ros/jazzy/setup.bash
cd ~/sancak_ws
colcon build --symlink-install
source install/setup.bash
```

Eksik bağımlılık varsa:

```bash
rosdep install --from-paths src --ignore-src -r -y
```

---

## QGroundControl kurulumu

QGroundControl, RC kumanda kalibrasyonu ve drone bağlantısı için kullanılır.

```bash
cd ~/Downloads
wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.4.4/QGroundControl.AppImage
chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
```

Uygulama açıldıktan sonra:

- QGroundControl'ı başlat
- "Vehicle Setup" bölümüne gir
- "Radio" sekmesine bak
- FS-i6X kumandayı PC'ye bağla
- RC'nin tanındığını doğrula

---

## FS-i6X kumandayı bağlama ve QGroundControl kalibrasyonu

Bu kısım, simülasyonda uçuş için en kritik adımdır.

### Adım 1: Kumandayı bağla

- FS-i6X kumandayı bilgisayara USB ile bağla.
- Kumandanın açık olduğundan emin ol.
- QGroundControl'ı aç.
- Sol menüde "Vehicle Setup" > "Radio" bölümüne gir.

### Adım 2: Kanal bilgilerini kontrol et

QGroundControl ekranında sensör ve kanal değerleri görünmelidir.

Kontrol edilecek alanlar:

- Roll
- Pitch
- Yaw
- Throttle
- Switch / mode tuşları
- Diğer kanallar

Eğer kanal görünmüyorsa:

- USB kablosunu kontrol et
- Kumanda açık mı kontrol et
- Sistem "joystick / radio" tanıması yapıyor mu kontrol et
- Farklı USB portu deneyin

### Adım 3: Radio kalibrasyonu başlat

- "Radio" ekranında "Calibrate" veya benzeri butona tıkla.
- Kumandanın tüm çubuklarını merkeze al.
- Sonra her eksen için tam yönlere doğru hareket et.

Örnek olarak:

- Roll: tam sola ve tam sağa
- Pitch: tam ileri ve tam geriye
- Throttle: tam aşağı ve tam yukarı
- Yaw: tam sola ve tam sağa

### Adım 4: Girdi değerlerini doğrula

Kalibrasyon sırasında her kanal için şu değerler beklenir:

- Minimum değer yaklaşık 1000
- Merkez değeri yaklaşık 1500
- Maksimum değer yaklaşık 2000

Bu değerler aralığı, uçuş kontrolü için gereklidir.

### Adım 5: Merkezleme ve boşluk kontrolü

Kumanda çubuklarını merkez konuma getirdiğinde:

- Roll = yaklaşık 1500
- Pitch = yaklaşık 1500
- Yaw = yaklaşık 1500
- Throttle = yaklaşık 1000 veya 1500 arası

Ayarları kaydetmeden önce kontrol et:

- Çubuklar dümdüz mi?
- Çubuklar merkezdeyken drone komut vermiyor mu?
- Tam hareketlerde değerler doğru aralığa ulaşıyor mu?

### Adım 6: Kalibrasyonu kaydet

- "Save" ya da "Apply" butonuna bas.
- Radio kalibrasyonunu tamamla.
- QGroundControl ekranında değerlerin sabitlenmesini bekle.

### Adım 7: Manuel uçuş için hazırlık

Kalibrasyon sonrası:

- ArduPilot bağlantısını kontrol et
- Gazebo simülasyonunu başlat
- QGroundControl içinde dronun bağlantısını doğrula
- Kumanda ile arm et
- Stabilize veya Manual moduna geç
- Kalkış ve uçuş testini yap

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

## Manuel uçuş adımları

1. Gazebo simülasyonunu başlat.
2. QGroundControl'ı aç.
3. Drone bağlantısını kontrol et.
4. RC kumandayla arm et.
5. Stabilize veya Manual moduna geç.
6. Throttle ile kalkış yap.
7. Roll, pitch ve yaw ile kontrolü elde tut.
8. Yavaşça iniş yap.
9. Disarm et.

---

## Hızlı başlatma komutu

```bash
source /opt/ros/jazzy/setup.bash
source ~/sancak_ws/install/setup.bash
cd ~/sancak_ws
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
```

---

## Tek tık çalıştırma notları

Ubuntu kurulu olan bir arkadaşın projeyi doğrudan çalıştırması için en kolay yöntem, aşağıdaki dosyayı kullanmaktır:

```bash
cd ~/sancak_ws
chmod +x quickstart.sh
./quickstart.sh
```

Bu betik şu işleri otomatik yapar:

- ROS 2 Jazzy ortamını yükler
- proje ortamını etkinleştirir
- gerekli `PATH` ayarını ekler
- Gazebo + ArduPilot simülasyonunu başlatır

Önce projeyi derlemek gerekir:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/sancak_ws
colcon build --symlink-install
source install/setup.bash
```

Derleme tamamlandıktan sonra tek tık çalıştırma komutunu kullanabilirsiniz:

```bash
cd ~/sancak_ws
./quickstart.sh
```

> Kumanda ve QGroundControl hazırsa, bu komutla Gazebo simülasyonu doğrudan açılacaktır.

---

## Sorun giderme

### Gazebo çalışmıyor

- ROS 2 ortamı yüklü mü?
- Gazebo Harmonic kurulu mu?
- `source install/setup.bash` yapıldı mı?
- `ros2 launch ...` komutu doğru mı?

### RC kumanda tanınmıyor

- USB kablo doğru bağlandı mı?
- Kumanda açık mı?
- QGroundControl radio ekranında kanal değerleri çıkıyor mu?
- Farklı USB portu deneyin.

### ArduPilot bağlantısı yok

- Gazebo başlatıldı mı?
- Launch komutu çalışıyor mu?
- QGroundControl içinde drone bağlantısı kuruldu mu?
- RC kalibrasyonu tamamlandı mı?

### Simülasyon çok yavaş veya açık kalmıyor

- Sistemde yeterli kaynak var mı?
- Gazebo kaynaklarını kontrol et
- Gereksiz terminal veya uygulama kapat

---

## Dünya çalıştırma

```bash
gz sim ~/sancak_ws/worlds/sancak_world.sdf
```

veya:

```bash
ros2 launch sancak_simulation simulation.launch.py
```

---

## ROS 2 paketleri

### sancak_simulation

Gazebo dünya yönetimi ve simülasyon ortamı başlatma için kullanılır.

```bash
ros2 launch sancak_simulation simulation.launch.py
```

---

## Contributors

- Zehra Kurttekin

---

## Not

Bu repo, profesyonel bir üretim sistemi değil; Ubuntu 24.04 üzerinde FS-i6X kumanda ile Gazebo simülasyonu için hızlı bir manuel uçuş test ortamıdır.

Amacı, daha büyük bir uçuş sistemine geçmek değil; yalnızca kumanda ile uçuş testinin yapılabilmesidir.

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
