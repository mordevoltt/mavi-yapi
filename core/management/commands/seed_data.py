from django.core.management.base import BaseCommand
from core.models import SiteSetting, Service, ProjectCategory, Project, Testimonial

class Command(BaseCommand):
    help = "Mavi Yapı Kocaeli inşaat sitesi için gerçek verileri yükler"

    def handle(self, *args, **kwargs):
        self.stdout.write("Mavi Yapı verileri yükleniyor...")

        # Site Ayarları
        setting, _ = SiteSetting.objects.get_or_create(id=1)
        setting.title = "Mavi Yapı | Kocaeli İnşaat, Tadilat & Mimari Dekorasyon"
        setting.slogan = "Kocaeli ve Çevresinde Kaliteli İşçilik, Güvenli Yapılar"
        setting.phone = "0541 635 41 13"
        setting.whatsapp = "905416354113"
        setting.email = "iletisim@maviyapi.com"
        setting.address = "Kocaeli (İzmit, Gebze, Kartepe, Başiskele, Körfez ve tüm Kocaeli geneli ücretsiz keşif)"
        setting.working_hours = "Pazartesi - Cumartesi: 08:00 - 19:30 (Pazar Acil Keşif)"
        setting.years_experience = 18
        setting.completed_projects = 460
        setting.satisfied_clients = 430
        setting.master_craftsmen = 15
        setting.about_text = (
            "Mavi Yapı olarak Kocaeli ve çevre ilçelerinde 18 yılı aşkın saha tecrübemiz ve uzman ustalarımızla; "
            "anahtar teslim komple inşaattan lüks villa tadilatına, alçı-boyadan dış cephe mantolama ve seramik-fayans "
            "döşemeye kadar hayallerinizdeki yapıları kaliteli işçilik ve güvenle inşa ediyoruz."
        )
        setting.save()

        # Hizmetler
        services_data = [
            {
                "title": "Anahtar Teslim İnşaat & Tadilat",
                "slug": "anahtar-teslim-insaat",
                "icon": "fa-house",
                "short_description": "Kocaeli genelinde temelden çatıya kaba ve ince inşaat, daire ve komple villa tadilatı.",
                "description": "Eski ve yıpranmış yapılarınızı modern mimariyle baştan inşa ediyoruz. Yıkım-kırım, moloz atımı, su-elektrik tesisatı, şap, sıva, zemin kaplama, boya ve montaj sürecini tek elden eksiksiz yürütüyoruz.",
                "image_url": "/static/images/projects/is_1.jpg",
                "order": 1
            },
            {
                "title": "Alçı & Alçıpan İşleri",
                "slug": "alci-alcipan",
                "icon": "fa-trowel",
                "short_description": "Asma tavan, gizli LED ışık bandı, saten alçı ve dekoratif tavan sistemleri.",
                "description": "İç mekanlarınıza estetik kazandıran modern alçıpan tavan sistemleri, gizli LED ışık havuzları, bölme duvarlar, saten alçı çekimi ve pürüzsüz yüzey hazırlığı.",
                "image_url": "/static/images/projects/is_12.jpg",
                "order": 2
            },
            {
                "title": "Boya & Dekorasyon",
                "slug": "boya-dekorasyon",
                "icon": "fa-paint-roller",
                "short_description": "İç cephe silinebilir boya, İtalyan efekt boya ve dış cephe silikonlu boya uygulamaları.",
                "description": "Tozsuz zımparalama ve kaliteli boya markalarıyla pürüzsüz yüzeyler. Renk danışmanlığı, tavan boyası, kapı ve ahşap boyama işleri.",
                "image_url": "/static/images/projects/is_3.jpg",
                "order": 3
            },
            {
                "title": "Dış Cephe Mantolama",
                "slug": "dis-cephe-mantolama",
                "icon": "fa-shield-halved",
                "short_description": "Yüksek ısı yalıtımı sağlayan TSE belgeli mantolama, fileli sıva ve dekoratif cephe kaplama.",
                "description": "Binanızı yazın serin, kışın sıcak tutan ve yakıt faturalarını %50'ye varan oranda düşüren mantolama çözümleri. Güvenli iskele kurulumu, fileli sıva ve dekoratif mineral kaplama.",
                "image_url": "/static/images/projects/is_7.jpg",
                "order": 4
            },
            {
                "title": "Fayans & Seramik Döşeme",
                "slug": "fayans-seramik",
                "icon": "fa-border-all",
                "short_description": "Lazer terazi ile banyo, mutfak, teras ve salonlar için 60x120 seramik ve granit döşeme.",
                "description": "Büyük ebat porselen seramikler, banyo su yalıtım izolasyonu ve sıfır hata lazerli terazi işçiliği. Eğim ve su gideri testleri yapılarak teslim edilir.",
                "image_url": "/static/images/projects/is_10.jpg",
                "order": 5
            },
            {
                "title": "Duvar & Taş İşçiliği",
                "slug": "duvar-tas-isciligi",
                "icon": "fa-cubes",
                "short_description": "Tuğla, gazbeton (Ytong) bölme duvar örme, bahçe istinat ve dekoratif doğal taş kaplama.",
                "description": "Milimetrik şakül ve teraziyle gazbeton (Ytong) bölme duvar yapımı, villa çevre istinat duvarı ve dekoratif doğal taş kaplama ustalığı.",
                "image_url": "/static/images/projects/is_6.jpg",
                "order": 6
            }
        ]

        for s_data in services_data:
            Service.objects.update_or_create(slug=s_data["slug"], defaults=s_data)

        # Proje Kategorileri
        cat_duvar, _ = ProjectCategory.objects.get_or_create(name="Duvar & Taş İşçiliği", slug="duvar-tas-isciligi")
        cat_tadilat, _ = ProjectCategory.objects.get_or_create(name="Komple Tadilat", slug="komple-tadilat")
        cat_ic, _ = ProjectCategory.objects.get_or_create(name="İç Mekan & Alçı Boya", slug="ic-mekan-alci-boya")
        cat_dis, _ = ProjectCategory.objects.get_or_create(name="Dış Cephe & Mantolama", slug="dis-cephe-mantolama")

        # Projeler
        projects_data = [
            {
                "title": "Müstakil Villa Doğal Taş Kaplama & Dış Cephe",
                "category": cat_duvar,
                "location": "Kartepe / Kocaeli",
                "description": "Villa bahçe duvarı ve dış cephesine doğal kayrak taş kaplama, harçlı taş duvar ve çevre düzenleme işçiliği.",
                "image_url": "/static/images/projects/is_6.jpg",
                "completion_year": "2026",
                "order": 1,
                "is_featured": True
            },
            {
                "title": "Modern Çok Katlı Konut Dış Cephe Giydirme & Mantolama",
                "category": cat_dis,
                "location": "İzmit / Kocaeli",
                "description": "Çok katlı modern konut projesinde ahşap görünümlü kompozit cephe, taşyünü mantolama ve dekoratif sıva uygulaması.",
                "image_url": "/static/images/projects/is_7.jpg",
                "completion_year": "2026",
                "order": 2,
                "is_featured": True
            },
            {
                "title": "Lüks Salon Asma Tavan & Şömine Taş Kaplama",
                "category": cat_ic,
                "location": "Başiskele / Kocaeli",
                "description": "Modern villa salonunda gizli LED ışık havuzlu asma tavan, pürüzsüz saten alçı ve dekoratif taş kaplama şömine alanı.",
                "image_url": "/static/images/projects/is_3.jpg",
                "completion_year": "2026",
                "order": 3,
                "is_featured": True
            },
            {
                "title": "Geniş Salon Lazer Terazili 60x120 Seramik Döşeme",
                "category": cat_tadilat,
                "location": "Gebze / Kocaeli",
                "description": "Hassas lazer terazi ve klips sistemiyle sıfır kot farkıyla 60x120 granit seramik döşeme ve derz dolgusu.",
                "image_url": "/static/images/projects/is_10.jpg",
                "completion_year": "2026",
                "order": 4,
                "is_featured": True
            },
            {
                "title": "Müstakil Villa Kaba İnşaat & Ytong Duvar Örme",
                "category": cat_duvar,
                "location": "Gölcük / Kocaeli",
                "description": "2 katlı modern villanın dış cephe ve iç bölme duvarlarının milimetrik şakülle Ytong gazbeton bloklarla örülmesi.",
                "image_url": "/static/images/projects/is_5.jpg",
                "completion_year": "2025",
                "order": 5,
                "is_featured": True
            },
            {
                "title": "Özel Geometrik Alçıpan Asma Tavan & Işık Bandı",
                "category": cat_ic,
                "location": "Körfez / Kocaeli",
                "description": "Usta el işçiliğiyle dairesel ve geometrik alçıpan tavan imalatı, akustik asma tavan ve gizli aydınlatma.",
                "image_url": "/static/images/projects/is_12.jpg",
                "completion_year": "2026",
                "order": 6,
                "is_featured": True
            }
        ]

        for p_data in projects_data:
            Project.objects.update_or_create(title=p_data["title"], defaults=p_data)

        # Yorumlar
        testimonials_data = [
            {
                "client_name": "Ahmet Yılmaz",
                "project_type": "Villa Dış Cephe & Mantolama",
                "location": "İzmit / Kocaeli",
                "rating": 5,
                "comment": "Mavi Yapı ekibi İzmit'teki villamızın dış cephesini ve mantolamasını yaptı. İskele kurulumundan iş bitimine kadar son derece tertipli çalıştılar. 0541 635 41 13 numarasından aradığımızda her zaman doğrudan ustayla muhatap olduk."
            },
            {
                "client_name": "Serkan Demir",
                "project_type": "Anahtar Teslim Daire Tadilatı",
                "location": "Kartepe / Kocaeli",
                "rating": 5,
                "comment": "Evimizi baştan aşağı yenilediler; alçıpan tavanlar, banyo fayansları ve boya badana kusursuz oldu. Lazer terazili çalışma dedikleri gibi sıfır hata çıktı, kesinlikle tavsiye ederim."
            },
            {
                "client_name": "Murat Kaya",
                "project_type": "Taş Duvar & Çevre Düzenleme",
                "location": "Başiskele / Kocaeli",
                "rating": 5,
                "comment": "Bahçe istinat duvarı ve doğal taş kaplama işini tam gününde teslim ettiler. İşçilikleri gerçekten çok sağlam. Teşekkürler Mavi Yapı."
            }
        ]

        Testimonial.objects.all().delete()
        for t_data in testimonials_data:
            Testimonial.objects.create(**t_data)

        self.stdout.write(self.style.SUCCESS("Mavi Yapı Kocaeli verileri başarıyla yüklendi!"))
