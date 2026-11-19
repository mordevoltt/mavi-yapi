import urllib.parse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from .models import SiteSetting, Service, ProjectCategory, Project, Testimonial, QuoteRequest
from .forms import QuoteRequestForm

def home(request):
    services = Service.objects.filter(is_active=True).order_by('order')
    categories = ProjectCategory.objects.all()
    projects = Project.objects.all().select_related('category').order_by('order')
    testimonials = Testimonial.objects.filter(is_active=True)
    setting = SiteSetting.get_settings()

    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            quote = form.save()
            service_label = dict(QuoteRequest.SERVICE_CHOICES).get(quote.service_type, quote.service_type)
            
            # WhatsApp için hazır mesaj metni
            wa_text = (
                f"Selamın aleyküm ustam, web sitenizden keşif talebi doldurdum:\n\n"
                f"👤 Ad Soyad: {quote.name}\n"
                f"📞 Telefon: {quote.phone}\n"
                f"📍 İlçe: {quote.district}\n"
                f"🔨 Yapılacak İş: {service_label}\n"
                f"📝 Not/Detay: {quote.message}"
            )
            encoded_msg = urllib.parse.quote(wa_text)
            clean_phone = setting.clean_whatsapp
            whatsapp_url = f"https://api.whatsapp.com/send?phone={clean_phone}&text={encoded_msg}"

            # AJAX talebi ise JSON dön
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == '1':
                return JsonResponse({
                    'status': 'success',
                    'name': quote.name,
                    'whatsapp_url': whatsapp_url,
                    'message': f"Teşekkürler Sayın {quote.name}! Talebiniz sisteme kaydedildi, WhatsApp'a aktarılıyorsunuz..."
                })

            # Normal form gönderimi ise doğrudan WhatsApp'a yönlendir
            messages.success(request, f"Talebiniz kaydedildi Sayın {quote.name}! Ustayla WhatsApp üzerinden hemen görüşebilirsiniz.")
            return redirect(whatsapp_url)
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest' or request.POST.get('ajax') == '1':
                return JsonResponse({
                    'status': 'error',
                    'errors': form.errors.as_json()
                }, status=400)
            messages.error(request, "Lütfen formdaki zorunlu alanları eksiksiz doldurunuz.")
    else:
        form = QuoteRequestForm()

    context = {
        'services': services,
        'categories': categories,
        'projects': projects,
        'testimonials': testimonials,
        'form': form,
        'setting': setting,
    }
    return render(request, 'core/index.html', context)


def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    other_services = Service.objects.filter(is_active=True).exclude(id=service.id).order_by('order')[:5]
    form = QuoteRequestForm(initial={'service_type': 'duvar'})

    context = {
        'service': service,
        'other_services': other_services,
        'form': form,
    }
    return render(request, 'core/service_detail.html', context)


def project_detail(request, pk):
    project = get_object_or_404(Project.objects.select_related('category'), pk=pk)
    related_projects = Project.objects.filter(category=project.category).exclude(id=project.id)[:3]
    form = QuoteRequestForm()

    context = {
        'project': project,
        'related_projects': related_projects,
        'form': form,
    }
    return render(request, 'core/project_detail.html', context)


def robots_txt(request):
    domain = request.build_absolute_uri('/').rstrip('/')
    lines = [
        "User-agent: *",
        "Allow: /",
        "",
        f"Sitemap: {domain}/sitemap.xml"
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain; charset=utf-8")


def sitemap_xml(request):
    domain = request.build_absolute_uri('/').rstrip('/')
    services = Service.objects.filter(is_active=True).order_by('order')
    projects = Project.objects.all().order_by('order')

    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        '  <url>',
        f'    <loc>{domain}/</loc>',
        '    <changefreq>daily</changefreq>',
        '    <priority>1.0</priority>',
        '  </url>'
    ]

    for s in services:
        xml_lines.extend([
            '  <url>',
            f'    <loc>{domain}/hizmet/{s.slug}/</loc>',
            '    <changefreq>weekly</changefreq>',
            '    <priority>0.8</priority>',
            '  </url>'
        ])

    for p in projects:
        xml_lines.extend([
            '  <url>',
            f'    <loc>{domain}/proje/{p.id}/</loc>',
            '    <changefreq>weekly</changefreq>',
            '    <priority>0.7</priority>',
            '  </url>'
        ])

    xml_lines.append('</urlset>')
    return HttpResponse("\n".join(xml_lines), content_type="application/xml; charset=utf-8")
