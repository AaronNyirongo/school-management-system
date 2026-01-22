from django.db import models

class ClassRoom(models.Model):
    LEVEL_CHOICES = [
        ("G1", "Grade 1"),
        ("G2", "Grade 2"),
        ("G3", "Grade 3"),
        ("G4", "Grade 4"),
        ("G5", "Grade 5"),
        ("G6", "Grade 6"),
        ("G7", "Grade 7"),
        ("G8", "Grade 8"),
        ("G9", "Grade 9"),
        ("F1", "Form 1"),
        ("F2", "Form 2"),
        ("F3", "Form 3"),
        ("F4", "Form 4"),
        ("F5", "Form 5"),
        ("F6", "Form 6"),
    ]

    level = models.CharField(max_length=2, choices=LEVEL_CHOICES)
    stream = models.CharField(max_length=10, blank=True)  # e.g. A, B, C
    year = models.PositiveIntegerField(null=True, blank=True)  # optional

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["level", "stream", "year"], name="unique_classroom_level_stream_year")
        ]

    def __str__(self):
        parts = [self.get_level_display()]
        if self.stream:
            parts.append(self.stream)
        if self.year:
            parts.append(str(self.year))
        return " - ".join(parts)
