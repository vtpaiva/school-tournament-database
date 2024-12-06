-- Selecionar escolas com equipes em todas os esportes possíveis.

SELECT 
    ES.CODIGO_INEP_MEC
FROM 
    ESCOLA ES
JOIN 
    EQUIPE E ON ES.ANO = E.ANO AND ES.CODIGO_INEP_MEC = E.CODIGO_INEP_MEC
JOIN 
    MODALIDADE M ON E.ID_MODALIDADE = M.ID
GROUP BY 
    ES.CODIGO_INEP_MEC
HAVING 
    COUNT(DISTINCT M.ESPORTE) = (SELECT COUNT(M1.ESPORTE) FROM MODALIDADE M1);

----

-- Gere uma lista com cada modalidade esportiva, o número total de participações 
-- e a pontuação média das equipes que participaram.

SELECT 
    M.ESPORTE AS Modalidade,
    COUNT(P.ID_Equipe) AS TotalParticipacoes,
    ROUND(AVG(P.Pontuacao), 2) AS PontuacaoMedia
FROM 
    Participa P
JOIN 
    Equipe E ON P.ID_Equipe = E.ID
JOIN 
    Modalidade M ON E.ID_Modalidade = M.ID
GROUP BY 
    M.ESPORTE
ORDER BY 
    TotalParticipacoes DESC;

----

-- Contagem de jogos de uma equipe em um período agrupada por resultado.

WITH PossiveisResultados AS (
    SELECT 'V'::RESULTADO_JOGO AS RESULTADO
    UNION ALL
    SELECT 'D'::RESULTADO_JOGO
    UNION ALL
    SELECT 'E'::RESULTADO_JOGO
    UNION ALL
    SELECT 'P'::RESULTADO_JOGO
)

SELECT
    P.RESULTADO,
    COUNT(E.ID)
FROM
    DISPUTA D
JOIN
    EQUIPE E ON D.ID_EQUIPE = E.ID AND E.ID = 2
JOIN
    JOGO J ON J.ID = D.ID_JOGO AND EXTRACT(YEAR FROM J.DATA_JOGO) = 2024
RIGHT JOIN
    PossiveisResultados P ON P.RESULTADO = D.RESULTADO
GROUP BY
    P.RESULTADO
ORDER BY
    P.RESULTADO DESC;

----

-- Seleciona o estudante com melhores estatísticas ao longo
-- do tempo para cada critério.

WITH ESTATISTICAS_ALUNOS AS (
    SELECT
        E.ESTUDANTE AS ESTUDANTE, 
        E.CRITERIO AS CRITERIO, 
        PI.REGRA_COLOCACAO AS REGRA, 
        E.VALOR AS VALOR
    FROM 
        Estatisticas E
    JOIN
        Participacao P ON E.ID_EQUIPE = P.ID_EQUIPE AND E.ESTUDANTE = P.ESTUDANTE
    JOIN
        Concorre C ON E.ID_EQUIPE = C.ID_EQUIPE AND E.ESTUDANTE = C.ESTUDANTE
    JOIN
        Premio_individual PI ON C.ID_COMPETICAO = PI.ID_COMPETICAO AND C.CRITERIO = PI.CRITERIO
)

SELECT 
    EC.CRITERIO,
    EC.REGRA,
    EC.ESTUDANTE,
    EC.VALOR AS VALOR_RESULTADO
FROM 
    ESTATISTICAS_ALUNOS EC
WHERE 
    (EC.CRITERIO, EC.REGRA, EC.VALOR) IN (
        SELECT 
            CRITERIO, 
            REGRA,
            CASE 
                WHEN REGRA = '+' THEN MAX(VALOR) 
                WHEN REGRA = '-' THEN MIN(VALOR)
            END AS VALOR_RESULTADO
        FROM 
            ESTATISTICAS_ALUNOS
        GROUP BY 
            CRITERIO, 
            REGRA
    )
ORDER BY 
    EC.CRITERIO,
    EC.REGRA;

----

-- Seleciona as escolas com mais títulos de acordo com a modalidade
-- retornando a chave secundária da modalidade e o ID da escola.

WITH EscolaColocacoes AS (
    SELECT 
        M.ID AS MODALIDADE_ID,
        M.ESPORTE AS ESPORTE,
        M.SEXO AS SEXO, 
        M.IDADE_MINIMA AS IDADE_MINIMA,
        M.IDADE_MAXIMA AS IDADE_MAXIMA,
        M.ALTURA AS ALTURA,
        M.PESO AS PESO,
        M.TIPO_DEFICIENCIA AS DEFICIENCIA,
        ES.CODIGO_INEP_MEC AS ESCOLA,
        COUNT(C.ID) AS contador
    FROM
        PARTICIPA P
    JOIN
        COMPETICAO C ON P.ID_COMPETICAO = C.ID AND P.COLOCACAO = 1
    JOIN
        EQUIPE E ON P.ID_EQUIPE = E.ID
    JOIN
        ESCOLA ES ON E.ANO = ES.ANO AND E.CODIGO_INEP_MEC = ES.CODIGO_INEP_MEC
    JOIN
        MODALIDADE M ON M.ID = C.ID_MODALIDADE
    GROUP BY 
        ES.CODIGO_INEP_MEC,
        M.ID,
        M.ESPORTE,
        M.SEXO, 
        M.IDADE_MINIMA,
        M.IDADE_MAXIMA,
        M.ALTURA,
        M.PESO,
        M.TIPO_DEFICIENCIA
)

SELECT 
    EC.ESPORTE,
    EC.SEXO, 
    EC.IDADE_MINIMA,
    EC.IDADE_MAXIMA,
    EC.ALTURA,
    EC.PESO,
    EC.DEFICIENCIA,
    EC.ESCOLA,
    EC.CONTADOR AS MAX_CONTADOR
FROM 
    ESCOLACOLOCACOES EC
JOIN (
    SELECT 
        MODALIDADE_ID,
        MAX(CONTADOR) AS MAX_CONTADOR
    FROM 
        ESCOLACOLOCACOES
    GROUP BY 
        MODALIDADE_ID
) 
AS 
    MAX_CONTADOR_TBL ON EC.MODALIDADE_ID = MAX_CONTADOR_TBL.MODALIDADE_ID 
    AND EC.CONTADOR = MAX_CONTADOR_TBL.MAX_CONTADOR
ORDER BY
    EC.ESPORTE;

----