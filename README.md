# Mavi Yapı | Kocaeli İnşaat, Tadilat & Mimari Dekorasyon

Mavi Yapı için Kocaeli ve çevre ilçelerinde anahtar teslim inşaat, alçı, boya, dış cephe mantolama, fayans ve taş-duvar işçiliği hizmetlerini sergileyen modern, mobil uyumlu ve çift yönlü WhatsApp/Admin entegrasyonlu web sitesi.

---

## 🌐 Ücretsiz Canlıya Alma (GitHub ➔ Render.com)

Bu projeyi GitHub üzerinden **Render.com** ile 2 dakikada **ücretsiz** olarak internete açabilir ve istediğiniz an kendi alan adınızı (domain) bağlayabilirsiniz:

### 1. Adım: GitHub Deposu Açma
1. [github.com](https://github.com) hesabınıza girin ve sağ üstteki **New Repository** butonuna tıklayın.
2. Repo adı olarak örn: `mavi-yapi` yazın ve **Create repository** deyin.
3. Proje klasörünüzde terminal açıp şu 3 komutu çalıştırın (kendi GitHub kullanıcı adınızla):
   ```bash
   git branch -M main
   git remote add origin https://github.com/KULLANICI_ADINIZ/mavi-yapi.git
   git push -u origin main
   ```

### 2. Adım: Render.com ile Tek Tıkla Canlıya Alma (Ücretsiz)
1. [render.com](https://render.com) adresine gidin ve **GitHub ile Giriş Yap** deyin.
2. Sağ üstten **New +** ➔ **Web Service** seçin.
3. GitHub'daki `mavi-yapi` deponuzu seçip **Connect** deyin.
4. Ayarlar:
   - **Name:** `mavi-yapi`
   - **Environment:** `Python 3`
   - **Build Command:** `./build.sh`
   - **Start Command:** `gunicorn config.wsgi:application`
   - **Instance Type:** `Free`
5. **Create Web Service** butonuna tıklayın!

Render 1-2 dakika içinde projeyi derleyecek ve size ücretsiz bir canlı link verecektir (örn: `https://mavi-yapi.onrender.com`).

---

## 🏷️ Kendi Domaininizi (Alan Adı) Bağlama
İleride alan adı aldığınızda (örn: `maviyapiinsaat.com`):
1. Render kontrol panelinde sitenizin **Settings** ➔ **Custom Domains** bölümüne gidin.
2. Alan adınızı yazın (`Add Custom Domain`).
3. Domaini satın aldığınız firmanın (GoDaddy, Turhost, İsimtescil vb.) DNS yönetiminden Render'ın vereceği `CNAME` veya `A` kaydını girin.
4. Render otomatik olarak **ücretsiz SSL (https://)** sertifikasını tanımlar ve siteniz kendi domaininizde yayın hayatına başlar!

---

## 💻 Yerel Geliştirme (Localhost)
Klasördeki `run_server.bat` dosyasına çift tıklayarak veya PowerShell ile:
```powershell
.\venv\Scripts\python.exe manage.py runserver
```
- **Site:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- **Yönetim Paneli:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
  - **Kullanıcı:** `admin`
  - **Şifre:** `admin123`
