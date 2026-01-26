from django.db import models


class Assessment(models.Model):
    # An assessment belongs to a teaching assignment (teacher + subject + classroom)
    teaching_assignment = models.ForeignKey(
        "teaching.TeachingAssignment",
        on_delete=models.PROTECT,
        related_name="assessments",
    )

    # Term (Term 1, Term 2, Term 3)
    term = models.ForeignKey(
        "academics.Term",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assessments",
    )

    name = models.CharField(max_length=100)  # e.g. "Midterm", "Quiz 1"
    date = models.DateField(null=True, blank=True)
    max_score = models.PositiveIntegerField(default=100)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.teaching_assignment}"


class Mark(models.Model):
    assessment = models.ForeignKey(
        "assessments.Assessment",
        on_delete=models.CASCADE,
        related_name="marks",
    )
    student = models.ForeignKey(
        "students.Student",
        on_delete=models.PROTECT,
        related_name="marks",
    )

    score = models.DecimalField(max_digits=6, decimal_places=2)  # e.g. 75.50
    comment = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["assessment", "student"],
                name="unique_mark_per_student_per_assessment",
            )
        ]

    def __str__(self):
        return f"{self.student} - {self.assessment}: {self.score}"
