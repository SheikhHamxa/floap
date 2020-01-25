from django.db import models


# Create your models here.


class LocationType(models.Model):
    location_type = (
        ('city', 'City'),
        ('town', 'Town'),
        ('village', 'Village'),
    )
    type = models.CharField(max_length=20, choices=location_type, unique=True)
    owner = models.ForeignKey('auth.User', related_name='locationtype', on_delete=models.CASCADE)

    def __str__(self):
        return self.type


class Location(models.Model):
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
    status = (
        ('Punjab', 'PUNJAB'),
        ('Sindh', 'SINDH'),
        ('Balochistan', 'BALOCHISTAN'),
        ('kpk', 'KPK'),
    )
    province = models.CharField(max_length=100, choices=status, null=True)
    district = models.CharField(max_length=100,choices=district ,null=True)
    sector = models.CharField(max_length=100, null=True)
    street = models.CharField(max_length=100, null=True)
    house_no = models.CharField(max_length=100, null=True)
    zip_code = models.IntegerField(null=True)
    owner = models.ForeignKey('auth.User', related_name='location', on_delete=models.CASCADE)
    location_type = models.ForeignKey(LocationType, related_name='location', on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.province} {0.district} {0.sector} {0.house_no} {0.location_type}'
        return template.format(self)


class Franchise(models.Model):
    name = models.CharField(max_length=100, null=True)
    register_num = models.IntegerField(unique=True,null=True)
    num_of_employes = models.IntegerField(null=True)
    office_starting_timing = models.DateTimeField(null=True)
    office_closing_timing = models.DateTimeField(null=True)
    owner = models.ForeignKey('auth.User', related_name='franchise', on_delete=models.CASCADE)
    email = models.EmailField(unique=True,null=True)
    location = models.ForeignKey(Location, related_name='franchise', on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.name} {0.email} {0.location}'
        return template.format(self)


"""
class LocationType(models.Model):
    location_type = (
        ('C', 'City'),
        ('T', 'Town'),
        ('V', 'Village'),
        )
    type = models.CharField(max_length=1, choices=location_type)

    def __str__(self):
        return self.type
"""
"""
    gpo=models.CharField(max_length=100)
    franchise=models.CharField(max_length=100)
    province=models.CharField(max_length=100)
    owner=models.ForeignKey('auth.User', related_name='locationtype', on_delete=models.CASCADE)
    location=models.ForeignKey(Location, related_name='locationtype', on_delete=models.CASCADE)

   """
"""
class City(models.Model):
    zip_code=models.IntegerField(max_length=6)
    owner=models.ForeignKey('auth.User',related_name='city', on_delete=models.CASCADE)

    def __str__(self):
        return self.zip_code
"""

"""
class FranchiseType(models.Model):
    # gpo=models.CharField(max_length=100)
    type=models.CharField(max_length=100)
    owner=models.ForeignKey('auth.User',related_name='franchisetype', on_delete=models.CASCADE)

    def __str__(self):
        return self.type
"""
