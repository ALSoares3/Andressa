from django.db import models

# Create your models here.


class Titulo(models.Model):
    nome = models.CharField(max_length=100)
    data_de_lancamento = models.DateTimeField()
    email_para_contato = models.EmailField()
    foto_da_autora = models.FileField(upload_to='static')
    descricao_do_livro = models.TextField()

def __str__(self):
    return self.nome

class Biblioteca(models.Model):
    nome = models.CharField(max_length=50)
    data_de_lancamento = models.DateTimeField()
    email_para_contato = models.EmailField()
    foto_da_autora = models.FileField(upload_to='static')
    descricao_do_livro = models.TextField()

def __str__(self):
    return self.nome