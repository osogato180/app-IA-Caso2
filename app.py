import streamlit as st
from db import get_db
from scoring import calcular_score, decision_credito
from datetime import datetime

st.set_page_config(page_title="Aprobación de Créditos - BRA", layout="centered")

st.title("🏦 Banco Regional Andino")
st.subheader("Sistema inteligente de aprobación de créditos")

st.write(
    "Este sistema permite evaluar solicitudes de crédito en minutos "
    "mediante un modelo automatizado de scoring crediticio."
)

# Formulario
with st.form("form_credito"):
    dni = st.text_input("DNI")
    ingresos = st.number_input("Ingresos mensuales (S/.)", min_value=0)
    monto = st.number_input("Monto solicitado (S/.)", min_value=0)
    plazo = st.selectbox("Plazo (meses)", [6, 12, 24, 36])
    historial = st.selectbox("Historial crediticio", ["Bueno", "Regular", "Malo"])
    
    submitted = st.form_submit_button("Evaluar crédito")

if submitted:
    score = calcular_score(ingresos, monto, historial)
    resultado = decision_credito(score)

    st.markdown("---")
    st.subheader("📊 Resultado de la evaluación")
    st.write(f"**Score crediticio:** {score}")
    st.write(f"**Resultado:** {resultado}")

    # Guardar en MongoDB
    db = get_db()
    db.solicitudes_credito.insert_one({
        "dni": dni,
        "ingresos": ingresos,
        "monto": monto,
        "plazo": plazo,
        "historial": historial,
        "score": score,
        "resultado": resultado,
        "fecha": datetime.now()
    })

    st.success("Solicitud registrada correctamente en el sistema.")