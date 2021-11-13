import os
import uuid
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
# Create your models here.
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('uploads/thumbnail_images/', filename)



class Properties(models.Model):
    # BUY_OR_SELL=[('BUY','BUY'),('SELL','SELL') ]
    TYPE=[('2kh','2_KANAL_HOUSE'),('1kh','1_KANAL_HOUSE'),
    ('4mh','14_MARLAR_HOUSE'),('5mh','5_MARLAR_HOUSE'),
    ('2kp','2_KANAL_PLOT'),('1kp','1_KANAL_PLOT'),
    ('4mp','14_MARLAR_PLOT'),('5mp','5_MARLAR_PLOT'),
    ('5ep','5_MARLA_EXTENSION_PLOT'),('5kf','5_KANAL_FARM'),('2kc','2_KANAL_CONSTRUCTION'),('1kc','1_KANAL_CONSTRUCTION'),('5mc','5_MARLA_CONSTRUCTION'),('4mc','14_MARLA_CONSTRUCTION')
    ]
    OWNER_OR_BROKER=[('O','OWNER'),('B','BROKER')]
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    phone =PhoneNumberField(_("Phone No."))
    image = models.ImageField(upload_to=get_file_path)
    video_links = models.URLField(_("Video Link"),max_length=200,blank=True,null=True)
    description = models.CharField(max_length=225)
    owner_or_broker = models.CharField(max_length=1,choices=OWNER_OR_BROKER)
    # buy_or_sell = models.CharField(max_length=4,choices=BUY_OR_SELL)
    category = models.CharField(_("Properties Type"), max_length=3,choices=TYPE)



    def __str__(self):
        return f'{self.name} - {self.price} - {self.phone} - {self.owner_or_broker} - {self.category}'

class Bid(models.Model):
    property_id= models.ForeignKey(Properties,on_delete=models.CASCADE,related_name='bidders')
    bid_price = models.IntegerField()
    bidder_name = models.CharField(max_length=100)
    bidder_phone = PhoneNumberField(_("Phone No"),region='PK')

    class Meta:
        unique_together = ('property_id','bidder_phone')


    def __str__(self) -> str:
        return f'{self.bid_price} {self.bidder_name} {self.property_id}';


class Youtube(models.Model):
    youtube_link = models.URLField(_("Youtube Link"),max_length=200)


    def __str__(self):
        return f'{self.youtube_link}'