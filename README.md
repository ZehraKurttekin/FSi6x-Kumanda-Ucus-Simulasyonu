# FSi6X Kumanda Uçuş Simülasyonu

Bu repo, Ubuntu 24.04 üzerinde ROS 2 Jazzy ve Gazebo içinde ArduPilot SITL çalıştırırken, fiziksel FS-i6X kumandayı kullanarak dronu manuel olarak uçurmak için hazırlanmıştır.

Bu proje sadece kumanda ile uçuş testi için tasarlanmıştır.

---

## 1) Gerekenler

### Yazılım

- Ubuntu 24.04
- ROS 2 Jazzy
- Gazebo Harmonic
- Colcon
- Git
- Python 3
- QGroundControl

### Donanım

- FS-i6X RC kumanda
- Bilgisayar
- USB kablo / gerekli adaptör

---

## 2) Kurulum adımları

### Adım 1: ROS 2 Jazzy kur

```bash
sudo apt update
sudo apt install -y curl gnupg lsb-release
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo gpg --dearmor -o /usr/share/keyrings/ros-archive-keyring.gpg

echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list

sudo apt update
sudo apt install -y ros-jazzy-desktop
```

Her terminal açılışında kullanmak için:

```bash
echo "source /opt/ros/jazzy/setup.bash" >> ~/.bashrc
source ~/.bashrc
```

Kontrol:

```bash
ros2 --version
```

### Adım 2: Gazebo Harmonic kur

```bash
sudo apt install -y ros-jazzy-ros-gz
```

Kontrol:

```bash
gz sim --versions
```

### Adım 3: Colcon ve araçları kur

```bash
sudo apt install -y python3-colcon-common-extensions python3-rosdep build-essential git
```

### Adım 4: Projeyi klonla

```bash
cd ~
git clone https://github.com/ZehraKurttekin/FSi6x-Kumanda-Ucus-Simulasyonu.git sancak_ws
cd ~/sancak_ws
```

### Adım 5: Derle

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

## 3) QGroundControl kurulumu

```bash
cd ~/Downloads
wget https://github.com/mavlink/qgroundcontrol/releases/download/v4.4.4/QGroundControl.AppImage
chmod +x QGroundControl.AppImage
./QGroundControl.AppImage
```

---

## 4) FS-i6X kumandayı bağlama ve kalibrasyon

### Adım 1: Kumandayı bilgisayara bağla

- FS-i6X kumandayı USB ile bağlayın.
- Kumandanın açık olduğundan emin olun.
- QGroundControl uygulamasını açın.

### Adım 2: Kanal kontrolü

QGroundControl menüsünden:

- Vehicle Setup
- Radio

sekmesine girin. Şu kanal değerleri görünmelidir:

- Roll
- Pitch
- Yaw
- Throttle
- Switch / mode tuşları

Eğer kanal gelmiyorsa:

- USB kablosunu kontrol edin
- Kumandanın açık olduğundan emin olun
- Farklı USB portunu deneyin

### Adım 3: Kalibrasyonu başlat

- Radio ekranında "Calibrate" veya benzeri butona basın.
- Tüm çubukları merkeze getirin.
- Her eksen için tam yönlere doğru hareket ettirin.

Örnek:

- Roll: sola ve sağa
- Pitch: ileri ve geri
- Yaw: sola ve sağa
- Throttle: aşağı ve yukarı

### Adım 4: Değerleri kontrol et

Kalibrasyon sırasında değerler şöyle olmalıdır:

- Minimum: yaklaşık 1000
- Orta: yaklaşık 1500
- Maksimum: yaklaşık 2000

Kumanda merkezdeyken:

- Roll ≈ 1500
- Pitch ≈ 1500
- Yaw ≈ 1500
- Throttle ≈ 1000 veya 1500 arası

### Adım 5: Kaydet

- "Save" veya "Apply" butonuna basın.
- Radio kalibrasyonu tamamlanana kadar bekleyin.

---

## 5) Gazebo simülasyonunu başlatma

Aşağıdaki komutla simülasyonu başlatın:

```bash
source /opt/ros/jazzy/setup.bash
source ~/sancak_ws/install/setup.bash
export PATH=$PATH:/home/$USER/sancak_ws/external/Micro-XRCE-DDS-Gen/scripts
cd ~/sancak_ws
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
```

Bu komut Gazebo içinde Iris modelini açar.

---

## 6) Manuel uçuş adımları

1. Gazebo simülasyonunu başlatın.
2. QGroundControl'ı açın.
3. Drone bağlantısını kontrol edin.
4. Kumanda ile arm edin.
5. Stabilize veya Manual moda geçin.
6. Throttle ile kalkış yapın.
7. Roll, pitch ve yaw ile kontrolü sağlayın.
8. Yavaşça iniş yapın.
9. Disarm edin.

---

## 7) Hızlı başlangıç

```bash
source /opt/ros/jazzy/setup.bash
source ~/sancak_ws/install/setup.bash
cd ~/sancak_ws
ros2 launch ardupilot_gz_bringup iris_runway.launch.py rviz:=false use_dds_agent:=false
```

---

## 8) Sorun giderme

### Gazebo başlatılmıyor

- ROS 2 yüklü mü?
- Gazebo Harmonic kurulmuş mu?
- `source install/setup.bash` yapıldı mı?

### RC kumanda tanınmıyor

- USB kablo doğru mu?
- Kumanda açık mı?
- QGroundControl radio ekranında kanal değerleri çıkıyor mu?

### ArduPilot bağlantısı yok

- Gazebo çalışıyor mu?
- Launch komutu doğru çalışıyor mu?
- QGroundControl içinde drone bağlantısı kuruldu mu?

---

## Not

Bu repo, Ubuntu üzerinde FS-i6X kumanda ile Gazebo simülasyonunda manuel uçuş testi için hazırlanmıştır. Başka amaç için değildir.
