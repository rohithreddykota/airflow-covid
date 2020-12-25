CREATE TABLE IF NOT EXISTS covid_time_series 
(
  state         CHAR(2),
  date_value    TIMESTAMP,
  metric_type   VARCHAR(16),
  confirmed     INT8,
  deceased      INT8,
  other         INT8,
  recovered     INT8,
  tested        INT8
);

DROP TABLE if exists temp_covid_time_series;

COMMIT;