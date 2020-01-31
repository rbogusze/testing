-- ** Anomaly detection **
-- Compute an anomaly score for each record in the source stream using Random Cut Forest
-- Creates a temporary stream and defines a schema
CREATE OR REPLACE STREAM "TEMP_STREAM" (
   "column1"        DOUBLE,
   "column2"        DOUBLE,
   "column3"        DOUBLE,
   "column4"        DOUBLE,
   "column5"        DOUBLE,
   "column6"        DOUBLE,
   "column7"        DOUBLE,
   "column8"        DOUBLE,
   "column9"        DOUBLE,
   "column10"        DOUBLE,
   "column11"        DOUBLE,
   "column12"        DOUBLE,
   "column13"        DOUBLE,
   "column14"        DOUBLE,
   "column15"        DOUBLE,
   "column16"        DOUBLE,
   "column17"        DOUBLE,
   "column18"        DOUBLE,
   "column19"        DOUBLE,
   "column20"        DOUBLE,
   "column21"        DOUBLE,
   "column22"        DOUBLE,
   "column23"        DOUBLE,
   "column24"        DOUBLE,
   "column25"        DOUBLE,
   "column26"        DOUBLE,
   "column27"        DOUBLE,
   "column28"        DOUBLE,
   "column29"        DOUBLE,
   "column30"        DOUBLE,
   "ANOMALY_SCORE"  DOUBLE);
-- Creates an output stream and defines a schema
CREATE OR REPLACE STREAM "DESTINATION_SQL_STREAM" (
   "ANOMALY_SCORE"  DOUBLE);
 
-- Compute an anomaly score for each record in the source stream
-- using Random Cut Forest
CREATE OR REPLACE PUMP "STREAM_PUMP" AS INSERT INTO "TEMP_STREAM"
SELECT STREAM "COL0","COL1", "COL2", "COL3", "COL4", "COL5", "COL6", "COL7", "COL8", "COL9", "COL10", "COL11", "COL12", "COL13", "COL14", "COL15", "COL16", "COL17", "COL18", "COL19", "COL20", "COL21", "COL22", "COL23", "COL24", "COL25", "COL26", "COL27", "COL28", "COL29", "ANOMALY_SCORE" FROM
  TABLE(RANDOM_CUT_FOREST(
    CURSOR(SELECT STREAM * FROM "SOURCE_SQL_STREAM_001")
  )
);
-- Sort records by descending anomaly score, insert into output stream
CREATE OR REPLACE PUMP "OUTPUT_PUMP" AS INSERT INTO "DESTINATION_SQL_STREAM"
SELECT STREAM "ANOMALY_SCORE" FROM "TEMP_STREAM" 
ORDER BY FLOOR("TEMP_STREAM".ROWTIME TO SECOND), ANOMALY_SCORE DESC;

