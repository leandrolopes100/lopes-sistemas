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
        "cor_fundo": "#0b1c30",
        "ordem": 1,
    },
    {
        "categoria": "Fintech",
        "titulo": "Dashboard Financeiro",
        "descricao": "Visualização de KPIs em tempo real com integração bancária segura via APIs.",
        "cor_fundo": "#0058be",
        "ordem": 2,
    },
    {
        "categoria": "Indústria",
        "titulo": "CRM Industrial",
        "descricao": "Otimização do ciclo de vendas e acompanhamento de contratos para fábricas.",
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
    {"nome": "TypeScript", "icone": "javascript", "ordem": 1},
    {"nome": "React", "icone": "frame_source", "ordem": 2},
    {"nome": "Node.js", "icone": "hub", "ordem": 3},
    {"nome": "PostgreSQL", "icone": "database", "ordem": 4},
    {"nome": "Docker", "icone": "view_in_ar", "ordem": 5},
    {"nome": "AWS", "icone": "cloud_queue", "ordem": 6},
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
