from django.db import models

# Create your models here.

class Position(models.Model):
    position_name =models.CharField(max_length= 50)
    foot =models.CharField(max_length= 50)

    def __str__(self):
     return f"{self.position_name} ({self.foot})"

class Squad(models.Model):
    pname = models.CharField(max_length=100)
    page = models.IntegerField()
    pposition = models.ManyToManyField(Position)
    # pfoot = models.CharField(max_length=50)
    prating = models.FloatField()
    
    def __str__(self):
        return f"{self.pname} ({self.prating})"

class Adress(models.Model):
    street = models.CharField(max_length=200)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=200)

    def __str__(self):
      return f"{self.street} ({self.postal_code})"

class Clubs(models.Model):
    cname = models.CharField( max_length=200)
    cadress = models.OneToOneField(Adress,on_delete=models.CASCADE, null= True)
    ccountry = models.CharField(max_length=150)
    ccompetitions = models.CharField(max_length=150)

    def __str__(self):
       return f"{self.cname} ({self.ccountry})"

class Matches(models.Model):
    club_name = models.ForeignKey(Clubs, on_delete=models.CASCADE, null=True)
    date = models.DateField()
    stadium = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.club_name} ({self.date})"


class Table(models.Model):
   club_name= models.OneToOneField(Clubs,  on_delete=models.CASCADE, null= True)
   point = models.IntegerField()
   win = models.IntegerField()
   lose = models.IntegerField()
   draw = models.IntegerField()
   played = models.IntegerField(default=0,null=True)
   goal = models.IntegerField()
   
   def save(self, *args, **kwargs):
        self.played = self.win + self.draw + self.lose
        super(Table, self).save(*args, **kwargs)
   def __str__(self):
       return f"{self.club_name} ({self.point})"
   
   
class FanPicture(models.Model) :
    fan_picture=models.ImageField(upload_to="images")

class Fans(models.Model):
    fan_picture=models.FileField(upload_to="images", null=True)
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=(('M', 'Male'), ('F', 'Female')))
    fan_level = models.CharField(max_length=1, choices=(('C', "level3"), ('B', "level2"), ('A', "Topfan")))
    email = models.EmailField()
    password = models.CharField(max_length=100)
    

    def __str__(self):
        return f"{self.name} ({self.fan_level})"
    

   

