import helpers
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR', None)
if STATICFILES_VENDOR_DIR is None:
    raise ValueError("STATICFILES_VENDOR_DIR is not set in settings")

VENDOR_STATICFILES = {
    'flowbite.min.css': 'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.css',
    'flowbite.min.js': 'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js',
    'flowbite.min.js.map': 'https://cdn.jsdelivr.net/npm/flowbite@3.1.2/dist/flowbite.min.js.map',
}

class Command(BaseCommand):
    help = 'Hello World command'

    def handle(self, *args: Any, **kwargs: Any):
        self.stdout.write(self.style.SUCCESS('Downloading vendor static files...'))
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            
            out_path = STATICFILES_VENDOR_DIR / name
            dl_success = helpers.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
                self.stdout.write(self.style.SUCCESS(f'Successfully downloaded {name} to {out_path}'))
            else:
                self.stdout.write(self.style.ERROR(f'Failed to download {name} from {url}'))

        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS('All vendor static files downloaded successfully!'))
        else: 
            self.stdout.write(self.style.WARNING('Some vendor static files failed to download.'))