from django.test import TestCase, Client
from django.urls import reverse
from core.models import SiteSetting, Service, ProjectCategory, Project, QuoteRequest

class CoreSiteTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.setting = SiteSetting.get_settings()
        self.category = ProjectCategory.objects.create(name="Duvar İşçiliği", slug="duvar-isciligi")
        self.service = Service.objects.create(
            title="Duvar İşçiliği",
            slug="duvar-isciligi",
            short_description="Tuğla ve taş duvar örme",
            description="Detaylı duvar açıklaması",
            order=1
        )
        self.project = Project.objects.create(
            title="Kadıköy Duvar Örme",
            category=self.category,
            location="Kadıköy",
            description="Proje açıklaması",
            image_url="https://images.unsplash.com/test.jpg"
        )

    def test_home_page_status(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Duvar İşçiliği")
        self.assertContains(response, "Mavi Yapı")
        self.assertContains(response, "Kocaeli")
        self.assertContains(response, "0541 635 41 13")

    def test_service_detail_status(self):
        response = self.client.get(reverse('core:service_detail', kwargs={'slug': self.service.slug}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Duvar İşçiliği")

    def test_project_detail_status(self):
        response = self.client.get(reverse('core:project_detail', kwargs={'pk': self.project.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Kadıköy Duvar Örme")

    def test_quote_form_submission(self):
        data = {
            'name': 'Ali Usta Test',
            'phone': '05551234567',
            'email': 'ali@example.com',
            'district': 'Kadıköy',
            'service_type': 'duvar',
            'message': 'Duvar örme işi için keşif istiyorum.'
        }
        response = self.client.post(reverse('core:home'), data, follow=False)
        self.assertEqual(response.status_code, 302)
        self.assertIn("whatsapp", response.url.lower())
        self.assertTrue(QuoteRequest.objects.filter(name='Ali Usta Test').exists())
