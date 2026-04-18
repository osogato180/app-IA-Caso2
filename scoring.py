def calcular_score(ingresos, monto, historial):
    score = 0

    # Evaluación de ingresos
    if ingresos > 3000:
        score += 40
    elif ingresos >= 1500:
        score += 25
    else:
        score += 10

    # Evaluación de historial crediticio
    if historial == "Bueno":
        score += 40
    elif historial == "Regular":
        score += 20
    else:
        score += 0

    # Evaluación del monto solicitado
    if monto <= ingresos * 12 * 0.3:
        score += 20

    return score


def decision_credito(score):
    if score >= 70:
        return "Aprobado"
    elif score >= 50:
        return "Observado"
    else:
        return "Rechazado"