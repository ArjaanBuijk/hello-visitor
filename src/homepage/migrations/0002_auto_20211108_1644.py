from django.db import migrations
from ..models import VisitCounter


def insert_default_items(_apps, _schema_editor):
    """Populates database with one visit counter."""
    # To learn about `apps`, see:
    # https://docs.djangoproject.com/en/3.2/topics/migrations/#data-migrations
    VisitCounter.insert_visit_counter()


class Migration(migrations.Migration):
    """Runs a data migration"""

    dependencies = [
        ("homepage", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(insert_default_items),
    ]
