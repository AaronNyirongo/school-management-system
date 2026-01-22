from django.db import models

class AttendanceRecord(models.Model):
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["student", "date"], name="unique_attendance_student_date")
        ]

    student = models.ForeignKey("students.Student", on_delete=models.CASCADE, related_name="attendance_records")
    date = models.DateField()
    present = models.BooleanField(default=True)
    note = models.CharField(max_length=255, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        status = "Present" if self.present else "Absent"
        return f"{self.student} - {self.date} - {status}"
