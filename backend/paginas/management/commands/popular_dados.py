from io import BytesIO

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand
from PIL import Image, ImageDraw, ImageFont

from paginas.models import Depoimento, Indicador, Projeto, Tecnologia

INDICADORES = [
    {"icone": "cloud_done", "valor": "99.9%", "rotulo": "Uptime Garantido", "ordem": 1},
    {"icone": "trending_down", "valor": "40%", "rotulo": "Redução de Custos", "ordem": 2},
    {"icone": "groups", "valor": "500+", "rotulo": "Usuários Ativos", "ordem": 3},
]

PROJETOS = [
    {
        "categoria": "Logística",
        "titulo": "ERP de Logística",
        "descricao": "Gestão completa de frotas e automação de rotas para transportadoras de grande porte.",
        "stack": "Django · PostgreSQL · Bootstrap",
        "cor_fundo": "#0b1c30",
        "ordem": 1,
    },
    {
        "categoria": "Fintech",
        "titulo": "Dashboard Financeiro",
        "descricao": "Visualização de KPIs em tempo real com integração bancária segura via APIs.",
        "stack": "Django · PostgreSQL · Chart.js",
        "cor_fundo": "#0058be",
        "ordem": 2,
    },
    {
        "categoria": "Indústria",
        "titulo": "CRM Industrial",
        "descricao": "Otimização do ciclo de vendas e acompanhamento de contratos para fábricas.",
        "stack": "Django (CBV) · PostgreSQL · Bootstrap",
        "cor_fundo": "#213145",
        "ordem": 3,
    },
]

DEPOIMENTOS = [
    {
        "nome": "Ricardo Mendes",
        "cargo_empresa": "Diretor de Operações, LogiTrans S.A.",
        "texto": "A implementação do novo ERP transformou completamente nossa agilidade operacional. "
        "Reduzimos o tempo de processamento de pedidos em 60% logo no primeiro mês.",
        "ordem": 1,
    },
]

TECNOLOGIAS = [
    {"nome": "Python", "icone": "code", "ordem": 1},
    {"nome": "Django", "icone": "widgets", "ordem": 2},
    {"nome": "Java", "icone": "coffee", "ordem": 3},
    {"nome": "JavaScript", "icone": "javascript", "ordem": 4},
    {"nome": "PostgreSQL", "icone": "database", "ordem": 5},
    {"nome": "Bootstrap / Tailwind", "icone": "palette", "ordem": 6},
    {"nome": "APIs REST", "icone": "api", "ordem": 7},
    {"nome": "Docker", "icone": "view_in_ar", "ordem": 8},
    {"nome": "Nginx", "icone": "dns", "ordem": 9},
    {"nome": "VPS / Linux", "icone": "terminal", "ordem": 10},
]


def gerar_imagem_placeholder(titulo, cor_fundo):
    imagem = Image.new("RGB", (800, 480), color=cor_fundo)
    desenho = ImageDraw.Draw(imagem)
    fonte = ImageFont.load_default()
    caixa_texto = desenho.textbbox((0, 0), titulo, font=fonte)
    largura_texto = caixa_texto[2] - caixa_texto[0]
    altura_texto = caixa_texto[3] - caixa_texto[1]
    posicao = ((800 - largura_texto) / 2, (480 - altura_texto) / 2)
    desenho.text(posicao, titulo, fill="#ffffff", font=fonte)
    buffer = BytesIO()
    imagem.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), name=f"{titulo}.png")


class Command(BaseCommand):
    help = "Popula o banco com o conteúdo inicial da landing page (indicadores, projetos, depoimentos, tecnologias)."

    def handle(self, *args, **opcoes):
        for dados in INDICADORES:
            Indicador.objects.get_or_create(rotulo=dados["rotulo"], defaults=dados)

        for dados in PROJETOS:
            if Projeto.objects.filter(titulo=dados["titulo"]).exists():
                continue
            cor_fundo = dados.pop("cor_fundo")
            projeto = Projeto(
                categoria=dados["categoria"],
                titulo=dados["titulo"],
                descricao=dados["descricao"],
                stack=dados["stack"],
                texto_alternativo=f"Screenshot ilustrativo do projeto {dados['titulo']}",
                ordem=dados["ordem"],
            )
            projeto.imagem.save(
                f"{dados['titulo']}.png",
                gerar_imagem_placeholder(dados["titulo"], cor_fundo),
                save=True,
            )

        for dados in DEPOIMENTOS:
            Depoimento.objects.get_or_create(nome=dados["nome"], defaults=dados)

        for dados in TECNOLOGIAS:
            Tecnologia.objects.get_or_create(nome=dados["nome"], defaults=dados)

        self.stdout.write(self.style.SUCCESS("Dados iniciais populados com sucesso."))
