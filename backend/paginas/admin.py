from django.contrib import admin

from .models import Depoimento, Indicador, MensagemContato, Projeto, Tecnologia


@admin.register(Indicador)
class IndicadorAdmin(admin.ModelAdmin):
    list_display = ["rotulo", "valor", "icone", "ordem", "ativo"]
    list_editable = ["ordem", "ativo"]
    ordering = ["ordem"]


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "categoria", "ordem", "ativo"]
    list_editable = ["ordem", "ativo"]
    list_filter = ["categoria", "ativo"]
    search_fields = ["titulo", "categoria", "descricao"]
    ordering = ["ordem"]


@admin.register(Depoimento)
class DepoimentoAdmin(admin.ModelAdmin):
    list_display = ["nome", "cargo_empresa", "ordem", "ativo"]
    list_editable = ["ordem", "ativo"]
    search_fields = ["nome", "cargo_empresa"]
    ordering = ["ordem"]


@admin.register(Tecnologia)
class TecnologiaAdmin(admin.ModelAdmin):
    list_display = ["nome", "icone", "ordem", "ativo"]
    list_editable = ["ordem", "ativo"]
    ordering = ["ordem"]


@admin.register(MensagemContato)
class MensagemContatoAdmin(admin.ModelAdmin):
    list_display = ["nome", "email", "assunto", "criado_em", "lida"]
    list_editable = ["lida"]
    list_filter = ["assunto", "lida", "criado_em"]
    search_fields = ["nome", "email", "mensagem"]
    readonly_fields = ["nome", "email", "assunto", "mensagem", "criado_em"]
    ordering = ["-criado_em"]
