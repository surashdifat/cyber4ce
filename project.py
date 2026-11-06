"""
═══════════════════════════════════════════
  CYBER4CE — Unified Cyber Security Suite
  Main Shell & Navigation
  Team: Abood, Sura, Estebraq & Ahmed
  ═══════════════════════════════════════════
"""

import streamlit as st
from datetime import datetime

# ═══ Page Configuration ═══
st.set_page_config(
    page_title="Cyber4ce | Cyber Security Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ═══ Load Design System CSS ═══
try:
    with open("design_system.css", "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
except FileNotFoundError:
    st.error("⚠️ design_system.css not found! Please make sure it's in the project root.")


# ═══════════════════════════════════════════
#  TOP BAR
# ═══════════════════════════════════════════
def render_top_bar():
    now = datetime.now().strftime("%Y-%m-%d | %H:%M:%S")
    st.markdown(f"""
    <div style="background: linear-gradient(90deg, #0F172A, #1E293B); 
                padding:14px 24px; border-radius:10px; 
                border:1px solid #334155; margin-bottom:20px;
                display:flex; justify-content:space-between; align-items:center;
                box-shadow: 0 4px 15px rgba(0,0,0,0.5);">
        <div style="color:#06B6D4; font-family:'Share Tech Mono', monospace; font-size:14px;">
            <span style="color:#EF4444;" class="blink">●</span> 
            &nbsp;SYSTEM ACTIVE | {now}
        </div>
        <div style="color:#E2E8F0; font-family:'Share Tech Mono', monospace; font-size:14px;">
            STATUS: <span style="color:#10B981; font-weight:bold;">SECURE 🛡️</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════
#  WELCOME PAGE
# ═══════════════════════════════════════════
def render_welcome():
    st.markdown("""
    <div style="text-align:center; padding:40px 20px 20px 20px;">
        <div style="font-family:'Orbitron', sans-serif; font-size:64px; font-weight:900; 
                    color:#06B6D4; text-shadow: 0 0 20px rgba(6,182,212,0.8), 0 0 40px rgba(6,182,212,0.4);
                    letter-spacing:6px; margin-bottom:10px;">
            CYBER<span style="color:#EF4444;">4</span>CE
        </div>
        <div style="font-family:'Share Tech Mono', monospace; font-size:18px; 
                    color:#94A3B8; letter-spacing:4px; margin-bottom:30px;">
            ⚡ CYBER SECURITY SUITE ⚡
        </div>
        <div style="font-family:'Share Tech Mono', monospace; font-size:15px; 
                    color:#E2E8F0; max-width:800px; margin:0 auto; line-height:1.8;">
            A unified cyber-defense platform offering four essential 
            security services — from password intelligence to breach monitoring. 
            Built by a team of four, for everyone's digital safety.
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin:20px 0;">
        <span style="color:#06B6D4; font-size:20px; letter-spacing:8px;">
            ─────── ◆ ───────
        </span>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("🛡️ SERVICES", "4", "Active")
    with col2:
        st.metric("👥 TEAM", "4 Members", "Dev Team")
    with col3:
        st.metric("🔒 ENCRYPTION", "AES-256", "Enabled")
    with col4:
        st.metric("🌐 STATUS", "ONLINE", "All Systems")

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; margin:30px 0 20px 0;">
        <h2 style="font-family:'Orbitron', sans-serif; color:#06B6D4; 
                   letter-spacing:4px; font-size:24px;">
            ▸ AVAILABLE SERVICES ◂
        </h2>
    </div>
    """, unsafe_allow_html=True)

    row1_col1, row1_col2 = st.columns(2)
    row2_col1, row2_col2 = st.columns(2)

    with row1_col1:
        st.markdown("""
        <div class="cyber-card slide-up">
            <div style="font-size:36px; margin-bottom:10px;">🔐</div>
            <h3 style="color:#06B6D4; font-family:'Orbitron', sans-serif; 
                       margin:0 0 10px 0; font-size:18px; letter-spacing:2px;">
                PASSWORD GENERATOR
            </h3>
            <p style="color:#94A3B8; font-size:13px; line-height:1.6; margin:0;">
                Generate military-grade passwords with a personal "salt" twist. 
                Real-time warnings for leaked credentials.
            </p>
            <div style="margin-top:15px;">
                <span class="cyber-badge badge-cyan">CRYPTOGRAPHY</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row1_col2:
        st.markdown("""
        <div class="cyber-card slide-up">
            <div style="font-size:36px; margin-bottom:10px;">💣</div>
            <h3 style="color:#EF4444; font-family:'Orbitron', sans-serif; 
                       margin:0 0 10px 0; font-size:18px; letter-spacing:2px;">
                SECURE SHARING
            </h3>
            <p style="color:#94A3B8; font-size:13px; line-height:1.6; margin:0;">
                Send encrypted messages that self-destruct after one view. 
                Zero storage, maximum privacy.
            </p>
            <div style="margin-top:15px;">
                <span class="cyber-badge badge-red">EPHEMERAL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    with row2_col1:
        st.markdown("""
        <div class="cyber-card slide-up">
            <div style="font-size:36px; margin-bottom:10px;">🎣</div>
            <h3 style="color:#F59E0B; font-family:'Orbitron', sans-serif; 
                       margin:0 0 10px 0; font-size:18px; letter-spacing:2px;">
                PHISHING SCANNER
            </h3>
            <p style="color:#94A3B8; font-size:13px; line-height:1.6; margin:0;">
                Analyze suspicious URLs for homograph attacks, bad SSL 
                certificates, and known phishing patterns.
            </p>
            <div style="margin-top:15px;">
                <span class="cyber-badge badge-orange">THREAT INTEL</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with row2_col2:
        st.markdown("""
        <div class="cyber-card slide-up">
            <div style="font-size:36px; margin-bottom:10px;">🛡️</div>
            <h3 style="color:#10B981; font-family:'Orbitron', sans-serif; 
                       margin:0 0 10px 0; font-size:18px; letter-spacing:2px;">
                PRIVACY SHIELD
            </h3>
            <p style="color:#94A3B8; font-size:13px; line-height:1.6; margin:0;">
                Clean your images and PDFs from hidden metadata (EXIF) 
                locally in your browser. Zero-Knowledge privacy.
            </p>
            <div style="margin-top:15px;">
                <span class="cyber-badge badge-green">ZERO-KNOWLEDGE</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; padding:20px; border-top:1px solid #1E293B; 
                margin-top:40px;">
        <div style="color:#64748B; font-family:'Share Tech Mono', monospace; font-size:12px;">
            ▸ CYBER4CE © 2026 · Built with 💙 by the Dev Team · 
            <span style="color:#06B6D4;">[4 SERVICES · 4 MINDS · 1 MISSION]</span>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ═══════════════════════════════════════════
#  SERVICE PAGES
# ═══════════════════════════════════════════

def render_password_generator():
    st.title("🔐 PASSWORD GENERATOR")
    st.markdown("### Smart Password Generation with Privacy Salt")
    st.markdown("---")
    st.info("🚧 **Service Under Development** — Owned by: **Estebraq**")
    st.markdown("""
    This service will:
    - Generate military-grade passwords
    - Add a personal 'salt' only you know
    - Check against leaked password databases
    - Give real-time security warnings
    """)


def render_secure_sharing():
    st.title("💣 SECURE SHARING")
    st.markdown("### Ephemeral Self-Destructing Messages")
    st.markdown("---")
    st.info("🚧 **Service Under Development** — Owned by: **Team Member 4**")
    st.markdown("""
    This service will:
    - Encrypt text/data with AES-256
    - Generate one-time view links
    - Auto-destroy after first view
    - Zero server-side storage
    """)


def render_phishing_scanner():
    try:
        from surapage import render_service
        render_service()
    except ImportError:
        st.warning("⚠️ **surapage.py not found.** Please add it to the project root.")
        st.markdown("""
        Once **Sura** delivers the file, place it as `surapage.py` in the project root,
        and this page will automatically load her service.
        """)
    except Exception as e:
        st.error(f"⚠️ Error loading Sura's service: {e}")


def render_privacy_shield():
    try:
        from abood import render_service as render_abood_service
        render_abood_service()
    except ImportError:
        st.warning("⚠️ **abood.py not found.** Please add it to the project root.")
    except Exception as e:
        st.error(f"⚠️ Error loading Abood's service: {e}")


# ═══════════════════════════════════════════
#  MAIN ROUTER
# ═══════════════════════════════════════════
render_top_bar()

with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:10px 0 20px 0;">
        <div style="font-family:'Orbitron', sans-serif; font-size:22px; font-weight:900;
                    color:#06B6D4; text-shadow: 0 0 15px rgba(6,182,212,0.7);
                    letter-spacing:3px;">
            CYBER<span style="color:#EF4444;">4</span>CE
        </div>
        <div style="font-family:'Share Tech Mono', monospace; font-size:10px;
                    color:#64748B; letter-spacing:3px; margin-top:5px;">
            ◆ SECURITY SUITE ◆
        </div>
    </div>
    <hr style="border-color:#1E293B; margin:10px 0;">
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="font-family:'Share Tech Mono', monospace; font-size:11px;
                color:#64748B; letter-spacing:2px; margin-bottom:10px;">
        ▸ NAVIGATION
    </div>
    """, unsafe_allow_html=True)

    page_selection = st.radio(
        "Navigation",
        [
            "🏠 Welcome",
            "🛡️ Privacy Shield",
            "💣 Secure Sharing",
            "🔐 Password Generator",
            "🎣 Phishing Scanner"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<hr style='border-color:#1E293B; margin:20px 0;'>", unsafe_allow_html=True)

    st.markdown("""
    <div style="text-align:center; font-family:'Share Tech Mono', monospace; 
                font-size:10px; color:#64748B; line-height:1.8;">
        <div style="color:#06B6D4; margin-bottom:5px;">▸ TEAM MEMBERS</div>
        Abood · Sura · Estebraq · Ahmed
        <br><br>
        <div style="color:#10B981;">
            <span class="blink">●</span> ALL SYSTEMS ONLINE
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─── Router Logic ───
if page_selection == "🏠 Welcome":
    render_welcome()
elif page_selection == "🔐 Password Generator":
    render_password_generator()
elif page_selection == "💣 Secure Sharing":
    render_secure_sharing()
elif page_selection == "🎣 Phishing Scanner":
    render_phishing_scanner()
elif page_selection == "🛡️ Privacy Shield":
    render_privacy_shield()
