-- Modalidades
INSERT INTO Modalidade (ESPORTE, SEXO, IDADE_MINIMA, IDADE_MAXIMA, ALTURA, PESO, TIPO_DEFICIENCIA, TITULARES, RESERVAS, REGRA_PONTUACAO)
VALUES 
('BASQUETE', 'M', 12, 18, 'MEDIO', 'MEDIO', 'NENHUMA', 5, 7, 'V3E1D0'),
('FUTEBOL', 'F', 14, 20, 'QUALQUER', 'QUALQUER', 'NENHUMA', 11, 5, 'V3E1D0'),
('NATAÇÃO', 'M', 10, 15, 'QUALQUER', 'QUALQUER', 'NENHUMA', 1, 0, 'V1E0D0'),
('TÊNIS', 'F', 16, 25, 'ALTO', 'MEDIO', 'NENHUMA', 2, 1, 'V1E0D0'),
('VOLEIBOL', 'M', 12, 18, 'MEDIO', 'MEDIO', 'MOTORA', 6, 6, 'V3E1D0'),
('HANDEBOL', 'F', 14, 20, 'ALTO', 'PESADO', 'VISUAL', 7, 7, 'V3E1D0'),
('ATLETISMO', 'M', 10, 17, 'QUALQUER', 'QUALQUER', 'INTELECTUAL', 1, 0, 'V1E0D0'),
('GINÁSTICA', 'F', 10, 15, 'BAIXO', 'LEVE', 'VISUAL', 1, 0, 'V2E0D0');

-- Modalidades desportivas
INSERT INTO Modalidade_desportiva (ID)
VALUES 
(1),
(2),
(3),
(4);

-- Modalidades paradesportivas
INSERT INTO Modalidade_paradesportiva (ID)
VALUES 
(5),
(6),
(7),
(8);

-- Adaptações
INSERT INTO Adaptacoes (ID_MODALIDADE, ADAPTACAO)
VALUES 
(5, 'CADEIRA DE RODAS'),
(6, 'BOLA COM SOM'),
(7, 'GUIA VISUAL'),
(8, 'REGRAS ADAPTADAS');

-- Medidas oficiais
INSERT INTO Medidas_oficiais (ID_MODALIDADE, EQUIPAMENTO_CIRCUITO, MEDIDA)
VALUES 
(1, 'LARGURA QUADRA (M)', 28.00),
(2, 'LARGURA CAMPO (M)', 90.00),
(3, 'COMPRIMENTO PISCINA (M)', 25.00),
(4, 'DIAMETRO RAQUETE (CM)', 20.00);

-- Funções
INSERT INTO Funcoes (CPF, FUNCAO)
VALUES 
('12345678901', 'E'),
('12345678902', 'E'),
('12345678903', 'E'),
('12345678904', 'E'),
('12345678913', 'E'),
('12345678914', 'E'),
('12345678905', 'P'),
('12345678906', 'P'),
('12345678907', 'P'),
('12345678908', 'P'),
('12345678909', 'A'),
('12345678910', 'A'),
('12345678911', 'A'),
('12345678912', 'A');

-- Estudantes
INSERT INTO Estudante (CPF, NOME, ALTURA, PESO, SEXO, IDADE, TIPO_DEFICIENCIA)
VALUES 
('12345678901', 'EDSON ARANTES DO NASCIMENTO', 'MEDIO', 'MEDIO', 'M', 15, 'NENHUMA'),
('12345678902', 'MARIE CURIE', 'MEDIO-BAIXO', 'LEVE', 'F', 14, 'NENHUMA'),
('12345678903', 'ISAAC NEWTON', 'ALTO', 'PESADO', 'M', 17, 'NENHUMA'),
('12345678904', 'SANTOS DUMONT', 'BAIXO', 'LEVE', 'F', 12, 'NENHUMA'),
('12345678913', 'OSWALDO CRUZ', 'ALTO', 'PESADO', 'F', 14, 'VISUAL'),
('12345678914', 'ELIS REGINA', 'MEDIO', 'MEDIO', 'M', 13, 'MOTORA');

-- Professores
INSERT INTO Professor (CPF, NOME, DISCIPLINA)
VALUES 
('12345678905', 'CARLOS DRUMMOND DE ANDRADE', 'EDUCACAO_FISICA'),
('12345678906', 'ALBERT EINSTEIN', 'CIENCIAS'),
('12345678907', 'AYRTON SENNA', 'MATEMATICA'),
('12345678908', 'WILLIAM SHAKESPEARE', 'PORTUGUES');

-- Árbitros
INSERT INTO Arbitro (CPF, NOME, CIDADE)
VALUES 
('12345678909', 'GEORGE ORWELL', 'SÃO PAULO'),
('12345678910', 'MICHAEL PHELPS', 'RIO DE JANEIRO'),
('12345678911', 'ELVIS PRESLEY', 'BRASILIA'),
('12345678912', 'JOAQUIM JOSÉ DA SILVA XAVIER', 'CURITIBA');

-- Escolas
INSERT INTO Escola (ANO, CODIGO_INEP_MEC, CIDADE, PONTUACAO_GERAL)
VALUES 
(2024, '12345678', 'SÃO PAULO', DEFAULT),
(2024, '87654321', 'RIO DE JANEIRO', 15),
(2024, '11223344', 'BRASILIA', 2),
(2024, '44332211', 'CURITIBA', 0);

-- Locais
INSERT INTO Local (CIDADE, BAIRRO, RUA, NUMERO, CAPACIDADE)
VALUES 
('SÃO PAULO', 'CENTRO', 'RUA A', 100, 2000),
('RIO DE JANEIRO', 'BOTAFOGO', 'RUA B', 200, 1500),
('BRASILIA', 'ASA SUL', 'RUA C', 300, 1800),
('CURITIBA', 'BATEL', 'RUA D', 400, 1200);

-- Competições
INSERT INTO Competicao (ID_MODALIDADE, ANO, ETAPA, PREMIACAO, REGRA_COLOCACAO, FINALIZADA)
VALUES 
(1, 2024, 'REGIONAL', 1000, 'PONTOS', FALSE),
(2, 2024, 'ESTADUAL', 2000, 'PLAYOFFS', TRUE),
(3, 2024, 'SUBREGIONAL', 500, 'UNICO', FALSE),
(4, 2024, 'REGIONAL', 1500, 'PONTOS', FALSE);

-- Jogos
INSERT INTO Jogo (DATA_JOGO, HORARIO, CIDADE, BAIRRO, RUA, NUMERO, ID_COMPETICAO, ARBITRO, FASE, TEMPO_DE_JOGO, PUBLICO)
VALUES 
('2024-11-20', '10:00:00', 'SÃO PAULO', 'CENTRO', 'RUA A', 100, 1, '12345678909', 'GRUPOS', '01:30:00', 1000),
('2024-11-21', '14:00:00', 'RIO DE JANEIRO', 'BOTAFOGO', 'RUA B', 200, 2, '12345678910', 'QUARTAS', '02:00:00', 800),
('2024-11-22', '16:00:00', 'BRASILIA', 'ASA SUL', 'RUA C', 300, 3, '12345678911', 'SEMIFINAL', '02:30:00', 700),
('2024-11-23', '18:00:00', 'CURITIBA', 'BATEL', 'RUA D', 400, 4, '12345678912', 'FINAL', '03:00:00', 900);

-- Equipes
INSERT INTO Equipe (ID_MODALIDADE, ANO, CODIGO_INEP_MEC, NOME)
VALUES 
(1, 2024, '12345678', 'ABAPORU'),
(2, 2024, '87654321', 'OPERARIOS'),
(3, 2024, '11223344', 'AGUAS DE MARCO'),
(4, 2024, '44332211', 'DOM CASMURRO'),
(5, 2024, '87654321', 'VIDAS SECAS'),
(6, 2024, '44332211', 'MACUNAIMA');

-- Participações
INSERT INTO Participacao (ID_EQUIPE, ESTUDANTE)
VALUES 
(1, '12345678901'),
(2, '12345678902'),
(3, '12345678903'),
(4, '12345678904'),
(5, '12345678913'),
(6, '12345678914');

-- Disputas
INSERT INTO Disputa (ID_EQUIPE, ID_JOGO, RESULTADO)
VALUES 
(1, 1, 'V'),
(2, 2, 'D'),
(3, 3, 'E'),
(4, 4, 'P');

-- Estatísticas
INSERT INTO Estatisticas (ID_EQUIPE, ESTUDANTE, CRITERIO, VALOR)
VALUES 
(1, '12345678901', 'CESTAS', 10),
(2, '12345678902', 'GOLS', 5),
(3, '12345678903', 'TEMPO', 8),
(4, '12345678904', 'PONTOS', 120);

-- Prêmios individuais
INSERT INTO Premio_individual (ID_COMPETICAO, CRITERIO, REGRA_COLOCACAO, PREMIACAO)
VALUES 
(1, 'CESTAS', '+', 500),
(2, 'GOLS', '+', 300),
(3, 'TEMPO', '-', 200),
(4, 'PONTOS', '+', DEFAULT);

-- Concorrência a prêmios individuais
INSERT INTO Concorre (ID_EQUIPE, ESTUDANTE, ID_COMPETICAO, CRITERIO, RESULTADO)
VALUES 
(6, '12345678914', 3, 'TEMPO', 'P'),
(1, '12345678901', 1, 'CESTAS', 'P'),
(2, '12345678902', 2, 'GOLS', 'V'),
(3, '12345678903', 3, 'TEMPO', 'P'),
(4, '12345678904', 4, 'PONTOS', 'P');

-- ParticipaçõE.ID_EQUIPE = P.ID_EQUIPE AND E.ESTUDANTE = P.ESTUDANTEes em competições
INSERT INTO Participa (ID_COMPETICAO, ID_EQUIPE, COLOCACAO, PONTUACAO)
VALUES 
(1, 1, 1, 10),
(2, 2, 2, 8),
(3, 3, 3, 6),
(4, 4, 4, 4);

-- Patrocínios
INSERT INTO Patrocinios (ID_EQUIPE, PATROCINIO)
VALUES 
(1, 'NIKE'),
(2, 'ADIDAS'),
(3, 'PUMA'),
(4, 'REEBOK');

-- Coordenação de equipes
INSERT INTO Coordena (PROFESSOR, ID_EQUIPE)
VALUES 
('12345678905', 1),
('12345678906', 2),
('12345678907', 3),
('12345678908', 4);