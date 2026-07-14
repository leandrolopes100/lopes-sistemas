from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import MensagemContatoForm
from .models import Depoimento, Indicador, Projeto, Tecnologia


def pagina_inicial(request):
    if request.method == "POST":
        formulario = MensagemContatoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Mensagem enviada com sucesso! Em breve entraremos em contato.")
            return redirect(f"{request.path}#contact")
        messages.error(request, "Verifique os campos do formulário e tente novamente.")
    else:
        formulario = MensagemContatoForm()

    contexto = {
        "indicadores": Indicador.objects.filter(ativo=True),
        "projetos": Projeto.objects.filter(ativo=True),
        "depoimentos": Depoimento.objects.filter(ativo=True),
        "tecnologias": Tecnologia.objects.filter(ativo=True),
        "formulario": formulario,
    }
    return render(request, "paginas/home.html", contexto)
