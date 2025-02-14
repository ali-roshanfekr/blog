# middleware.py
from django.core.cache import cache
from django.http import HttpResponseForbidden


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        ip = self.get_client_ip(request)
        if self.is_banned(ip):
            return HttpResponseForbidden("Your IP has been banned due to too many requests.")

        # ثبت زمان درخواست
        self.track_request(ip)

        response = self.get_response(request)
        return response

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def track_request(self, ip):
        key = f"request_count_{ip}"
        count = cache.get(key, 0)
        count += 1

        if count > 1000:
            # بن کردن IP
            cache.set(f"banned_{ip}", True, timeout=86400)  # بن کردن به مدت 24 ساعت
        else:
            cache.set(key, count, timeout=86400)  # تنظیم تایم‌اوت به 24 ساعت

    def is_banned(self, ip):
        key = f"banned_{ip}"
        return cache.get(key, False)
