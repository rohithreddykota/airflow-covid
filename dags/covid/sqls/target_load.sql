INSERT INTO covid_time_series
(
  state,
  date_value,
  metric_type,
  confirmed,
  deceased,
  other,
  recovered,
  tested
)
SELECT state::CHAR(2),
       date_value::TIMESTAMP,
       metric_type::VARCHAR(16),
       confirmed::INT8,
       deceased::INT8,
       other::INT8,
       recovered::INT8,
       tested::INT8
FROM temp_covid_time_series;

DROP TABLE temp_covid_time_series;

COMMIT;

