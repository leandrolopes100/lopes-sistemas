from django import forms

from .models import MensagemContato

CLASSE_CAMPO = (
    "w-full bg-surface-muted border border-line rounded-lg text-ink placeholder-ink-faint "
    "font-sans text-body-sm px-3.5 py-3 focus:border-stamp focus:ring-2 focus:ring-stamp/20 "
    "outline-none transition-colors"
)


class MensagemContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        fields = ["nome", "email", "assunto", "mensagem"]
        widgets = {
            "nome": forms.TextInput(attrs={"placeholder": "Seu nome", "class": CLASSE_CAMPO}),
            "email": forms.EmailInput(attrs={"placeholder": "seu@email.com", "class": CLASSE_CAMPO}),
            "assunto": forms.Select(attrs={"class": CLASSE_CAMPO}),
            "mensagem": forms.Textarea(
                attrs={"placeholder": "Como posso ajudar seu negócio?", "rows": 4, "class": CLASSE_CAMPO}
            ),
        }
