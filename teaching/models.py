from django.db import models


class TeachingAssignment(models.Model):
    teacher = models.ForeignKey(
        "teachers.Teacher",
        on_delete=models.PROTECT,
        related_name="assignments",
    )

    classroom = models.ForeignKey(
        "academics.ClassRoom",
        on_delete=models.PROTECT,
        related_name="teaching_assignments",
    )

    subject = models.ForeignKey(
        "subjects.Subject",
        on_delete=models.PROTECT,
        related_name="teaching_assignments",
    )

    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.PROTECT,
        related_name="teaching_assignments",
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "classroom", "subject", "term"],
                name="unique_teaching_assignment",
            )
        ]

    def __str__(self):
        return f"{self.teacher} -> {self.subject} ({self.classroom})"
