-- Análise de atendimentos por estado

SELECT
    estado,
    COUNT(*) AS total_atendimentos
FROM dados_saude
GROUP BY estado
ORDER BY total_atendimentos DESC;
