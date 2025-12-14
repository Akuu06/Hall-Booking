from django.db import models

class Booking(models.Model):
    applicant_name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=15)
    email = models.EmailField()
    hall_name = models.CharField(max_length=100)
    purpose = models.CharField(max_length=200)

    start_date = models.DateField()
    end_date = models.DateField()

    rent = models.DecimalField(max_digits=10, decimal_places=2)
    additional_charges = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    remark = models.CharField(max_length=100)
    receipt_no = models.CharField(max_length=50)
    status = models.CharField(max_length=50)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.applicant_name
