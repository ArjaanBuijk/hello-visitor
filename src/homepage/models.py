"""Defines the models"""
from django.db import models


class VisitCounter(models.Model):
    """ORM for VisitCounter"""

    count = models.IntegerField()

    @staticmethod
    def insert_visit_counter():
        """Populates database with one visit counter. Call from a data migration."""
        visit_counter = VisitCounter(count=0)
        visit_counter.save()

    def __str__(self):
        return f"VisitCounter - number of visits: {self.count}"
