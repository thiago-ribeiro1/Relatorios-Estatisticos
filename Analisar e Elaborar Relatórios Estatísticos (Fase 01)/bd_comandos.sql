create database estatisticas;

create table pesquisasatisfacao (
    id SERIAL PRIMARY KEY,
    nota INTEGER NOT NULL CHECK (nota >= 0 AND nota <= 10)        
    num_usuarios INTEGER NOT NULL CHECK (num_usuarios > 0) -- Número de usuários que participaram da pesquisa
);

INSERT INTO pesquisasatisfacao (nota, num_usuarios)
VALUES
    (10, 5),   -- 5 usuários deram nota 10
    (9, 10),   -- 10 usuários deram nota 9
    (8, 8),    -- 8 usuários deram nota 8
    (7, 12),   -- 12 usuários deram nota 7
    (6, 7),    -- 7 usuários deram nota 6
    (5, 9),    -- 9 usuários deram nota 5
    (4, 8),    -- 8 usuários deram nota 4
    (3, 4),    -- 4 usuários deram nota 3
    (2, 3),    -- 3 usuários deram nota 2
    (1, 2);    -- 2 usuários deram nota 1

