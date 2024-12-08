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
    COUNT(DISTINCT M.ESPORTE) = (SELECT DISTINCT COUNT(M1.ESPORTE) FROM MODALIDADE M1);

----

-- Gere uma lista com cada esporte, o número total de participações 
-- de equipes em cada esporte e a pontuação média das equipes que participaram.

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

-- Contagem de jogos de uma equipe em um ano agrupada por resultado
-- independentemente de haver jogos com dado resultado, retornando 0 caso inexista.

SELECT
    P.RESULTADO,
    COUNT(Subquery.ID) AS TOTAL
FROM (
    SELECT 'V'::RESULTADO_JOGO AS RESULTADO
    UNION ALL
    SELECT 'D'::RESULTADO_JOGO
    UNION ALL
    SELECT 'E'::RESULTADO_JOGO
    UNION ALL
    SELECT 'P'::RESULTADO_JOGO
) AS P
LEFT JOIN (
    SELECT
        D.RESULTADO,
        E.ID
    FROM
        DISPUTA D
    JOIN
        EQUIPE E ON D.ID_EQUIPE = E.ID
    JOIN
        JOGO J ON J.ID = D.ID_JOGO
    WHERE
        E.ID = 2
        AND EXTRACT(YEAR FROM J.DATA_JOGO) = 2024
) AS Subquery
ON P.RESULTADO = Subquery.RESULTADO
GROUP BY
    P.RESULTADO
ORDER BY
    P.RESULTADO DESC;

----

-- Seleciona o estudante com melhores estatísticas que participaram
-- de algum prêmio individual ao longo do tempo para cada critério.

SELECT DISTINCT ON (E.CRITERIO)
    E.ESTUDANTE AS ESTUDANTE, 
    E.CRITERIO AS CRITERIO, 
    PI.REGRA_COLOCACAO, 
    E.VALOR AS VALOR
FROM 
    Estatisticas E
JOIN
    Participacao P ON E.ID_EQUIPE = P.ID_EQUIPE AND E.ESTUDANTE = P.ESTUDANTE
LEFT JOIN
    Concorre C ON E.ID_EQUIPE = C.ID_EQUIPE AND E.ESTUDANTE = C.ESTUDANTE
JOIN
    Premio_individual PI ON C.ID_COMPETICAO = PI.ID_COMPETICAO AND E.CRITERIO = PI.CRITERIO
ORDER BY 
    E.CRITERIO,
CASE 
    WHEN PI.REGRA_COLOCACAO = '+' THEN E.VALOR
    WHEN PI.REGRA_COLOCACAO = '-' THEN -E.VALOR
END DESC;

----

-- Seleciona as escolas com mais títulos em cada modalidade acumulados ao 
-- longo dos anos retornando as chaves primária e secundária da modalidade 
-- e o código INEP da escola.

SELECT DISTINCT ON (M.ID)
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
ORDER BY
    M.ID,
    contador DESC;

----