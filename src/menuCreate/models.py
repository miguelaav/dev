from django.db import models
import uuid 

# Se definen los modelos de menu del dia
# id = Primary Key definida como registro en formato UUID
# Date = Fecha de la creación del registro
class MenuCreateModel(models.Model):
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	date = models.DateField(blank=False)
