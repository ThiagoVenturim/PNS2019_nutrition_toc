# =============================================================================
# SELEÇÃO DE VARIÁVEIS — PNS 2019
# Estudo: TOC e Hábitos Alimentares (faixa etária 30–59 anos)
# =============================================================================

# ─── RENOMEAÇÕES ──────────────────────────────────────────────────────────────
colunas_renomeadas = {
    "C008"   : "Idade",     # Idade em anos completos (calculada pelo DMC)
    "Q11009" : "TOC",       # Diagnóstico autorreferido de TOC (1=Sim / 2=Não)
    "P00104" : "Peso",      # Peso autorreferido em quilogramas
    "P00404" : "Altura",    # Altura autorreferida em centímetros
    "V0001"  : "Estado",    # Código da Unidade da Federação (11=RO … 53=DF)
}

# ─── MAPEAMENTOS GEOGRÁFICOS ──────────────────────────────────────────────────
map_estados = {
    "11": "Rondônia",         "12": "Acre",
    "13": "Amazonas",         "14": "Roraima",
    "15": "Pará",             "16": "Amapá",
    "17": "Tocantins",        "21": "Maranhão",
    "22": "Piauí",            "23": "Ceará",
    "24": "Rio Grande do Norte", "25": "Paraíba",
    "26": "Pernambuco",       "27": "Alagoas",
    "28": "Sergipe",          "29": "Bahia",
    "31": "Minas Gerais",     "32": "Espírito Santo",
    "33": "Rio de Janeiro",   "35": "São Paulo",
    "41": "Paraná",           "42": "Santa Catarina",
    "43": "Rio Grande do Sul","50": "Mato Grosso do Sul",
    "51": "Mato Grosso",      "52": "Goiás",
    "53": "Distrito Federal",
}

map_regiao = {
    "Rondônia": "Norte",     "Acre": "Norte",
    "Amazonas": "Norte",     "Roraima": "Norte",
    "Pará": "Norte",         "Amapá": "Norte",
    "Tocantins": "Norte",    "Maranhão": "Nordeste",
    "Piauí": "Nordeste",     "Ceará": "Nordeste",
    "Rio Grande do Norte": "Nordeste", "Paraíba": "Nordeste",
    "Pernambuco": "Nordeste","Alagoas": "Nordeste",
    "Sergipe": "Nordeste",   "Bahia": "Nordeste",
    "Minas Gerais": "Sudeste","Espírito Santo": "Sudeste",
    "Rio de Janeiro": "Sudeste","São Paulo": "Sudeste",
    "Paraná": "Sul",         "Santa Catarina": "Sul",
    "Rio Grande do Sul": "Sul","Mato Grosso do Sul": "Centro-Oeste",
    "Mato Grosso": "Centro-Oeste","Goiás": "Centro-Oeste",
    "Distrito Federal": "Centro-Oeste",
}

# =============================================================================
# 1. HIGIENE DO SONO  |  Módulo N  |  Qualitativa Ordinal
# =============================================================================
cols_sono = [
    "N010",     # Frequência de problemas no sono nas últimas 2 semanas
                # (1=Nenhum dia | 2=< metade dos dias | 3=> metade | 4=Quase todos os dias)
]

# =============================================================================
# 2. SINTOMAS PSICOLÓGICOS (PHQ-9 adaptado)  |  Módulo N  |  Qualitativa Ordinal
# Captura sofrimento psicológico dimensional além do diagnóstico formal
# =============================================================================
cols_sintomas_psicologicos = [
    "N011",     # Frequência de cansaço / falta de energia nas últimas 2 semanas
    "N012",     # Frequência de pouco interesse ou prazer em fazer as coisas
    "N013",     # Frequência de dificuldade para se concentrar nas atividades
    "N014",     # Frequência de problemas na alimentação (falta ou excesso de apetite)
    "N015",     # Frequência de lentidão para se movimentar/falar ou agitação excessiva
    "N016",     # Frequência de sentir-se deprimido, para baixo ou sem perspectiva
    "N017",     # Frequência de sentir-se fracasso ou que decepcionou a família
    "N018",     # Frequência de pensamentos de se ferir ou de que seria melhor estar morto
]

# =============================================================================
# 3. CONSUMO DE ÁLCOOL E TABACO  |  Módulo P  |  Qualitativa Nominal / Ordinal
# AJUSTE: Removidas colunas de tipo específico de produto do tabaco (NaN >95%)
#         Mantidas apenas as variáveis-síntese de frequência e quantidade
# =============================================================================
cols_drogas = [
    # — ÁLCOOL —
    "P027",     # Frequência de consumo de álcool (1=nunca | 2=<1x/mês | 3=≥1x/mês)
    "P02801",   # Dias por semana que consome bebida alcoólica
    "P029",     # Número de doses consumidas no dia em que bebe

    # — TABACO — (variáveis-síntese; detalhamento por tipo removido)
    "P050",     # Fuma atualmente? (1=sim diariamente | 2=sim menos | 3=não fuma)
    "P051",     # No passado fumou diariamente? (apenas para quem não fuma mais)
    "P052",     # No passado fumou algum produto do tabaco? (filtro ex-fumante)
    "P058",     # Quantidade média de cigarros industrializados/dia (ex-fumantes)
    "P05801",   # Quantidade de cigarros/semana (ex-fumantes que fumavam semanalmente)

    # REMOVIDAS (muito julgamento + NaN >95%):
    # P05401–P05422 → quantidades por tipo específico (cachimbo, charuto, narguilé etc.)
    # P053, P055, P056, P057, P059–P063, P06302 → tentativas de parar de fumar
    # P067, P06701 → tabaco sem fumaça (rapé, fumo de mascar)
    # P067a → cigarro eletrônico
    # P068–P07201 → propaganda e advertências de cigarro
]

# =============================================================================
# 4. ATIVIDADE FÍSICA  |  Módulo P  |  Qualitativa Nominal / Ordinal
# AJUSTE: Removidas colunas de minutagem detalhada de deslocamento (muito julgamento)
#         Mantido o núcleo de prática, frequência e tipo
# =============================================================================
cols_atividade = [
    "P034",     # Praticou exercício físico ou esporte nos últimos 12 meses? (1=Sim | 2=Não)
    "P035",     # Dias por semana que pratica exercício físico ou esporte
    "P036",     # Tipo de exercício praticado com maior frequência (código de atividade)
    "P03701",   # Horas de duração do exercício no dia em que pratica
    "P03702",   # Minutos de duração do exercício no dia em que pratica

    # Atividade no trabalho
    "P038",     # Anda bastante a pé no trabalho? (1=Sim | 2=Não)
    "P039",     # Faz faxina pesada ou carrega peso no trabalho? (1=Sim | 2=Não)
    "P03904",   # Dias por semana com atividade física intensa no trabalho

    # REMOVIDAS (muito julgamento — granularidade excessiva para o objetivo):
    # P03905, P03906 → horas/minutos exatos de atividade no trabalho
    # P040, P04001   → faz trajeto a pé/bicicleta para o trabalho e dias/semana
    # P04101, P04102 → horas/minutos do trajeto a pé/bicicleta para o trabalho
]

# =============================================================================
# 5. DIETA E ALIMENTAÇÃO  |  Módulo P  |  Qualitativa Nominal / Ordinal
# Núcleo principal do estudo — MANTIDAS TODAS as variáveis
# =============================================================================

# 5a. Consumo ontem — alimentos naturais/básicos
cols_dieta_naturais_ontem = [
    "P00601",   # Consumiu arroz, macarrão, polenta, cuscuz ou milho verde ontem? (1=Sim | 2=Não)
    "P00602",   # Consumiu batata, mandioca, cará ou inhame ontem?
    "P00603",   # Consumiu feijão, ervilha, lentilha ou grão-de-bico ontem?
    "P00604",   # Consumiu carne de boi, porco, frango ou peixe ontem?
    "P00605",   # Consumiu ovo (frito, cozido ou mexido) ontem?
    "P00607",   # Consumiu alface, couve, brócolis, agrião ou espinafre ontem?
    "P00608",   # Consumiu abóbora, cenoura, batata-doce ou quiabo ontem?
    "P00609",   # Consumiu tomate, pepino, abobrinha, berinjela, chuchu ou beterraba ontem?
    "P00610",   # Consumiu mamão, manga, melão amarelo ou pequi ontem?
    "P00611",   # Consumiu laranja, banana, maçã ou abacaxi ontem?
    "P00612",   # Consumiu leite ontem?
    "P00613",   # Consumiu amendoim, castanha de caju ou castanha do Brasil ontem?
]

# 5b. Consumo ontem — ultraprocessados e bebidas industriais
cols_dieta_ultraprocessados_ontem = [
    "P00614",   # Consumiu refrigerante ontem?
    "P00615",   # Consumiu suco de caixinha/lata ou refresco em pó ontem?
    "P00616",   # Consumiu bebida achocolatada ou iogurte com sabor ontem?
    "P00617",   # Consumiu salgadinho de pacote ou biscoito salgado ontem?
    "P00618",   # Consumiu biscoito doce, recheado ou bolo de pacote ontem?
    "P00619",   # Consumiu sorvete, chocolate, gelatina ou sobremesa industrial ontem?
    "P00620",   # Consumiu salsicha, linguiça, mortadela ou presunto ontem?
    "P00621",   # Consumiu pão de forma, cachorro-quente ou hambúrguer ontem?
    "P00622",   # Consumiu margarina, maionese, ketchup ou molhos industrializados ontem?
    "P00623",   # Consumiu macarrão instantâneo, sopa de pacote ou prato congelado ontem?
]

# 5c. Frequência habitual de consumo de alimentos (dias/semana)
cols_dieta_frequencia = [
    "P006",     # Dias/semana que costuma comer feijão (0=nunca … 7 dias)
    "P00901",   # Dias/semana que come verdura ou legume (exceto batata/mandioca)
    "P01001",   # Vezes/dia que come verdura ou legume (se ≥5 dias/semana)
    "P01101",   # Dias/semana que come carne vermelha (boi, porco, cabrito etc.)
    "P013",     # Dias/semana que come frango ou galinha
    "P015",     # Dias/semana que come peixe
    "P018",     # Dias/semana que come frutas
    "P019",     # Vezes/dia que come frutas (se ≥5 dias/semana)
    "P02501",   # Dias/semana que come alimentos doces (biscoito recheado, chocolate etc.)
    "P02601",   # Percepção do próprio consumo de sal (1=muito alto … 5=muito baixo)
    "P02602",   # Dias/semana que substitui almoço por lanche rápido (sanduíche, pizza etc.)
]

# 5d. Frequência habitual de consumo de bebidas (dias/semana)
cols_dieta_bebidas = [
    "P01601",   # Dias/semana que toma suco de fruta natural (inclui polpa congelada)
    "P02001",   # Dias/semana que toma suco de caixinha/lata ou refresco em pó
    "P02101",   # Tipo de suco industrializado (1=diet/light/zero | 2=normal | 3=ambos)
    "P02002",   # Dias/semana que toma refrigerante
    "P02102",   # Tipo de refrigerante (1=diet/light/zero | 2=normal | 3=ambos)
    "P023",     # Dias/semana que toma leite de origem animal (vaca, cabra, búfala)
    "P02401",   # Tipo de leite (1=desnatado/semidesnatado | 2=integral | 3=ambos)
]

# Agrupamento geral de dieta (para uso nos pipelines)
cols_dieta = (
    cols_dieta_naturais_ontem
    + cols_dieta_ultraprocessados_ontem
    + cols_dieta_frequencia
    + cols_dieta_bebidas
)

# =============================================================================
# 6. DEFICIÊNCIAS  |  Módulo G  |  Qualitativa Ordinal / Nominal
# AJUSTE: Removidas ~45 colunas auxiliares com NaN >95% (aparelhos, SUS, órteses)
#         Mantidas apenas as colunas de dificuldade funcional e filtros de triagem
# =============================================================================
cols_deficiencia = [
    # — Visão —
    "G032",     # Usa óculos ou aparelho de auxílio para visão? (filtro de triagem)
    "G046",     # Dificuldade de enxergar COM correção (1=Não conseg. … 4=Sem dific.)
    "G047",     # Dificuldade de enxergar SEM correção (1=Não conseg. … 4=Sem dific.)

    # — Audição —
    "G058",     # Dificuldade de ouvir SEM aparelho (1=Não conseg. … 4=Sem dific.)
    "G05801",   # Sabe usar LIBRAS? (1=Sim | 2=Não)

    # — Locomoção —
    "G059",     # Usa aparelho de auxílio para locomoção? (filtro de triagem)
    "G071",     # Dificuldade de caminhar/subir degraus SEM apoio
    "G072",     # Usa aparelho de auxílio para membros superiores? (filtro)
    "G081",     # Dificuldade de levantar objeto da cintura até os olhos SEM apoio
    "G082",     # Dificuldade de pegar objetos pequenos SEM apoio
    "G083",     # Dificuldade por limitação MENTAL/INTELECTUAL (ativ. habituais)
                # (1=Não conseg. | 2=Grande dific. | 3=Pequena dific. | 4=Sem dific.)

    # REMOVIDAS (muito julgamento + NaN >95%):
    # G033–G045 → modelos específicos de óculos, lente, bengala, cão-guia (SUS ou não)
    # G048–G057 → modelos de aparelhos auditivos e implantes (SUS ou não)
    # G060–G070 → tipos de cadeira de rodas, muletas, próteses de locomoção (SUS ou não)
    # G073–G080 → próteses de membros superiores (SUS ou não)
    # G084–G086 → reabilitação e acesso a cuidados
]

# =============================================================================
# 7. GRAVIDEZ  |  Módulo S / P  |  Qualitativa Nominal
# Usar como variável de controle apenas para mulheres (C006 = 2)
# =============================================================================
cols_gravidez = [
    "P005",     # Está grávida no momento? (1=Sim | 2=Não | 3=Não sabe) — só mulheres
    "S065",     # Alguma vez ficou grávida? (1=Sim | 2=Não) — histórico
]

# =============================================================================
# 8. COMORBIDADES E SAÚDE MENTAL  |  Módulo Q  |  Qualitativa Nominal
# AJUSTE: Adicionadas depressão (Q092), ansiedade (Q11006), diabetes (Q03001)
#         e hipertensão (Q00201) — essenciais como variáveis de confusão e controle
# =============================================================================
cols_comorbidades = [
    # — Variável-alvo —
    "TOC",      # Diagnóstico autorreferido de TOC (1=Sim | 2=Não) [renomeada de Q11009]

    # — Saúde mental (comorbidades do TOC) —
    "Q092",     # Diagnóstico de DEPRESSÃO por médico ou psicólogo (1=Sim | 2=Não)
    "Q11006",   # Diagnóstico de ANSIEDADE / PÂNICO (1=Sim | 2=Não)
    "Q11007",   # Diagnóstico de ESQUIZOFRENIA (1=Sim | 2=Não)
    "Q11008",   # Diagnóstico de TRANSTORNO BIPOLAR (1=Sim | 2=Não)

    # — Doenças crônicas físicas (variáveis de confusão alimentar) —
    "Q00201",   # Diagnóstico de HIPERTENSÃO ARTERIAL (1=Sim | 2=Não)
    "Q03001",   # Diagnóstico de DIABETES (1=Sim | 2=Não)
    "Q060",     # Diagnóstico de COLESTEROL ALTO (1=Sim | 2=Não)
    "Q06306",   # Diagnóstico de INSUFICIÊNCIA CARDÍACA (1=Sim | 2=Não)
    "Q068",     # Diagnóstico de AVC / DERRAME (1=Sim | 2=Não)
    "Q074",     # Diagnóstico de ASMA / BRONQUITE ASMÁTICA (1=Sim | 2=Não)
    "Q079",     # Diagnóstico de ARTRITE / REUMATISMO (1=Sim | 2=Não)
    "Q084",     # Diagnóstico de PROBLEMA CRÔNICO DE COLUNA (1=Sim | 2=Não)
    "Q088",     # Diagnóstico de DORT (distúrbio osteomuscular relacionado ao trabalho)
    "Q120",     # Diagnóstico de CÂNCER (1=Sim | 2=Não)
    "Q124",     # Diagnóstico de INSUFICIÊNCIA RENAL CRÔNICA (1=Sim | 2=Não)
    "Q128",     # Diagnóstico de OUTRA DOENÇA CRÔNICA (1=Sim | 2=Não)
    "Q11604",   # Diagnóstico de doença crônica pulmonar (enfisema, bronquite, DPOC)
]

# =============================================================================
# 9. VIOLÊNCIA E TRAUMA  |  Módulo V  |  Qualitativa Nominal
# Fato: trauma e violência estão documentados como fatores de risco para TOC
# (DSM-5, 2013; Chaudhary et al., 2023)
# =============================================================================
cols_violencia = [
    "V001",     # Sofreu ofensa, humilhação ou ridicularização nos últ. 12 meses (1=Sim | 2=Não)
    "V00201",   # Foi ameaçado verbalmente de ser ferido nos últ. 12 meses
    "V01401",   # Alguém lhe deu tapa, bofetada ou empurrão (violência física leve)
    "V01404",   # Foi ameaçado ou ferido com arma ou objeto (violência física grave)
    "V02701",   # Alguém tocou seu corpo de forma sexual contra vontade (últ. 12 meses)
    "V02702",   # Foi forçado(a) a ter relações sexuais contra vontade (últ. 12 meses)
    "V034",     # Deixou de realizar atividades habituais por causa de violência
    "V03502",   # Sentiu medo, tristeza, ansiedade ou depressão como consequência de violência
]

# =============================================================================
# 10. ACESSO A SERVIÇOS DE SAÚDE E PLANO  |  Módulos I e J  |  Qual. Nominal / Ordinal
# AJUSTE: Removidas I004 e I005 (tipo de plano e quem paga — muito julgamento)
#         Mantida J051 (dificuldade para alimentar/dormir — clinicamente relevante)
# =============================================================================
cols_servicos_saude = [
    # — Percepção de saúde —
    "J001",     # Avaliação geral do estado de saúde (1=Muito bom … 5=Muito ruim)
    "J00101",   # Avaliação do bem-estar físico e mental (1=Muito bom … 5=Muito ruim)
    "J002",     # Deixou de realizar atividades habituais por saúde nas últ. 2 sem.?
    "J051",     # Foi transportado por ambulância (proxy de gravidade de condição aguda)

    # — Acesso e uso de serviços —
    "J01101",   # Quando consultou médico pela última vez (1=até 1 ano … 5=nunca)
    "J014",     # Conseguiu atendimento na 1ª vez que procurou serviço de saúde?
    "J046",     # Conseguiu obter TODOS os medicamentos receitados?
    "J057",     # Ficou internado em hospital por ≥24h nos últimos 12 meses?

    # — Plano de saúde (presença) —
    "I00101",   # Tem plano de saúde ODONTOLÓGICO? (1=Sim | 2=Não)
    "I00102",   # Tem plano de saúde MÉDICO? (1=Sim | 2=Não)

    # REMOVIDAS (muito julgamento):
    # I004 → O plano paga internação hospitalar?
    # I005 → Quem paga a mensalidade do plano?
]

# =============================================================================
# 11. TRABALHO, RENDA E DEMOGRAFIA  |  Módulos C, E, M  |  Misto
# AJUSTE: Removida E01401 (código CBO — centenas de categorias, sem referência)
#         Adicionada escolaridade (D009a) — determinante social importante
# =============================================================================
cols_trabalho_renda_demografia = [
    # — Demografia básica —
    "C006",     # Sexo (1=Masculino | 2=Feminino)
    "Idade",    # Idade em anos completos — filtrada para 30–59 [renomeada de C008]
    "Estado",   # Unidade da Federação [renomeada de V0001]
    "Regiao",   # Grande região geográfica (derivada de Estado)

    # — Escolaridade (adicionada) —
    "D009a",    # Curso mais elevado frequentado (creche=1 … doutorado=15)

    # — Status de trabalho —
    "E01201",   # Trabalhou na semana de referência? (1=Sim | 2=Não)
    "E019",     # Total de horas trabalhadas por semana (todas as ocupações)

    # REMOVIDA: "E01401" — Código CBO da ocupação (centenas de categorias, muito julgamento)

    # — Renda —
    "E01602",   # Valor em R$ do rendimento bruto mensal do trabalho principal
    "VDF00102", # Rendimento domiciliar per capita — melhor proxy de classe social

    # — Condições de trabalho e saúde mental —
    "M005011",  # Horas trabalhadas entre 20h e 5h (turno noturno) — impacta sono e ansiedade
    "M00601",   # Frequência de trabalho noturno (1=<1x/mês … 6=≥5x/semana)
    "M007",     # Trabalha em turno ininterrupto de 24h? (1=Sim | 2=Não)
    "M011071",  # Sofreu discriminação no ambiente de trabalho? (1=Sim | 2=Não)
]

# =============================================================================
# 12. ANTROPOMETRIA  |  Módulos P e W  |  Quantitativa Contínua
# =============================================================================
cols_antropometria = [
    "Peso",     # Peso autorreferido em kg [renomeada de P00104]
    "Altura",   # Altura autorreferida em cm [renomeada de P00404]
    "W00103",   # Peso AFERIDO em kg (medição na balança durante a coleta PNS)
    "W00203",   # Altura AFERIDA em cm (medição no estadiômetro durante a coleta PNS)
]

# =============================================================================
# AGRUPAMENTO FINAL — todas as colunas do estudo
# =============================================================================
todas_as_colunas = (
    cols_sono
    + cols_sintomas_psicologicos
    + cols_drogas
    + cols_atividade
    + cols_dieta
    + cols_deficiencia
    + cols_gravidez
    + cols_comorbidades
    + cols_violencia
    + cols_servicos_saude
    + cols_trabalho_renda_demografia
    + cols_antropometria
)

def carregar_colunas():
    """Retorna a lista de colunas selecionadas para o estudo."""
    return todas_as_colunas