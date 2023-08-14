from django.db import models

# Create your models here.

class Item(models.Model):
    item_name = models.CharField(db_column="Item_Name", max_length=200)
    item_desc = models.CharField(db_column="Item_Desc", max_length=200)
    item_price = models.IntegerField(db_column="Item_Price",)

    def __str__(self) -> str:
        return f"{self.item_name}"

    class Meta:
        managed = True
        db_table = "tblItems"
