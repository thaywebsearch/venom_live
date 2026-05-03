# 🩸 Imagem em Movimento — Venom Edition

> Projeto Streamlit com **CSS Injection** · **HTML Render** · **Conversão IMG → Base64**  
> Deploy automático via **GitHub** + **Streamlit Community Cloud**

---

## 🔴 Demo

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://SEU_USER-SEU_REPO-app-HASH.streamlit.app)

---

## 📁 Estrutura do Projeto

```
imagem-em-movimento/
│
├── app.py              ← Estrutura 1 · Script principal Streamlit
├── img_to_base64.py    ← Estrutura 2 · Conversor IMG → Base64
├── logo.png            ← Imagem do logotipo (Venom)
├── requirements.txt    ← Estrutura 3 · Dependências do projeto
└── README.md           ← Este ficheiro
```

---

## ⚙️ As 3 Estruturas

### Estrutura 1 — `app.py` · Script Principal

Script Streamlit que combina duas técnicas para renderizar a imagem animada:

| Técnica | Descrição |
|---|---|
| **CSS Injection** | Estilos injetados via `st.markdown(..., unsafe_allow_html=True)` |
| **HTML Render** | Bloco HTML completo renderizado dentro do Streamlit |
| **Base64 Embed** | Imagem embutida no HTML como Data URI — sem ficheiros externos |

```python
# Injeção de CSS global
st.markdown(CSS, unsafe_allow_html=True)

# Renderização do HTML com imagem embutida
st.markdown(HTML, unsafe_allow_html=True)
```

**Animações CSS incluídas:**
- `venom-float` — flutuação suave da imagem
- `venom-glow` — pulso de brilho neon azul ↔ roxo
- `spin` — anéis orbitais giratórios (sentidos opostos)
- `flicker` — efeito de cintilação no título
- `ambient-pulse` — glow ambiente radial de fundo
- `drip-pulse` — barra de energia pulsante

---

### Estrutura 2 — `img_to_base64.py` · Conversor IMG → Base64

Módulo de conversão de imagem para string Base64, importado pelo `app.py`.

**Pipeline de conversão:**

```
logo.png
   │
   ▼  file.read_bytes()
[bytes binários]   →  b'\x89PNG\r\n...'
   │
   ▼  base64.b64encode()
[bytes Base64]     →  b'iVBORw0KGgo...'
   │
   ▼  .decode("utf-8")
[string Base64]    →  'iVBORw0KGgo...'
   │
   ▼  embutida no HTML
src="data:image/png;base64,iVBORw0KGgo..."
```

**Funções disponíveis:**

```python
from img_to_base64 import img_to_base64, get_mime_type, img_to_data_uri

# Retorna string Base64 pura
b64 = img_to_base64("logo.png")

# Retorna o MIME type correto
mime = get_mime_type("logo.png")        # → "image/png"

# Retorna o Data URI completo
uri = img_to_data_uri("logo.png")       # → "data:image/png;base64,..."
```

**Formatos suportados:** `.png` · `.jpg` · `.jpeg` · `.webp` · `.gif` · `.svg`

**Testar via terminal:**
```bash
python img_to_base64.py logo.png
```

---

### Estrutura 3 — `requirements.txt` · Dependências

```txt
streamlit>=1.35.0
```

> `base64` e `pathlib` são bibliotecas nativas do Python e **não precisam** ser declaradas.

---

## 🚀 Como Correr Localmente

**1. Clonar o repositório**
```bash
git clone https://github.com/SEU_USER/SEU_REPO.git
cd SEU_REPO
```

**2. Instalar dependências**
```bash
pip install -r requirements.txt
```

**3. Lançar a aplicação**
```bash
streamlit run app.py
```

Acede em: `http://localhost:8501`

---

## ☁️ Deploy — Streamlit Community Cloud

**1. Push para o GitHub**
```bash
git add app.py logo.png requirements.txt img_to_base64.py README.md
git commit -m "feat: imagem em movimento — estrutura completa"
git push -u origin main
```

**2. Conectar ao Streamlit Cloud**

| Campo | Valor |
|---|---|
| Repository | `SEU_USER/SEU_REPO` |
| Branch | `main` |
| Main file path | `app.py` |

Acede a [share.streamlit.io](https://share.streamlit.io) → **New app** → preenche os campos → **Deploy!**

**3. Atualizações automáticas**

A cada `git push`, o Streamlit Cloud faz o redeploy automaticamente — sem nenhuma ação manual.

```bash
git add .
git commit -m "update: nova versão"
git push
```

---

## 🎨 Paleta Visual

| Token | Cor | Uso |
|---|---|---|
| `--accent` | `#00b4ff` | Azul neon — orbits, glow, pills |
| `--accent2` | `#bf00ff` | Roxo — gradiente, segunda orbit |
| `--accent3` | `#6e00ff` | Roxo profundo — ambient glow |
| `--bg` | `#000005` | Fundo absoluto |
| `--text` | `#c8d8ff` | Texto principal |

---

## 🛠️ Tecnologias

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35+-red?style=flat-square&logo=streamlit)
![CSS3](https://img.shields.io/badge/CSS3-Animations-blueviolet?style=flat-square&logo=css3)
![GitHub](https://img.shields.io/badge/GitHub-Deploy-black?style=flat-square&logo=github)

---

## 📄 Licença

MIT © 2025 — Livre para uso e modificação.
