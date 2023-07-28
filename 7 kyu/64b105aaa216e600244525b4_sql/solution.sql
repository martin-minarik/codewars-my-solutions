SELECT *
FROM ((SELECT "a", "b"
      FROM sample_table
      ORDER BY "a"
      LIMIT 10)

      UNION ALL

      SELECT 0 AS "a", '-' AS "b"
      FROM generate_series(1, 10 - (SELECT COUNT(*) FROM sample_table))) AS subquery
LIMIT 10;