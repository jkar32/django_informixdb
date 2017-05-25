"""
    0 = CHAR
    1 = SMALLINT
    2 = INTEGER
    3 = FLOAT
    4 = SMALLFLOAT
    5 = DECIMAL
    6 = SERIAL 1
    7 = DATE
    8 = MONEY
    9 = NULL
    10 = DATETIME
    11 = BYTE
    12 = TEXT
    13 = VARCHAR
    14 = INTERVAL
    15 = NCHAR
    16 = NVARCHAR
    17 = INT8
    18 = SERIAL8 1
    19 = SET
    20 = MULTISET
    21 = LIST
    22 = ROW (unnamed)
    23 = COLLECTION
    40 = LVARCHAR fixed-length opaque types 2
    41 = BLOB, BOOLEAN, CLOB variable-length opaque types 2
    43 = LVARCHAR (client-side only)
    45 = BOOLEAN
    52 = BIGINT
    53 = BIGSERIAL 1
    2061 = IDSSECURITYLABEL 2, 3
    4118 = ROW (named)
"""

informix_types = [
	(0, 'SQL_TYPE_CHAR', 'CharField'),
	(1, 'SQL_TYPE_SMALLINT', 'SmallIntegerField'),
	(2, 'SQL_TYPE_INTEGER', 'IntegerField'),
	(3, 'SQL_TYPE_FLOAT', 'FloatField'),
	(3, 'SQL_TYPE_DOUBLE', 'FloatField'),
	(4, 'SQL_TYPE_REAL', 'FloatField'),
	(4, 'SQL_TYPE_SMFLOAT', 'FloatField'),
	(5, 'SQL_TYPE_DECIMAL', 'DecimalField'),
	(5, 'SQL_TYPE_NUMERIC', 'DecimalField'),
	(6, 'SQL_TYPE_SERIAL', 'AutoField'),
	(7, 'SQL_TYPE_DATE', 'DateField'),
	(8, 'SQL_TYPE_MONEY', 'DecimalField'),
	(9, 'SQL_TYPE_NULL', '??'),
	(10, 'SQL_TYPE_DATETIME', 'DateTimeField'),
	(11, 'SQL_TYPE_BYTE', 'BinaryField'),
	(12, 'SQL_TYPE_TEXT', 'TextField'),
	(13, 'SQL_TYPE_VARCHAR', 'CharField'),
	(14, 'SQL_TYPE_INTERVAL', '??'),
	(15, 'SQL_TYPE_NCHAR', 'CharField'),
	(16, 'SQL_TYPE_NVARCHAR', 'CharField'),
	(17, 'SQL_TYPE_INT8', 'IntegerField'),
	(18, 'SQL_TYPE_SERIAL8', 'AutoField'),
	(19, 'SQL_TYPE_SET', '??'),
	(31, 'SQL_TYPE_MASK', '??'),
	(40, 'SQL_TYPE_LVARCHAR', 'CharField'),
    (43, 'SQL_TYPE_LVARCHAR', 'CharField'),
    (45, 'SQL_TYPE_BOOLEAN', 'BoolField'),
	(52, 'SQL_TYPE_BIGINT', 'IntegerField'),
]