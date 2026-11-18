def situacao(media, frequencia):
    """Situação final do aluno na disciplina.

    media: nota de 0.0 a 10.0, com uma casa decimal.
    frequencia: porcentagem de presença, inteiro de 0 a 100.
    """
    if media < 0.0 or media > 10.0:
        raise ValueError(f"média inválida: {media}")
    if frequencia < 0 or frequencia > 100:
        raise ValueError(f"frequência inválida: {frequencia}")
    if frequencia < 75:
        return "REPROVADO_POR_FALTA"
    if media >= 7.0:
        return "APROVADO"
    if media >= 4.0:
        return "RECUPERACAO"
    return "REPROVADO"
