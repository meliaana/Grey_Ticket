import uuid

from django.db import models


class Ticket(models.Model):
    code = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def save(self, *args, **kwargs):
        self.code = self.generate_key()
        return super(Ticket, self).save(*args, **kwargs)

    @staticmethod
    def generate_key():
        return uuid.uuid4().hex

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(to='user.User', on_delete=models.CASCADE, related_name='order')
    ticket = models.OneToOneField(to='Ticket', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.ticket}'
