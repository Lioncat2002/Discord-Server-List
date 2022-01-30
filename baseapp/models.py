from django.db import models

class ServerModel(models.Model):
    #guild_icon=models.ImageField()
    guild_name=models.CharField(max_length=200)
    guild_description=models.TextField(null=True,blank=True)
    guild_link=models.URLField(max_length=200)

    def __str__(self):
        return self.guild_name
