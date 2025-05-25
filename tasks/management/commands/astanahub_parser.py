import requests

from datetime import datetime
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand

from tasks.models import Participant


class Command(BaseCommand):
    help = 'Собирает 10 первых участников AstanaHub Techpark'

    def handle(self, *args, **options):
        url = 'https://astanahub.com/ru/service/techpark/'
        resp = requests.get(url)
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        table = soup.find("table", class_="table")
        if not table:
            raise RuntimeError("Таблица не найдена на странице")
        rows = table.tbody.find_all("tr")[:10]

        for tr in rows:
            cols = tr.find_all("td")

            issue_str = cols[1].get_text(strip=True)
            expiration_str = cols[2].get_text(strip=True)
            bin_number = cols[3].get_text(strip=True)
            status = cols[4].get_text(strip=True)
            company_name = cols[5].get_text(strip=True)

            try:
                issue_date = datetime.strptime(issue_str, "%Y-%m-%d").date()
                expiration_date = datetime.strptime(expiration_str, "%Y-%m-%d").date()
            except ValueError:
                issue_date = expiration_date = None

            obj, created = Participant.objects.update_or_create(
                bin=bin_number,
                defaults={
                    'company_name': company_name,
                    'issue_date': issue_date,
                    'expiration_date': expiration_date,
                    'status': status,
                }
            )

            action = "Создано" if created else "Обновлено"
            self.stdout.write(f"{action}: {company_name} (BIN={bin_number})")

        self.stdout.write(self.style.SUCCESS('Парсинг завершён'))