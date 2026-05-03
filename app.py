import streamlit as st
import base64
from pathlib import Path

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Venom · Imagem em Movimento",
    page_icon="🩸",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ── Helper: encode local image to base64 ──────────────────────────────────────
def img_to_base64(path: str) -> str:
    return base64.b64encode(Path(path).read_bytes()).decode()

logo_b64 = img_to_base64("logo.png")

# ── CSS Injection ──────────────────────────────────────────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@300;400;600&display=swap');

:root {
  --bg:      #000005;
  --accent:  #00b4ff;
  --accent2: #bf00ff;
  --accent3: #6e00ff;
  --text:    #c8d8ff;
  --muted:   #3a3a5c;
}

/* ── hide streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

html, body, [data-testid="stAppViewContainer"] {
  background: var(--bg) !important;
  font-family: 'Rajdhani', sans-serif;
  color: var(--text);
  overflow-x: hidden;
}

/* ── scanline overlay ── */
[data-testid="stAppViewContainer"]::before {
  content: "";
  position: fixed; inset: 0;
  background: repeating-linear-gradient(
    to bottom,
    transparent,
    transparent 3px,
    rgba(0,180,255,.018) 3px,
    rgba(0,180,255,.018) 4px
  );
  pointer-events: none;
  z-index: 9998;
}

/* ── main wrapper ── */
.mv-wrapper {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 60px 24px;
  position: relative;
  overflow: hidden;
}

/* ── deep radial glow background ── */
.mv-wrapper::after {
  content: "";
  position: fixed;
  width: 700px; height: 700px;
  border-radius: 50%;
  background: radial-gradient(
    circle,
    rgba(110,0,255,.12) 0%,
    rgba(0,180,255,.06) 35%,
    transparent 70%
  );
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  pointer-events: none;
  animation: ambient-pulse 7s ease-in-out infinite;
}

@keyframes ambient-pulse {
  0%,100% { opacity:.7; transform: translate(-50%,-50%) scale(1);    }
  50%      { opacity:1;  transform: translate(-50%,-50%) scale(1.18); }
}

/* ── eyebrow ── */
.mv-eyebrow {
  font-family: 'Rajdhani', sans-serif;
  font-size: 11px;
  font-weight: 300;
  letter-spacing: .4em;
  text-transform: uppercase;
  color: var(--muted);
  margin-bottom: 48px;
  animation: fade-down .8s ease both;
}

/* ── logo container ── */
.mv-logo-wrap {
  position: relative;
  width: 320px; height: 320px;
  display: flex; align-items: center; justify-content: center;
  animation: fade-up 1s ease .2s both;
}

/* rotating outer ring — blue */
.mv-logo-wrap::before {
  content: "";
  position: absolute; inset: -18px;
  border-radius: 50%;
  border: 1px solid rgba(0,180,255,.25);
  border-top-color: rgba(0,180,255,.8);
  border-right-color: rgba(191,0,255,.5);
  animation: spin 10s linear infinite;
  filter: blur(.4px);
}

/* counter-rotating ring — purple */
.mv-logo-wrap::after {
  content: "";
  position: absolute; inset: -32px;
  border-radius: 50%;
  border: 1px dashed rgba(191,0,255,.2);
  border-bottom-color: rgba(191,0,255,.6);
  animation: spin 16s linear infinite reverse;
}

@keyframes spin { to { transform: rotate(360deg); } }

/* ── orbit dot ── */
.mv-orbit {
  position: absolute; inset: -18px;
  border-radius: 50%;
  animation: spin 10s linear infinite;
  pointer-events: none;
}
.mv-orbit-dot {
  position: absolute;
  top: 0; left: 50%; transform: translateX(-50%);
  width: 8px; height: 8px; border-radius: 50%;
  background: var(--accent);
  box-shadow: 0 0 12px var(--accent), 0 0 28px var(--accent);
}

/* second orbit dot (purple, counter) */
.mv-orbit2 {
  position: absolute; inset: -32px;
  border-radius: 50%;
  animation: spin 16s linear infinite reverse;
  pointer-events: none;
}
.mv-orbit-dot2 {
  position: absolute;
  bottom: 0; left: 50%; transform: translateX(-50%);
  width: 6px; height: 6px; border-radius: 50%;
  background: var(--accent2);
  box-shadow: 0 0 10px var(--accent2), 0 0 22px var(--accent2);
}

/* ── logo image ── */
.mv-logo {
  width: 300px; height: 300px;
  object-fit: cover;
  border-radius: 50%;
  animation: venom-float 6s ease-in-out infinite,
             venom-glow  4s ease-in-out infinite;
}

@keyframes venom-float {
  0%,100% { transform: translateY(0px)   scale(1);    }
  30%      { transform: translateY(-14px) scale(1.02); }
  60%      { transform: translateY(-7px)  scale(.99);  }
}

@keyframes venom-glow {
  0%,100% {
    filter: drop-shadow(0 0 20px rgba(0,180,255,.5))
            drop-shadow(0 0 6px  rgba(191,0,255,.3));
  }
  50% {
    filter: drop-shadow(0 0 45px rgba(0,180,255,.9))
            drop-shadow(0 0 20px rgba(191,0,255,.6))
            drop-shadow(0 0 60px rgba(110,0,255,.35));
  }
}

/* ── title ── */
.mv-title {
  font-family: 'Bebas Neue', sans-serif;
  font-size: clamp(3rem, 8vw, 5.5rem);
  letter-spacing: .08em;
  line-height: 1;
  text-align: center;
  margin-top: 48px;
  background: linear-gradient(135deg, var(--accent) 0%, #ffffff 40%, var(--accent2) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: fade-up 1s ease .4s both, flicker 8s step-end infinite 2s;
}

@keyframes flicker {
  0%,96%,100% { opacity:1;  }
  97%          { opacity:.7; }
  98%          { opacity:1;  }
  99%          { opacity:.4; }
}

/* ── subtitle ── */
.mv-sub {
  font-size: 14px;
  font-weight: 300;
  letter-spacing: .08em;
  color: var(--muted);
  text-align: center;
  max-width: 360px;
  line-height: 1.8;
  margin-top: 14px;
  animation: fade-up 1s ease .6s both;
}

/* ── pills ── */
.mv-pills {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
  justify-content: center;
  margin-top: 36px;
  animation: fade-up 1s ease .8s both;
}

.mv-pill {
  padding: 5px 18px;
  border-radius: 4px;
  font-size: 10px;
  letter-spacing: .18em;
  text-transform: uppercase;
  font-weight: 600;
  border: 1px solid rgba(0,180,255,.2);
  color: rgba(0,180,255,.6);
  background: rgba(0,180,255,.04);
  transition: all .3s ease;
  position: relative;
  overflow: hidden;
}

.mv-pill::before {
  content: "";
  position: absolute; inset: 0;
  background: linear-gradient(90deg, transparent, rgba(0,180,255,.08), transparent);
  transform: translateX(-100%);
  transition: transform .5s ease;
}

.mv-pill:hover::before { transform: translateX(100%); }

.mv-pill:hover {
  border-color: var(--accent);
  color: var(--accent);
  box-shadow: 0 0 14px rgba(0,180,255,.2), inset 0 0 8px rgba(0,180,255,.05);
  cursor: default;
}

/* ── drip bar ── */
.mv-drip {
  width: 2px;
  height: 70px;
  background: linear-gradient(to bottom, var(--accent), var(--accent2), transparent);
  margin-top: 44px;
  border-radius: 2px;
  box-shadow: 0 0 8px var(--accent);
  animation: fade-up 1s ease 1s both, drip-pulse 3s ease-in-out infinite 1s;
}

@keyframes drip-pulse {
  0%,100% { opacity:.5; height:70px; }
  50%      { opacity:1;  height:90px; box-shadow: 0 0 16px var(--accent), 0 0 30px var(--accent2); }
}

/* ── shared keyframes ── */
@keyframes fade-up {
  from { opacity:0; transform: translateY(28px); }
  to   { opacity:1; transform: translateY(0);    }
}
@keyframes fade-down {
  from { opacity:0; transform: translateY(-18px); }
  to   { opacity:1; transform: translateY(0);      }
}
</style>
"""

# ── HTML ───────────────────────────────────────────────────────────────────────
HTML = f"""
<div class="mv-wrapper">

  <p class="mv-eyebrow">⬡ &nbsp; sistema · ativo &nbsp; ⬡</p>

  <div class="mv-logo-wrap">
    <div class="mv-orbit"><div class="mv-orbit-dot"></div></div>
    <div class="mv-orbit2"><div class="mv-orbit-dot2"></div></div>
    <img class="mv-logo"
         src="data:image/png;base64,{logo_b64}"
         alt="Venom Logo" />
  </div>

  <h1 class="mv-title">Imagem em<br>Movimento</h1>

  <p class="mv-sub">
    CSS Injection &nbsp;·&nbsp; HTML Render &nbsp;·&nbsp; Streamlit<br>
    Energia simbiótica · Sempre em movimento.
  </p>

  <div class="mv-pills">
    <div class="mv-pill">Streamlit</div>
    <div class="mv-pill">CSS Injection</div>
    <div class="mv-pill">HTML Render</div>
    <div class="mv-pill">Neon FX</div>
  </div>

  <div class="mv-drip"></div>

</div>
"""

# ── Render ─────────────────────────────────────────────────────────────────────
st.markdown(CSS, unsafe_allow_html=True)
st.markdown(HTML, unsafe_allow_html=True)
