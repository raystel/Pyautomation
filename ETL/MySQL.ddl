# etl meta data
DROP TABLE IF EXISTS etl.ETL_Job;
CREATE TABLE etl.ETL_Job (
  sys          VARCHAR(10),
  etl_job      VARCHAR(50),
  enable       TINYINT,
  depend_sys   VARCHAR(10),
  depend       VARCHAR(50),
  stream_sys   VARCHAR(10),
  stream       VARCHAR(50),
  source       VARCHAR(50),
  trigger_time      VARCHAR(6)
);





