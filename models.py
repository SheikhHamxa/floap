from django.db import models
from location.models import Location, Franchise
# from USer.models import USer

# Create your models here.
# from location.models import  Location
from vehicle.models import Vehicle


class PackageRates(models.Model):
    district = (
        ('Rawalpindi', 'RAWALPINDI'),
        ('Islamabd', 'ISLAMAABAD'),
        ('Faislabad', 'FAISALABAD'),
        ('Peshawer', 'PESHAWER'),
        ('Karachi', 'KARACHI'),
        ('Lahore', 'LAHORE'),
        ('Abbotabad', 'ABBOTABAD'),
        ('Quetta', 'QUETTA'),
        ('Hyderabd', 'HYDERABAD'),
        ('Attock', 'ATTOCK'),
        ('Bahawalnager', 'BAHAWALNAGR'),
        ('Bahawalpur', 'BAHAWALPUR'),
        ('Bhakker', 'BHAKKER'),
        ('Chakwal', 'CHAKWAL'),
        ('Gujrat', 'GUJRAT'),
        ('Gujranwala', 'GUJRANWALA'),
        ('Hafzabad', 'HAFIZABAD'),
        ('Multan', 'MULTAN'),
        ('Rahim yar khan', 'RAHIM_YAR_KHAN'),
        ('Sahiwal', 'SAHIWAL'),
        ('Sarghoda', 'SARGHODA'),
        ('Sialkot', 'SIALKOT'),
        ('Layyah', 'LAYYAH'),
        ('Tibbet', 'TIBBET'),
        ('Chamman', 'CHAMMAN'),
        ('Sui', 'SUI'),
        ('ZHOB', 'ZHOB'),
        ('Gawader', 'GAWADAR'),
        ('Sukhhar', 'SUKKHAR'),
        ('Ghotki', 'GHOTKI'),
        ('Naushro feroz', 'NAUSHERO FEROZ'),
        ('Tharphar', 'THARPAR'),
        ('Mirpur khas', 'MIRPUR KHAS'),
        ('Sheikupura', 'SHIKHARPUR'),
        ('Larkana', 'LARKANA'),
        ('Jacobabad', 'JACOBABAD'),
        ('Malir', 'MALIR'),
        ('Karachi east', 'KARACHI EAST'),
        ('Karachi west', 'KARACHI WEST'),
        ('Bannu', 'BANUU'),
        ('Laki marawat', 'LAKI MARAWAT'),
        ('Dera Ismail khan', 'DERA ISMAIL'),
        ('Mansehra', 'MANSEHARA'),
        ('Haripur', 'HARIPUR'),
        ('Kohat', 'KOHAT'),
        ('Shingla', 'SHANGLA'),
        ('Chitral', 'CHITRAL'),
        ('Swat', 'SAWAT'),
        ('Mardan', 'MARDAN'),
        ('Swabi', 'SAWABI'),
        ('Charsada', 'CHARSEDA'),
        ('Bagh', 'BAGH'),
        ('Mirpur', 'MIRPUR'),
        ('Rawalakot', 'RAWALAKOT'),


    )
    price_package_title= (

        ('60 rupees','BOOK/COPY_Size for less than 500 gram of book/copy'),
        ('180 rupees of book/copy','BOOK/COPY_Size between 500 gm To 1000 gram '),
        ('250 rupees of book/copy', 'BOOK/COPY_Size between 1000 gm To 2000 gram'),
        ( '45 rupees of documents','DOCUMENTS_SIZE less than 30 gram '),
        ('70 rupees of documents' , 'DOCUMENTS_SIZE  between 30gm To 100 gram  '),
        ('170 rupees of documents', 'DOCUMENTS_Size  between 100 To 200 gram '),
        ('70 rupees of Other physical material', 'OTHER_PHYSICAL_INSTRUMENTS_Size less than 300 gram  '),
        ('170 rupees of physical material','OTHER_PHYSICAL_INSTRUMENTS_Size between 300 to 1000 gram for other'),
        ('200 rupees other physical material', 'OTHER_PHYSICLA_INSTRUMENTS_Size more than 1000 gram ')

    )
    price_per_gram = models.CharField(max_length=100, choices=price_package_title)
    from_place = models.CharField(max_length=100, choices=district, null=True)
    to_place = models.CharField(max_length=100, choices=district, null=True)
    # ""    location = models.ManyToManyField(Location, related_name='packagerates', null=True)
    owner = models.ForeignKey('auth.User', related_name='packagerates', on_delete=models.CASCADE)

    def __str__(self):
        template= '{0.from_place}  {0.to_place}'
        return template.format(self)


class PackageStatus(models.Model):
    package_status = (
        ('PENDING', 'Pending'),
        ('READY_FOR_PICKUP', 'Ready_For_Pickup'),
        ('ON_THE_WAY', 'On_Way'),
        ('AT_FRANCHISE', 'At_Franchise'),
        ('READY_FOR_SHIPMENT', 'Ready_For_Shipment'),
        ('SHIPMENT_GOES','Shipment_Goes')
    )
    status = models.CharField(max_length=100, choices=package_status)
    owner = models.ForeignKey('auth.User', related_name='packagestatus', on_delete=models.CASCADE)
    # package = models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        template= ' {0.status}'
        return template.format(self)


class Package(models.Model):
    package_title= (
        ("BOOK/COpy", 'Book/Copy'),
        ('DOCUMENTS', 'Documents'),
        ('OTHER_PHYSICAL_INSTRUMENTS', "Other_Physical_Instruments")

    )
    name = models.CharField(max_length=100, choices=package_title)
    # item_type = models.TextField()
    arrivel_date = models.DateField()
    owner = models.ForeignKey('auth.User', related_name='package', on_delete=models.CASCADE)
    packagerates = models.ForeignKey(PackageRates, related_name='package', on_delete=models.CASCADE)
    # "" vehicle = models.ForeignKey(Vehicle, related_name='package', on_delete=models.CASCADE)
    user = models.ForeignKey('USer.USer', related_name='package', on_delete=models.CASCADE)
    # USer=models.ForeignKey(Employe, related_name='package', on_delete=models.CASCADE)
    packagestatus = models.ForeignKey(PackageStatus, related_name='package', on_delete=models.CASCADE)

    def __str__(self):
        template= '{0.name} {0.arrivel_date} {0.packagerates}'
        return template.format(self)


class PackageBilling(models.Model):
    owner = models.ForeignKey('auth.User', related_name='packagebilling', on_delete=models.CASCADE)

    # bill_pay=models.CharField(max_length=100, unique=True)
    package=models.OneToOneField(Package, on_delete=models.CASCADE, primary_key=True)
    franchise=models.ForeignKey(Franchise, related_name= 'packagebilling', on_delete=models.CASCADE)

    def __str__(self):
        return self.package.name




"""


Status_Package = (
    ('pending', 'PENDING'),
    ('ready_for_shipment', 'READY_FOR_SHIPMENT'),
    ('on_the_way', 'ON_THE_WAY'),
    ('at_franchise', 'AT_FRANCHISE'),
    ('ready_for_pickup', 'READY_FOR_PICKUP'),
)
"""

"""
class PackageStatus(models.Model):
    status = models.CharField(max_length=15)
    package = models.ForeignKey(Package, related_name='package_status', on_delete=models.CASCADE)
    owner = models.ForeignKey('auth.User', related_name='package_status', on_delete=models.CASCADE)

    def __str__(self):
        return self.status
"""
