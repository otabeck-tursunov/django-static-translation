# Django-ModelTranslation
- **Notion sahifa: https://soapy-fisherman-347.notion.site/Django-Multi-Language-f489e64601c049ebb83cc47908831a45?pvs=4**
- **Static Translation**
    - [***GetText*](https://mlocati.github.io/articles/gettext-iconv-windows.html) dasturini o’rnatish uchun link:**
        
        [gettext 0.21 and iconv 1.16 - Binaries for Windows](https://mlocati.github.io/articles/gettext-iconv-windows.html)
        
    
    ---
    
    - **settings.py faylimizga quyidagi o’zgarishlarni kiritamiz:**
        
        ```python
        **LANGUAGE_CODE = 'uz-uz'
        TIME_ZONE = 'UTC', # mintaqani o'zgartirishimiz mumkin. 
        # O'zbekiston uchun mintaqalar: 'Etc/GMT-5', 'Asia/Tashkent', 'Asia/Samarkand'
        USE_TZ = True
        USE_L10N = True
        USE_I18N = True**
        ```
        
    - **Saytimizda bo’lishi kerak bo’lgan tillarni quyidagi shaklda settings.py fayliga qo’shamiz:**
        
        ```python
        **from django.utils.translation import gettext_lazy as _
        
        LANGUAGES = (
            ('en', _('English')),
            ('uz', _('Uzbek')),
        )
        
        # Ko'p holatlarda gettext_lazy() funksiyasini "_" nomga o'rkazib ishlatiladi
        # yoki oddiy holatda ham ishlatishingiz mumkin:
        
        from django.utils.translation import gettext_lazy
        
        LANGUAGES = (
            ('en', gettext_lazy('English')),
            ('uz', gettext_lazy('Uzbek')),
        )**
        ```
        
    - **settings.py faylimizga yana bir MIDDLEWARE qo'shishimiz kerak:
                                                                           `'django.middleware.locale.LocaleMiddleware'`**
        
        ```python
        **MIDDLEWARE = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.locale.LocaleMiddleware', # yangi
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]**
        ```
        
    - **Endi, tarjimalarimiz saqlanadigan papka manzilni settings.py fayliga saqlaymiz:**
        
        ```python
        **LOCALE_PATHS = [
            BASE_DIR / 'locale/',
        ]**
        ```
        
         **- Bu papka quyidagi ko’rinishda shakllanadi, bu papka ichida har bir til uchun yana alohida papkalar ajratiladi:**
        
        ```bash
        **locale
        ├── en
        ├── uz
        └── ..**
        ```
        
    - **Endi misol uchun oddiy model yaratamiz:**
        
        ```python
        **from django.db import models
        from django.utils.translation import gettext_lazy as _
        
        class Article(models.Model):
            title = models.CharField(_('Sarlavha'), max_length=50)
            description = models.TextField(_('Batafsil'))
        
            def __str__(self):
                return self.title**
        ```
        
         **- E’tibor bering ‘gettext_lazy’ni  ‘_’ ko’rinishida ishlatyapmiz, agar siz o’z nomi bilan ishlatgan bo’lsangiz ‘gettext_lazy’ ni o’zidan foydalaning!**
        
    - **Natija uchun HTML sahifasini yaratamiz:**
        
        ```python
        **{% load i18n %}
        
        {% trans 'Salom' %}**
        ```
        
         **- Shablonimzda tarjima qilmoqchi bo’lgan so’zlarimizni yuqoridagi kabi ko’rinishda      yozamiz!**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/4ded61d3-fb9a-4bb6-a381-a15e88f8b9e9/Untitled.png)
        
        **Izoh: Bu yerda hozir faqat o’zbek tilida, boshqa tillarni endi qo’shib chiqamiz!**
        
        ---
        
    - **Yuqorida yaratib olgan locale papkamizda tarjima ma’lumotlarini saqlash uchun Terminalda quyidagi buyruqni yozing:**
        
        ```python
        **django-admin makemessages --all --ignore=env**
        ```
        
         **- ignore=env qismidagi env sizning virtual muhitingiz nomi bilan bir xil bo’lishi kerak, agar nom qo’ymagan bo’lsangiz django o’zi env/venv nomi bilan yaratadi!**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5f1f6033-c6f7-49f3-a93e-3928611ba298/Untitled.png)
        
         **- Buyruqni yozishdan avval barchar tillar uchun alohida papka yaratganingizga ishonch hosil qiling! (en, uz, … kabi)**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/971e6512-6d05-4477-a0d4-ca9a57bb133a/Untitled.png)
        
         **- Buyruqni yozganingizdan so’ng rasmdagidek bizning locale faylimizda .po fayllar yaratiladi.** 
        
    - **Endi ushbu fayllarni ko’rib chiqamiz:**
        
        **/locale/en/django.po**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2fe2c44e-c6d1-4428-8c6a-65fbbb9db939/Untitled.png)
        
         **- Ko’rib turganingizdek biz o’zgartirmochi bo’lgan so’zlarimiz, endi msgstrga Ingliz tilidagi so’zlarni yozib chiqishimiz kerak quyidagicha:**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/5487f7f5-d626-4576-bb09-caab60fb3e37/Untitled.png)
        
    - **Quyidagi buyruq orqali tarjimalarni .mo fayliga saqlaymiz:**
        
        ```python
        **django-admin compilemessages --ignore=env**
        ```
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/772814da-8f88-4fcf-b167-48ef223fa2d8/Untitled.png)
        
         **- Ko’rib turganingizdek yangi django.mo fayli yaratildi.**
        
    
    - **urls.py faylimizga qo’shimcha qo’shamiz:**
        
        ```python
        **from django.conf.urls.i18n import i18n_patterns
        
        urlpatterns = [
            *i18n_patterns(*urlpatterns, prefix_default_language=False),
            ]**
        ```
        
        ---
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/8c4cb2a3-9ed7-48b8-89a2-53e2c616107d/Untitled.png)
        
    - **Endi bajarganlarimizni tekshirsak bo’ladi:**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9f7c40ea-4679-4c2d-bcb6-21748e4c2889/Untitled.png)
        
         **- Sahifani ingliz tiliga tarjima qilish uchun urlga “/en/” ni qo’shib yozamiz:**
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/a62b82fe-ce64-4ab8-b59b-53ee300637c3/Untitled.png)
        
         **- Ko’rib turganingizdek dasturimiz to’g’ri ishlayapti, umid qilamanki sizda ham o’xshadi!
