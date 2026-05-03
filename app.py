"""
╔══════════════════════════════════════════════════════════════════╗
║         ESTRUTURA 2 · IMG → BASE64 CONVERTER                    ║
║         Técnica de conversão de imagem para Base64              ║
║         Integração com app.py via CSS Injection + HTML Render   ║
╚══════════════════════════════════════════════════════════════════╝

COMO FUNCIONA:
──────────────
  1. A imagem (PNG/JPG/WEBP/GIF) é lida como bytes binários
  2. Os bytes são codificados em Base64 (RFC 4648)
  3. A string resultante é embutida diretamente no HTML como URI
  4. O navegador decodifica e renderiza sem depender de arquivos externos

VANTAGEM:
─────────
  ✔ Zero dependência de servidor de arquivos estáticos
  ✔ Funciona 100% dentro do Streamlit (st.markdown unsafe_allow_html)
  ✔ A imagem viaja embutida no próprio HTML
"""

import base64
import os
import sys
from pathlib import Path


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  FUNÇÃO PRINCIPAL — usada dentro do app.py
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def img_to_base64(path: str) -> str:
    """
    Converte qualquer imagem local para uma string Base64.

    Parâmetros:
        path (str): Caminho relativo ou absoluto para o arquivo de imagem.
                    Suporta: .png · .jpg · .jpeg · .webp · .gif · .svg

    Retorna:
        str: String Base64 pura (sem prefixo data URI).
             Pronta para ser embutida em <img src="data:image/...;base64,{string}">

    Uso dentro do app.py:
        logo_b64 = img_to_base64("logo.png")
        html = f'<img src="data:image/png;base64,{logo_b64}" />'

    Exceções:
        FileNotFoundError : arquivo não encontrado no caminho informado.
        ValueError        : extensão de arquivo não suportada.
    """

    SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg"}

    file = Path(path)

    # ── Validações ──────────────────────────────────────────────
    if not file.exists():
        raise FileNotFoundError(
            f"\n  ✖ Arquivo não encontrado: '{path}'\n"
            f"  → Verifique se logo.png está na mesma pasta que app.py\n"
        )

    if file.suffix.lower() not in SUPPORTED:
        raise ValueError(
            f"\n  ✖ Extensão '{file.suffix}' não suportada.\n"
            f"  → Use: {', '.join(SUPPORTED)}\n"
        )

    # ── Leitura binária + codificação ───────────────────────────
    raw_bytes: bytes = file.read_bytes()          # lê os bytes brutos
    b64_bytes: bytes = base64.b64encode(raw_bytes) # codifica em Base64
    b64_str:   str   = b64_bytes.decode("utf-8")   # converte para string

    return b64_str


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  FUNÇÃO AUXILIAR — detecta o mime type automaticamente
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_mime_type(path: str) -> str:
    """
    Retorna o MIME type correto com base na extensão do arquivo.

    Parâmetros:
        path (str): Caminho ou nome do arquivo de imagem.

    Retorna:
        str: MIME type (ex: "image/png", "image/jpeg", "image/webp")
    """

    MIME_MAP = {
        ".png":  "image/png",
        ".jpg":  "image/jpeg",
        ".jpeg": "image/jpeg",
        ".webp": "image/webp",
        ".gif":  "image/gif",
        ".svg":  "image/svg+xml",
    }

    ext = Path(path).suffix.lower()
    return MIME_MAP.get(ext, "image/png")  # fallback: png


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  FUNÇÃO COMPLETA — retorna o data URI pronto para o <img src="">
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def img_to_data_uri(path: str) -> str:
    """
    Converte imagem para Data URI completo.
    Formato: data:{mime};base64,{dados}

    Uso direto no HTML:
        uri = img_to_data_uri("logo.png")
        html = f'<img src="{uri}" />'

    Isto elimina qualquer referência a arquivo externo —
    a imagem fica 100% embutida no HTML gerado.
    """

    mime   = get_mime_type(path)
    b64    = img_to_base64(path)
    return f"data:{mime};base64,{b64}"


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  DEMONSTRAÇÃO — como o app.py usa esta técnica
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DEMO_TEMPLATE = '''
# ── Trecho do app.py (Estrutura 1) que usa a conversão ────────────

import streamlit as st
from img_to_base64 import img_to_base64   # ← importa desta Estrutura 2

# Converte logo.png → string Base64
logo_b64 = img_to_base64("logo.png")

# Injeta no HTML com CSS Injection
HTML = f"""
<div class="mv-wrapper">
  <img
    class="mv-logo"
    src="data:image/png;base64,{logo_b64}"
    alt="Logo Animado"
  />
</div>
"""

st.markdown(CSS, unsafe_allow_html=True)   # injeta os estilos
st.markdown(HTML, unsafe_allow_html=True)  # renderiza o HTML com a imagem
'''


# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#  EXECUÇÃO DIRETA — teste via terminal
#  python img_to_base64.py logo.png
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if __name__ == "__main__":

    print("\n" + "═" * 60)
    print("  ESTRUTURA 2 · Conversor IMG → Base64")
    print("═" * 60)

    # Usa argumento CLI ou 'logo.png' como padrão
    target = sys.argv[1] if len(sys.argv) > 1 else "logo.png"

    print(f"\n  Arquivo alvo : {target}")

    try:
        b64    = img_to_base64(target)
        mime   = get_mime_type(target)
        uri    = img_to_data_uri(target)
        size   = os.path.getsize(target)
        b64_kb = len(b64) / 1024

        print(f"  MIME type    : {mime}")
        print(f"  Tamanho orig : {size / 1024:.1f} KB")
        print(f"  Tamanho B64  : {b64_kb:.1f} KB  (~{(b64_kb/size*1024-1)*100:.0f}% overhead)")
        print(f"\n  Data URI     : {uri[:80]}...")
        print(f"\n  ✔ Pronto para usar no app.py como:")
        print(f'    src="data:{mime};base64,{{logo_b64}}"')
        print("\n" + "─" * 60)
        print("\n  COMO O APP.PY USA ESTA TÉCNICA:")
        print(DEMO_TEMPLATE)

    except (FileNotFoundError, ValueError) as e:
        print(e)
        sys.exit(1)
