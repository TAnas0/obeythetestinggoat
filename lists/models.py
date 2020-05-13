from django.db import models

class ItemList(models.Model):
    url_name = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Item(models.Model):
    text = models.CharField(max_length=50)
    item_list = models.ForeignKey(ItemList, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
