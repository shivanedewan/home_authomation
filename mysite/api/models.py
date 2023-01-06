from django.db import models

#Board > Pins(8, let)

class Board(models.Model):
    name    = models.CharField(max_length=30)


    def __str__(self):
        return self.name

    @property
    def pin_status(self):       #returns status of all pins through an arr [Bool]
        pins    = self.pin_set.order_by('pin_no')
        status  = [(p.pin_no ,p.status) for p in pins]
        return status

    @property
    def active_pins(self):
        return self.pin_set.filter(status=True).count()

    def pin_action(self, pin_arr):
        pins = self.pin_set.order_by('pin_no')
        if not len(pins)==len(pin_arr):
            raise ValueError('Pin Number Don\'t match should be',len(pins))
        
        for i, pin in enumerate(pins):# take in an arr 
            pin.status = pin_arr[i]
            pin.save()
        return self.pin_status


class Pin(models.Model):
    name    = models.CharField(max_length=30)
    board   = models.ForeignKey(Board, on_delete=models.CASCADE)
    pin_no  = models.PositiveIntegerField()
    status  = models.BooleanField(default=False)

    class Meta:
        unique_together = ['pin_no', 'board']
        
    
    def __str__(self):
        return f'{self.name}({self.pin_no})'

    @property
    def is_active(self):
        return bool(self.pin_no)
    
    def flip(self):
        self.status = not self.status
        self.save()
