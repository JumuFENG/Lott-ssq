/* Creating database */
CREATE  DATABASE IF NOT EXISTS  ssq;
/* Selecting database */
USE ssq;

DROP TABLE IF EXISTS ssq_history;

/* admin table */
create table ssq_history
(
    id                  VARCHAR(10)         NOT NULL  UNIQUE,
    date                DATE                NOT NULL,
    red_all             VARCHAR(12)         NOT NULL,
    blue                SMALLINT            NOT NULL,
    red_1               SMALLINT            NOT NULL,
    red_2               SMALLINT            NOT NULL,
    red_3               SMALLINT            NOT NULL,
    red_4               SMALLINT            NOT NULL,
    red_5               SMALLINT            NOT NULL,
    red_6               SMALLINT            NOT NULL,
    total_buy           BIGINT              NOT NULL DEFAULT 0,
    remained            BIGINT              NOT NULL DEFAULT 0,
    award1_count        INT                 NOT NULL DEFAULT 0,
    award1_money        INT                 NOT NULL DEFAULT 0,
    award2_count        INT                 NOT NULL DEFAULT 0,
    award2_money        INT                 NOT NULL DEFAULT 0,
    award3_count        INT                 NOT NULL DEFAULT 0,
    award3_money        INT                 NOT NULL DEFAULT 3000,
    award4_count        INT                 NOT NULL DEFAULT 0,
    award4_money        INT                 NOT NULL DEFAULT 200,
    award5_count        INT                 NOT NULL DEFAULT 0,
    award5_money        INT                 NOT NULL DEFAULT 10,
    award6_count        INT                 NOT NULL DEFAULT 0,
    award6_money        INT                 NOT NULL DEFAULT 5,
    PRIMARY KEY (id)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
