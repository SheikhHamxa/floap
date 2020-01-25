from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

from location.models import Franchise
from package.models import PackageRates

# from package.models import Package, PackageRates
# from vehicle.models import Vehicle
from vehicle.models import Vehicle

LEXERS = [item for item in get_all_lexers() if item[1]]
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


class UserType(models.Model):
    User_Type = (
        ('SENDER', 'Sender'),
        ('RECEIVER', 'Receiver'),
        ('MANAGER', 'Manager'),
        ('STAFF','Staff'),
        ('ADMIN','Admin'),
        ('Driver','Driver'),
        ('POST_PERSON', 'post_person')

    )
    user_type = models.CharField(max_length=15, choices=User_Type)
    owner = models.ForeignKey('auth.User', related_name='usertype', on_delete=models.CASCADE)

    def __str__(self):
        template= '{0.user_type} '
        return template.format(self)

"""
    sender = models.CharField(max_length=100)
    receiver = models.CharField(max_length=100)
    post_person = models.CharField(max_length=100)
    staff = models.CharField(max_length=100)
    manager = models.CharField(max_length=100)
    Admin = models.CharField(max_length=100)

    def __str__(self):
        return self.sender
"""


class USer(models.Model):
    status = (
        ('Punjab', 'PUNJAB'),
        ('Sindh', 'SINDH'),
        ('Balochistan', 'BALOCHISTAN'),
        ('kpk', 'KPK'),
    )
    select_gender = (('M', 'MALE'),
                     ('F', 'FEMALE'),
                     )

    created = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100,  null=True)
    email = models.EmailField(unique=True)
    city = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100)
    cnic = models.CharField(max_length=100, unique=True)
    gender = models.CharField(max_length=1, choices=select_gender)
    province = models.CharField(max_length=100, null=True, choices=status)
    sector = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    house_no = models.CharField(max_length=100, null=True)
    owner = models.ForeignKey('auth.User', related_name='user', on_delete=models.CASCADE)
    #    sender= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # receiver= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # manager= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # admin= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # driver= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # post_person= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    # staff= models.ForeignKey('self', related_name='user', on_delete=models.CASCADE,blank=True)
    usertype = models.ForeignKey(UserType, related_name='user', on_delete=models.CASCADE)
    # package=models.ForeignKey(Package,related_name='package',on_delete=models.CASCADE)
    franchise = models.ForeignKey(Franchise, related_name='user', on_delete=models.CASCADE)
    # location = models.ForeignKey(Location, related_name='user', on_delete=models.CASCADE)
    # "" packagerates = models.ForeignKey(PackageRates, related_name='user', on_delete=models.CASCADE)
    vehicle = models.ManyToManyField(Vehicle)
    # highlighted = models.TextField()

    # class Meta:
    # ordering = ['created', ]

    def __str__(self):
        template = '{0.first_name} {0.last_name} {0.email} {0.sector} '
        return template.format(self)


"""
    def save(self, *args, **kwargs):  # new
        
        

        lexer = get_lexer_by_name(self.language)
        linenos = 'table' if self.linenos else False
        options = {'title': self.title} if self.title else {}
        formatter = HtmlFormatter(style=self.style, linenos=linenos,
                                  full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Employe, self).save(*args, **kwargs)
"""

"""
class Sender(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    USer = models.ForeignKey(Employe, related_name='sender', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='sender', on_delete=models.CASCADE)

    def __str__(self):
        return self.USer.first_name


class Receiver(models.Model):
    province = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    house_no = models.CharField(max_length=100)
    USer = models.ForeignKey(Employe, related_name='receiver', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='receiver', on_delete=models.CASCADE)
    sender = models.ManyToManyField(Sender)

    def __str__(self):
        return self.USer.first_name

"""
"""
class PostPerson(models.Model):
    USer = models.ForeignKey(Employe, related_name='postperson', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='postperson', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()


class Manager(models.Model):
    USer = models.ForeignKey(Employe, related_name='manager', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='manager', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()


class Staff(models.Model):
    USer = models.ForeignKey(Employe, related_name='staff', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='staff', on_delete=models.CASCADE)
    employe_number = models.IntegerField()
    duty_tyming = models.DateTimeField()
    
"""""