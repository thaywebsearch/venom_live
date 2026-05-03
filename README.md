# venom_live

📁 Estrutura do projeto:

/
├── app.py              ← Estrutura 1 (atualizado)
├── img_to_base64.py    ← Estrutura 2 (novo)
├── logo.png            ← Venom image
└── requirements.txt

🔬 Como a Estrutura 2 funciona — pipeline completo:

logo.png
   │
   ▼  file.read_bytes()
[bytes binários]  → b'\x89PNG\r\n\x1a\n...'
   │
   ▼  base64.b64encode()
[bytes Base64]    → b'iVBORw0KGgoAAAAN...'
   │
   ▼  .decode("utf-8")
[string Base64]   → 'iVBORw0KGgoAAAAN...'
   │
   ▼  embutida no HTML
src="data:image/png;base64,iVBORw0KGgo..."


