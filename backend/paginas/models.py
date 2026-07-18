from django.db import models


class Indicador(models.Model):
    icone = models.CharField(max_length=50, help_text="Nome do ícone Material Symbols, ex: cloud_done")
    valor = models.CharField(max_length=20, help_text="Ex: 99.9%, 40%, 500+")
    rotulo = models.CharField(max_length=100)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"

    def __str__(self):
        return f"{self.valor} — {self.rotulo}"


class Projeto(models.Model):
    categoria = models.CharField(max_length=50)
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    stack = models.CharField(max_length=150, blank=True, help_text="Ex: Django · PostgreSQL · Bootstrap")
    imagem = models.ImageField(upload_to="projetos/")
    texto_alternativo = models.CharField(max_length=255, blank=True)
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Projeto"
        verbose_name_plural = "Projetos"

    def __str__(self):
        return self.titulo


class Depoimento(models.Model):
    nome = models.CharField(max_length=100)
    cargo_empresa = models.CharField(max_length=150)
    texto = models.TextField()
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Depoimento"
        verbose_name_plural = "Depoimentos"

    def __str__(self):
        return self.nome


class Tecnologia(models.Model):
    nome = models.CharField(max_length=50)
    icone = models.CharField(max_length=50, help_text="Nome do ícone Material Symbols, ex: hub")
    ordem = models.PositiveIntegerField(default=0)
    ativo = models.BooleanField(default=True)

    class Meta:
        ordering = ["ordem"]
        verbose_name = "Tecnologia"
        verbose_name_plural = "Tecnologias"

    def __str__(self):
        return self.nome


class MensagemContato(models.Model):
    ASSUNTO_NOVO_PROJETO = "novo_projeto"
    ASSUNTO_CONSULTORIA = "consultoria"
    ASSUNTO_MANUTENCAO = "manutencao"
    ASSUNTO_ESCOLHAS = [
        (ASSUNTO_NOVO_PROJETO, "Novo Projeto"),
        (ASSUNTO_CONSULTORIA, "Consultoria"),
        (ASSUNTO_MANUTENCAO, "Manutenção"),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=20, choices=ASSUNTO_ESCOLHAS, default=ASSUNTO_NOVO_PROJETO)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    lida = models.BooleanField(default=False)

    class Meta:
        ordering = ["-criado_em"]
        verbose_name = "Mensagem de Contato"
        verbose_name_plural = "Mensagens de Contato"

    def __str__(self):
        return f"{self.nome} — {self.get_assunto_display()}"
