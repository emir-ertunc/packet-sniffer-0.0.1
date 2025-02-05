# Packet Sniffer

Ağ paket analizi ve IDS projesi, Scapy ile geliştirilen bir Python uygulamasıdır. Proje, protokol analizi, anomali tespiti, saldırı tespiti kuralları, otomatik tepki mekanizmaları ve veritabanı entegrasyonu gibi aşamalardan oluşmaktadır. İngilizce versiyonuna [buradan](https://github.com/emir-ertunc/packet-sniffer/edit/main/README.md) ulaşabilirsiniz.

## Proje Hakkında

Bu proje, ağ güvenliğini artırmak için Python programlama dili ve Scapy kütüphanesi kullanarak geliştirilmiş bir Ağ Paket Analizörü ve Saldırı Tespit Sistemi (IDS) uygulamasıdır. Bu sistem, ağ üzerinden geçen paketleri analiz eder, anormal davranışları tespit eder ve potansiyel saldırıları loglayarak yöneticilere bildirir.

## İçindekiler

- [Kurulum Talimatları](#kurulum-talimatları)
- [Kullanım](#kullanım)
- [Proje Özellikleri](#proje-özellikleri)
- [Geliştirme Süreci](#geliştirme-süreci)
- [Katkıda Bulunma](#katkıda-bulunma)
- [İletişim](#İletişim)

## Kurulum Talimatları

Bu projeyi çalıştırmak için aşağıdaki adımları izleyin:

1. **Python Yükleyin**  
   Proje Python 3.12.6 sürümünde geliştirilmiştir. Eğer bilgisayarınızda Python yüklü değilse, Python'un [resmi web sitesinden](https://www.python.org/downloads/) indirip kurabilirsiniz.
   
   
   **requirements.txt İle Kütüphane Kurulumu**  
   Gerekli kitaplıkları gereksinimler.txt dosyası aracılığıyla yüklerseniz 2. ve 3. adımları atlayabilirsiniz.
   
   
2. **Scapy Kütüphanesini Kurun**  
   Proje, ağ paketlerini yakalamak ve analiz etmek için Scapy kütüphanesine ihtiyaç duyar. Scapy'yi yüklemek için terminal veya komut istemcisine şu komutu yazın:

   ```
   pip install scapy
   ```

3. **Pandas Kütüphanesini Kurun**  
   Log kayıtlarınızı daha güzel bir şekilde görselleştirmek için Pandas ve openpyxl kütüphanelerine ihtiyaç duyarsınız. Bu kütüphaneleri yüklemek için terminal veya komut istemcisine şu komutu yazın:

   ```
   pip install pandas
   ```

4. **Projeyi Yükleyin**
   Projeyi GitHub'dan klonlamak için aşağıdaki komutu kullanabilirsiniz:
   
   ```  
   git clone https://github.com/kullaniciadi/proje_adi.git
   ```
 
 ## Kullanım

Projeyi çalıştırmak için terminal veya komut istemcisinde aşağıdaki komutu yazın:

   ```
   python ids_main.py
   ```

Uygulama çalıştığında, yakalanan paketlerin detayları terminalde görüntülenecek ve aynı zamanda bir log dosyasına kaydedilecektir.

## Proje Özellikleri

- **Paket Analizi:** Ağ üzerinden geçen paketlerin içeriği analiz edilir.
- **Anomali Tespiti:** Belirli bir IP adresinden gelen anormal yüksek trafik veya beklenmedik port trafiği tespit edilir.
- **Saldırı Tespiti Kuralları:** Özel kurallar ile belirli saldırı türleri tespit edilir. **(eklenecek)**
- **Otomatik Tepki Mekanizması:** Tespit edilen saldırılar durumunda otomatik eylemler gerçekleştirilir. **(eklenecek)**
- **Veritabanı Entegrasyonu:** Yakalanan paketler ve olaylar bir veritabanına kaydedilir. **(eklenecek)**
- **Gelişmiş Görselleştirme:** Anlık trafik ve tespit edilen saldırılar görselleştirilir. **(eklenecek)**
- **Performans Testleri:** Yüksek trafik altında sistem performansı test edilir. **(eklenecek)**

## Geliştirme Süreci

Proje, aşamalı olarak geliştirilmektedir. Aşağıdaki aşamalar, projenin tamamlanması için planlanmıştır:

1. ~Paket Analizi ve Anormallik Tespiti~
2. Saldırı Tespiti Kuralları
3. Otomatik Tepki Mekanizması
4. Veritabanı Entegrasyonu
5. Gelişmiş Görselleştirme
6. Performans ve Ölçeklenebilirlik
7. Güvenlik Testleri

## Katkıda Bulunma

Bu projeye katkıda bulunmak isterseniz, aşağıdaki adımları izleyebilirsiniz:

1. Projeyi GitHub'dan fork edin.
2. Değişikliklerinizi yapın ve commit edin.
3. Pull request açın.

Her türlü katkı ve öneriye açığım!

## İletişim

Proje ile ilgili sorularınız veya önerileriniz varsa, lütfen aşağıdaki iletişim bilgilerini kullanarak benimle irtibat kurun:

- **E-posta:** [emir_ertunc@outlook.com](mailto:emir_ertunc@outlook.com)



