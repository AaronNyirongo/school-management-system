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

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["teacher", "classroom", "subject"],
                name="unique_teacher_class_subject",
            )
        ]

    def __str__(self):
        return f"{self.teacher} -> {self.subject} ({self.classroom})"
