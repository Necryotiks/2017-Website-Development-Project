"""
Definition of models.
"""
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Record(models.Model):#maek django
    first_name = models.CharField(max_length = 50, blank = True)
    last_name = models.CharField(max_length = 50, blank = True)
    date = models.DateField()
    phone_num = models.CharField(max_length = 50, blank = True)
    email = models.EmailField(max_length = 50, blank = True)
    street_address = models.CharField(max_length = 50,blank = True)
    city = models.CharField(max_length = 50,blank = True)
    STATE_LIST = (('AL','Alabama'),('AK','Alaska'),('AZ','Arizona'),('AK','Arkansas'),
        ('CA','California'),('CO','Colorado'),('CT','Connecticut'),('DE','Delaware'),
        ('FL','Florida'),('GA','Georgia'),('HI','Hawaii'),('ID','Idaho'),
        ('IL','Illinois'),('IN','Indiana'),('IA','Iowa'),('KS','Kansas'),
        ('KY','Kentucky'),('LA','Louisiana'),('ME','Maine'),('MD','Maryland'),
        ('MA','Massachusetts'),('MI','Michigan'),('MN','Minnesota'),('MS','Mississippi'),
        ('MO','Missouri'),('MT','Montana'),('NE','Nebraska'),('NV','Nevada'),
        ('NH','New Hampshire'),('NJ','New Jersey'),('NM','New Mexico'),('NY','New York'),
        ('NC','North Carolina'),('ND','North Dakota'),('OH','Ohio'),('OK','Oklahoma'),
        ('OR','Oregon'),('PA','Pennsylvania'),('RI','Rhode Island'),('SC','South Carolina'),
        ('SD','South Dakota'),('TN','Tennessee'),('TX','Texas'),('UT','Utah'),
        ('VT','Vermont'),('VA','Virgina'),('WA','Washington'),('WV','West Virgina'),
        ('WI','Wisconsin'),('WY','Wyoming'),('AS','American Samoa'),('DC','District of Columbia'),
        ('FM','Federated States of Micronesia'),('GU','Guam'),('MH','Marshall Islands'),('MP','Northern Mariana Islands'),
        ('PW','Palau'),('PR','Puerto Rico'),('VI','United States Virgin Islands'),('AE','Armed Forces Africa'),
        ('AA','Armed Forces Americas'),('AE','Armed Forces Canada'),('AE','Armed Forces Europe'),('AE','Armed Forces Middle East'),
        ('AP','Armed Forces Pacific'))#First string is for database, second is displayed to user...I think
    state = models.CharField(max_length = 2,choices = STATE_LIST)
    zip = models.CharField(max_length = 5, blank = True)
    CARRIER_LIST = (('AT&T','AT&T'),('VERIZON','VERIZON'),('SPRINT','SPRINT'),('T-MOBILE','T-MOBILE'),)#First string is for database, second is displayed to user...I think
    carrier = models.CharField(max_length = 10,choices = CARRIER_LIST)
    text = models.CharField(max_length = 140, blank = True)
