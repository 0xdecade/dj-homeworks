import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        phones_data = self._load_data('phones.csv')

        for phone_dict in phones_data:
            self._save_phone(phone_dict)

    def _load_data(self, file_path):
        """Метод для чтения CSV файла"""
        try:
            with open(file_path, 'r') as file:
                return list(csv.DictReader(file, delimiter=';'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"File I/O error: {e}"))
            return []

    def _save_phone(self, phone_data):
        """Метод для сохранения одной записи в БД"""
        try:
            Phone.objects.create(**phone_data)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"DB error: {e}"))
