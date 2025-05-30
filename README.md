# پروژه حل مسئله n وزیر

## معرفی

در این پروژه، مسئله کلاسیک n وزیر پیاده‌سازی شده است. هدف، قرار دادن n وزیر روی یک صفحه شطرنج n×n است به‌طوری که هیچ‌کدام از وزیرها در یک سطر، ستون یا قطر با دیگری اشتراک نداشته باشند.

## الگوریتم‌ها

برای حل مسئله، از دو الگوریتم متفاوت استفاده شده است:

- الگوریتم پسگرد (Backtracking): روشی کلاسیک و دقیق برای پیدا کردن تمام یا اولین راه‌حل ممکن.
- الگوریتم ژنتیک (Genetic Algorithm): روشی تقریبی مبتنی بر تکامل طبیعی، مناسب برای حل سریع‌تر در مقیاس بزرگ‌تر.

## نحوه عملکرد برنامه

1. ابتدا برنامه یک رابط گرافیکی ساده ایجاد می‌کند.
2. کاربر مقدار n را وارد می‌کند.
3. هر دو الگوریتم به ترتیب اجرا می‌شوند.
4. نتیجه هر الگوریتم به‌صورت گرافیکی روی یک صفحه جداگانه نمایش داده می‌شود.
5. تخته شطرنج با وزیرهای قرار گرفته‌شده نمایش داده می‌شود.

## ساختار فایل

تمام منطق برنامه در فایل n_queens_gui.py قرار دارد و شامل بخش‌های زیر است:

- دریافت ورودی از کاربر از طریق رابط گرافیکی
- توابع مربوط به الگوریتم Backtracking
- توابع مربوط به الگوریتم Genetic
- توابع رسم تخته شطرنج و نمایش گرافیکی نتایج

## نحوه اجرا

برای اجرای برنامه،  دستور زیر را در ترمینال اجرا کنید:

python n_queens_gui.py