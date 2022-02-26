from pyexpat import model
from tabnanny import verbose
from django.db import models

STA_CHOICES=(
    ('ENTREGUE', 'ENTREGUE'),
    ('PREPARO', 'PREPARO'),
)
    
QUANT_CHOICES= (
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
)
PAG_QUANT= (
    ('PIX', 'PIX'),
    ('CC', 'CARTÃO_CREDITO'),
    ('CD', 'CARTAO_DEBITO'),
    ('DINHEIRO', 'DINHEIRO'),
)

def upload_image_comida(instance, filename):
    return f'{instance.nome}-{filename}'

class Base(models.Model):
    publicacao= models.DateTimeField(auto_now_add=True)
    atualizacao= models.DateTimeField(auto_now=True)
    ativo=models.BooleanField(default=True)
    
    class Meta:
        abstract=True
        
class item(Base):
    nomei=models.CharField(max_length=120)
    descricao=models.TextField(max_length=350)
    valor= models.DecimalField(max_digits=20, decimal_places=2)
    imagem = models.ImageField(upload_to=upload_image_comida, blank=True, null=True)

    class Meta:
        verbose_name='item'
        verbose_name_plural='itens'
        
    def __str__(self):
        return self.nomei
        

class pedido(Base):
    cliente= models.CharField(max_length=100)
    ped_cliente=models.ForeignKey(item, on_delete=models.CASCADE)
    quan= models.CharField(max_length=1, choices=QUANT_CHOICES)
    pag= models.CharField(max_length=9, choices=PAG_QUANT)
    
    class Meta:
        verbose_name='PEDIDO'
        
    def __str__(self):
        return self.cliente 
        

class entrega(Base):
    identi= models.ForeignKey(pedido, on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=STA_CHOICES)