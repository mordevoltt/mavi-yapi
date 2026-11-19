from django.db import models
from django.utils.text import slugify

class SiteSetting(models.Model):
    title = models.CharField(max_length=150, default="Mavi Yapı | Kocaeli İnşaat, Tadilat & Mimari Dekorasyon", verbose_name="Site Başlığı")
    slogan = models.CharField(max_length=255, default="Kocaeli ve Çevresinde Kaliteli İşçilik, Güvenli Yapılar", verbose_name="Slogan")
    phone = models.CharField(max_length=30, default="0541 635 41 13", verbose_name="Telefon")
    whatsapp = models.CharField(max_length=30, default="905416354113", verbose_name="WhatsApp No (Örn: 905xxxxxxxxx)")
    email = models.EmailField(default="iletisim@maviyapi.com", verbose_name="E-posta")
    address = models.CharField(max_length=255, default="Kocaeli Geneli (İzmit, Gebze, Kartepe, Başiskele, Körfez ve Tüm İlçeler)", verbose_name="Adres")
    working_hours = models.CharField(max_length=100, default="Pazartesi - Cumartesi: 08:00 - 19:30 (Pazar Acil Keşif)", verbose_name="Çalışma Saatleri")
    
    # İstatistikler
    years_experience = models.PositiveIntegerField(default=18, verbose_name="Yıllık Tecrübe")
    completed_projects = models.PositiveIntegerField(default=460, verbose_name="Tamamlanan Proje")
    satisfied_clients = models.PositiveIntegerField(default=430, verbose_name="Mutlu Müşteri")
    master_craftsmen = models.PositiveIntegerField(default=15, verbose_name="Usta & Ekip Sayısı")

    about_text = models.TextField(
        default="Mavi Yapı olarak Kocaeli ve çevre ilçelerinde 18 yılı aşkın saha tecrübemiz ve uzman ustalarımızla; anahtar teslim komple inşaattan lüks villa tadilatına, alçı-boyadan dış cephe kaplama ve fayans döşemeye kadar hayallerinizdeki yapıları kaliteli işçilik ve güvenle inşa ediyoruz.",
        verbose_name="Hakkımızda Özeti"
    )

    class Meta:
        verbose_name = "Site Genel Ayarları"
        verbose_name_plural = "Site Genel Ayarları"

    def __str__(self):
        return self.title

    @property
    def clean_phone(self):
        digits = "".join(filter(str.isdigit, str(self.phone)))
        if digits.startswith("0"):
            return "+9" + digits
        elif not digits.startswith("90"):
            return "+90" + digits
        return "+" + digits

    @property
    def clean_whatsapp(self):
        digits = "".join(filter(str.isdigit, str(self.whatsapp)))
        if digits.startswith("0"):
            digits = "9" + digits
        elif not digits.startswith("90"):
            digits = "90" + digits
        return digits

    @classmethod
    def get_settings(cls):
        settings_obj, _ = cls.objects.get_or_create(id=1)
        return settings_obj


class Service(models.Model):
    title = models.CharField(max_length=150, verbose_name="Hizmet Adı")
    slug = models.SlugField(max_length=160, unique=True, blank=True)
    icon = models.CharField(
        max_length=50, 
        default="fa-hammer", 
        verbose_name="FontAwesome İkon Kodu",
        help_text="Örn: fa-brick, fa-trowel-bricks, fa-paint-roller, fa-home, fa-layer-group, fa-ruler-combined"
    )
    short_description = models.CharField(max_length=250, verbose_name="Kısa Özet")
    description = models.TextField(verbose_name="Detaylı Açıklama")
    image_url = models.CharField(
        max_length=500, 
        blank=True, 
        verbose_name="Görsel URL / Yol", 
        help_text="Web veya statik görsel linki"
    )
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")
    is_active = models.BooleanField(default=True, verbose_name="Yayında mı?")

    class Meta:
        verbose_name = "Hizmet"
        verbose_name_plural = "Hizmetlerimiz"
        ordering = ['order', 'id']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategori Adı")
    slug = models.SlugField(max_length=120, unique=True, blank=True)

    class Meta:
        verbose_name = "Proje Kategorisi"
        verbose_name_plural = "Proje Kategorileri"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Proje Başlığı")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE, related_name="projects", verbose_name="Kategori")
    location = models.CharField(max_length=150, verbose_name="Konum / İlçe", default="İstanbul")
    description = models.TextField(verbose_name="Yapılan İşlemler & Detay")
    image_url = models.CharField(max_length=500, verbose_name="Ana Proje Görseli URL'si")
    before_image_url = models.CharField(max_length=500, blank=True, null=True, verbose_name="Tadilat Öncesi Görseli (İsteğe bağlı)")
    completion_year = models.CharField(max_length=10, default="2026", verbose_name="Teslim Yılı")
    is_featured = models.BooleanField(default=True, verbose_name="Ana Sayfada Öne Çıkar")
    order = models.PositiveIntegerField(default=0, verbose_name="Sıralama")

    class Meta:
        verbose_name = "Proje"
        verbose_name_plural = "Projelerimiz (Portfolyo)"
        ordering = ['order', '-id']

    def __str__(self):
        return f"{self.title} ({self.category.name})"


class Testimonial(models.Model):
    client_name = models.CharField(max_length=120, verbose_name="Müşteri Adı Soyadı")
    project_type = models.CharField(max_length=150, verbose_name="Yapılan İş (Örn: Villa Duvar & Komple Tadilat)")
    location = models.CharField(max_length=100, verbose_name="Konum (Örn: Kadıköy)")
    rating = models.PositiveSmallIntegerField(default=5, verbose_name="Yıldız Puanı (1-5)")
    comment = models.TextField(verbose_name="Yorum / Değerlendirme")
    is_active = models.BooleanField(default=True, verbose_name="Gösterilsin mi?")

    class Meta:
        verbose_name = "Müşteri Yorumu"
        verbose_name_plural = "Müşteri Yorumları"

    def __str__(self):
        return f"{self.client_name} - {self.project_type}"


class QuoteRequest(models.Model):
    SERVICE_CHOICES = [
        ('duvar', 'Duvar İşçiliği (Tuğla, Gazbeton, Taş Duvar)'),
        ('komple_tadilat', 'Komple Anahtar Teslim Tadilat'),
        ('ic_tasarim', 'İç Mekan Tasarım, Alçıpan & Boya'),
        ('dis_cephe', 'Dış Cephe Mantolama & Kaplama'),
        ('fayans_seramik', 'Fayans, Seramik & Granit Döşeme'),
        ('cati_izolasyon', 'Çatı Tamiri & Su/Isı İzolasyonu'),
        ('diger', 'Diğer Özel İnşaat / Onarım İşi'),
    ]

    name = models.CharField(max_length=120, verbose_name="Ad Soyad")
    phone = models.CharField(max_length=30, verbose_name="Telefon")
    email = models.EmailField(blank=True, null=True, verbose_name="E-posta (İsteğe bağlı)")
    district = models.CharField(max_length=100, verbose_name="İl / İlçe")
    service_type = models.CharField(max_length=50, choices=SERVICE_CHOICES, default='duvar', verbose_name="Talep Edilen Hizmet")
    message = models.TextField(verbose_name="İşin Detayları ve Açıklama")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Başvuru Tarihi")
    is_contacted = models.BooleanField(default=False, verbose_name="Ulaşıldı / Geri Dönüş Yapıldı")

    class Meta:
        verbose_name = "Keşif & Fiyat Teklifi Talebi"
        verbose_name_plural = "Keşif & Fiyat Teklifi Talepleri"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.phone} ({self.get_service_type_display()})"
