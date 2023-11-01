from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here. 
class Post(models.Model):
    body_text = models.TextField('Texto Principal') 
    pub_date = models.DateTimeField('Data Publicação')
    categoria = models.CharField(
    'Categoria',
    max_length=15,
    choices=['
        ('noticias', 'Noticias'),
        ('como fazer', 'Como Fazer'),
        ('review', 'Review'),
    ],
    default=None,
    null=True
)

autor = models.ForeignKey(
    User, 
    editable=False, 
    on_delete=models.DO_NOTHING, # não exclui a pergunta se o autor for removido null=True a permite autor NULL para não conflitar com registros já existentes
    null=True 
)