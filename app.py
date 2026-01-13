import streamlit as st

# Configuración de página
st.set_page_config(page_title="Para la más linda", page_icon="💖")

# CSS que respeta el tema del sistema (Claro/Oscuro)
st.markdown("""
    <style>
    /* Fondo con corazones sutiles */
    .stApp {
        background-image: url("https://www.transparenttextures.com/patterns/cuis-hearts.png");
    }
    
    /* Contenedor adaptativo para el premio */
    .premio-box {
        padding: 25px;
        border-radius: 20px;
        border: 2px solid #ff4d6d;
        text-align: center;
        background-color: rgba(255, 77, 109, 0.1);
        margin-top: 20px;
    }
    
    /* Título que resalta en ambos temas */
    .titulo-romantico {
        text-align: center;
        color: #ff4d6d;
        font-family: 'Georgia', serif;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Lógica de estados
if 'intentos' not in st.session_state:
    st.session_state.intentos = 0
if 'acerto' not in st.session_state:
    st.session_state.acerto = False

st.markdown("<h1 class='titulo-romantico'>✨ Una pregunta para ti ✨</h1>", unsafe_allow_html=True)

# Imagen central
st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=500&auto=format", use_container_width=True)

if not st.session_state.acerto:
    if st.session_state.intentos < 2:
        # El widget de texto de Streamlit cambia de color automáticamente según el tema del móvil
        respuesta = st.text_input("¿Quién es la niña más linda?", placeholder="Escribe tu respuesta aquí...")
        
        if st.button("Enviar respuesta ❤️"):
            nombre_limpio = respuesta.strip().capitalize()
            if nombre_limpio in ["Thelma", "Thelmis","thelma","Thelmis"]:
                st.session_state.acerto = True
                st.rerun()
            else:
                st.session_state.intentos += 1
                if st.session_state.intentos == 1:
                    st.warning("⚠️ ¡Incorrecto! Piénsalo bien... te queda un solo intento.")
                else:
                    st.error("💔 Se agotaron los intentos...")
    else:
        if st.button("Intentar de nuevo 🔄"):
            st.session_state.intentos = 0
            st.rerun()
else:
    # Efectos visuales de celebración
    st.balloons()
    st.snow()
    
    st.markdown("<h2 style='text-align: center;'>¡SÍ! 😍</h2>", unsafe_allow_html=True)
    
    # Cuadro de premio
    st.markdown("""
        <div class="premio-box">
            <h2 style='color: #ff4d6d;'>🎁 ¡TE HAS GANADO UN PREMIO!</h2>
            <p style='font-size: 1.2rem;'>
                Eres la niña más linda. Pide algo rico, <b>yo lo pago.</b> 🍔🍕 Sushi, pizza... ¡tú eliges!
                Mandame captura al whatsapp
            </p>
        </div>
    """, unsafe_allow_html=True)
