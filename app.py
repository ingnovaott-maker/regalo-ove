import streamlit as st

# Configuración visual
st.set_page_config(page_title="Trivia", page_icon="💖")

# Diseño con CSS para fondo de corazones y estilo romántico
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f3;
        background-image: url("https://www.transparenttextures.com/patterns/cuis-hearts.png");
    }
    .titulo {
        color: #c9184a;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .premio-box {
        background-color: white;
        padding: 25px;
        border-radius: 20px;
        border: 3px dashed #ff4d6d;
        text-align: center;
        box-shadow: 10px 10px 15px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de intentos
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0
if 'acerto' not in st.session_state:
    st.session_state.acerto = False

st.markdown("<h1 class='titulo'>✨ Una pregunta especial ✨</h1>", unsafe_allow_html=True)

# Imagen decorativa
st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=500&auto=format", use_container_width=True)

if not st.session_state.acerto:
    if st.session_state.intentos < 2:
        respuesta = st.text_input("¿Quién es la niña más linda?", placeholder="Escribe aquí...")
        
        if st.button("Enviar respuesta ❤️"):
            nombre_limpio = respuesta.strip().capitalize()
            if nombre_limpio in ["Thelma", "Thelmis","thelma","thelmis"]:
                st.session_state.acerto = True
                st.rerun()
            else:
                st.session_state.intentos += 1
                if st.session_state.intentos == 1:
                    st.warning("⚠️ Respuesta incorrecta... piénsalo bien, ¡te queda un solo intento!")
                else:
                    st.error("💔 Te quedaste sin intentos...")
    else:
        if st.button("Reintentar"):
            st.session_state.intentos = 0
            st.rerun()
else:
    # Pantalla de victoria
    st.balloons()
    st.snow()
    st.markdown("<h2 style='text-align: center; color: #ff4d6d;'>¡ACERTASTE! 😍</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div class="premio-box">
            <h2 style='color: #c9184a;'>🎁 ¡Te has ganado un premio!</h2>
            <p style='font-size: 1.3rem; color: #590d22;'>
                <b>Pide algo rico yo lo pago...</b> <br>
                Dime qué quieres comer y lo pedimos ahora mismo. 🍔🍕🍣
                Toma captura de pantalla y enviamela a whatsapp
            </p>
        </div>
    """, unsafe_allow_html=True)