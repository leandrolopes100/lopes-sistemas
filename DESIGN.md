---
name: Sinal Limpo
colors:
  paper: '#fafaf9'
  surface: '#ffffff'
  surface-muted: '#f4f4f6'
  line: '#e4e4e9'
  ink: '#111114'
  ink-dim: '#6b6d74'
  ink-faint: '#a4a6ac'
  signal: '#4f3df5'
  signal-dim: '#eeecfe'
  signal-deep: '#3b2ed1'
  success: '#1f9d55'
  error: '#d64545'
typography:
  display-mobile:
    fontFamily: Instrument Sans
    fontSize: 34px
    fontWeight: '700'
    lineHeight: '1.15'
    letterSpacing: -0.01em
  display-lg:
    fontFamily: Instrument Sans
    fontSize: 56px
    fontWeight: '700'
    lineHeight: '1.05'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Instrument Sans
    fontSize: 34px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Instrument Sans
    fontSize: 22px
    fontWeight: '500'
    lineHeight: '1.45'
  headline-sm:
    fontFamily: Instrument Sans
    fontSize: 18px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.65'
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.65'
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  eyebrow:
    fontFamily: Inter
    fontSize: 12.5px
    fontWeight: '600'
    lineHeight: '1'
    letterSpacing: 0.08em
  caption:
    fontFamily: Inter
    fontSize: 12.5px
    fontWeight: '400'
    lineHeight: '1.4'
  data-md:
    fontFamily: Instrument Sans
    fontSize: 26px
    fontWeight: '600'
    lineHeight: '1'
  data-lg:
    fontFamily: Instrument Sans
    fontSize: 44px
    fontWeight: '700'
    lineHeight: '1'
rounded:
  sm: 8px
  DEFAULT: 10px
  md: 12px
  lg: 16px
  xl: 20px
  full: 9999px
spacing:
  base: 8px
  xs: 4px
  sm: 12px
  md: 24px
  lg: 40px
  xl: 64px
  gutter: 24px
  margin-desktop: 48px
  margin-mobile: 16px
---

## Brand & Style

O sistema visual é **clean e direto** — a referência é o produto de software sério (Linear, Vercel, Stripe): fundo claro, muito espaço em branco, um único acento vibrante, tipografia sans nítida. Nada de ornamento; a clareza é o produto. Cada elemento existe para reduzir esforço de leitura, não para impressionar.

A personalidade é **confiança objetiva**: sem escurecer a tela para parecer "premium", sem console técnico piscando para parecer "avançado" — o visual comunica que o software funciona bem porque é simples de olhar. O único elemento de assinatura é o **bloco "Como chega / Como fica"** no hero: ícones dispersos (planilha, WhatsApp, papel) convergindo por uma linha tracejada animada até um único ícone de sistema — a tese do negócio (bagunça operacional → sistema único) expressa visualmente, não só em texto.

## Colors

- **paper / surface:** `paper` é o fundo de página (quase-branco, levemente quente); `surface` é branco puro, reservado para cards e painéis elevados — a diferença sutil entre os dois cria profundidade sem sombra pesada.
- **surface-muted:** Preenchimento de seções alternadas e de elementos secundários (chips de tecnologia, thumbnails antes de carregar).
- **line:** Única cor de borda do sistema — cards, divisores, inputs. Sempre 1px, nunca decorativa.
- **ink / ink-dim / ink-faint:** Três níveis de texto — primário (quase preto), secundário (parágrafos), terciário (legendas, placeholders, eyebrows neutros).
- **signal:** Único acento de ação — CTAs, links, ícones ativos, palavra de destaque no H1, eyebrows. Usado com moderação; a página é 95% neutra para que o `signal` continue lendo como sinal, não decoração.
- **signal-dim:** Tint muito claro do acento — fundo de badges de categoria, ícones de contato, círculo do ícone de aspas.
- **success / error:** Reservados exclusivamente para feedback de formulário.

## Typography

Duas famílias, cada uma com um papel:

- **Instrument Sans:** Headlines, títulos de seção, números de indicadores (`tabular-nums`), nome do depoimento. Geométrica e um pouco mais caráter que Inter — dá personalidade ao display sem recorrer a serifa ou peso itálico.
- **Inter:** Corpo de texto, labels, navegação, botões. Eyebrows usam Inter em versalete rastreado (`letter-spacing: 0.08em`, uppercase, cor `signal`) — o único lugar da página em caixa alta.

Não há fonte monoespaçada no sistema — evitado deliberadamente após a v1 (console/mono) ter lido como "futurista" para o cliente.

## Layout & Spacing

Ritmo de 8px. Margens responsivas: `16px` no mobile, `48px` no desktop.

O hero divide copy e o **card de assinatura**: bloco "Como chega / Como fica" no topo + painel de indicadores reais do backend logo abaixo, sem decoração adicional — o card inteiro é um único elemento funcional, não um enfeite ao lado do texto.

## Shapes & Elevation

Cantos suavizados (8–20px, mais arredondados que sistemas anteriores — aproxima do padrão de produto SaaS atual). Elevação vem de `shadow-sm/md/lg` do Tailwind (sombras baixas, difusas, nunca pretas puras) combinada com borda `line` de 1px — cards "flutuam" discretamente, sem glass effect nem gradiente decorativo além do glow radial muito sutil atrás do H1.

## Components

- **Botões:** `signal` sólido para ação primária (texto branco), borda `line` para secundária (hover: borda e texto `signal`). Texto em sentença normal, nunca caixa alta.
- **Inputs:** Fundo `surface-muted`, borda `line`, foco em anel `signal` (`ring-2 ring-signal/20` + borda `signal`). Labels em eyebrow.
- **Cards de portfólio:** Imagem com leve dessaturação (`grayscale-[0.6]`) que revela cor plena no hover, elevação de sombra + leve translateY. Categoria como pill (`signal-dim` bg, `signal` texto, `rounded-full`).
- **Depoimento:** Aspas em círculo `signal-dim`, texto em Instrument Sans (sem itálico), nome em `signal`.
- **Reveal on scroll:** Seções entram com fade+translate via `IntersectionObserver`, controlado por uma classe `.js-reveal` adicionada via JS — se o JavaScript falhar, o conteúdo permanece visível por padrão. Respeita `prefers-reduced-motion`.

## Histórico de versões

1. **v1 — Painel de Operação:** console técnico, grafite + âmbar, JetBrains Mono. Rejeitado: "muito futurista".
2. **v2 — Boutique de Operações:** tinta escura + dourado + Fraunces serifada, editorial/premium. Aprovado inicialmente, mas reavaliado depois como não suficientemente "moderno".
3. **v3 — Sinal Limpo (atual):** clean minimalista claro, inspirado em Linear/Vercel/Stripe. Acento único `signal` (violeta), Instrument Sans + Inter, sombras suaves, sem fonte mono.
