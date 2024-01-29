
CREATE TABLE bookmark
(
  id          varchar  NOT NULL,
  srcstr      varchar  NOT NULL COMMENT 'source string',
  trgstr      varchar  NOT NULL COMMENT 'target string',
  createdtime datetime NOT NULL COMMENT 'created date&time',
  deleted     boolean  NOT NULL COMMENT 'is deleted',
  deletedtime datetime NOT NULL COMMENT 'deleted date&time',
  userid      varchar  NOT NULL,
  PRIMARY KEY (id)
) COMMENT 'bookmark of tranlation';

CREATE TABLE history
(
  id          varchar  NOT NULL,
  srcstr      varchar  NOT NULL COMMENT 'source string',
  trgstr      varchar  NOT NULL COMMENT 'target string',
  createdtime datetime NOT NULL COMMENT 'created date&time',
  deleted     boolean  NOT NULL COMMENT 'is deleted',
  deletedtime datetime NOT NULL COMMENT 'deleted date&time',
  userid      varchar  NOT NULL,
  PRIMARY KEY (id)
) COMMENT 'history of tranlation';

CREATE TABLE rating
(
  id     varchar NOT NULL,
  rating int     NULL     COMMENT 'rating score(1-5)',
  id     varchar NOT NULL,
  PRIMARY KEY (id)
) COMMENT 'user rating';

CREATE TABLE suggestion
(
  id      varchar NOT NULL,
  srcstr  varchar NOT NULL COMMENT 'source string',
  trgstr  varchar NOT NULL COMMENT 'target string',
  sgststr varchar NOT NULL COMMENT 'suggested string',
  id      varchar NOT NULL,
  PRIMARY KEY (id)
) COMMENT 'user suggestion';

CREATE TABLE User
(
  id varchar NOT NULL,
  PRIMARY KEY (id)
) COMMENT 'user_id ';

CREATE TABLE UserProfile
(
  id       varchar NOT NULL,
  username varchar NULL    ,
  userid   varchar NOT NULL COMMENT 'foreign key',
  password varchar NOT NULL COMMENT 'user password',
  PRIMARY KEY (id)
) COMMENT 'user profile';

ALTER TABLE UserProfile
  ADD CONSTRAINT FK_User_TO_UserProfile
    FOREIGN KEY (userid)
    REFERENCES User (id);

ALTER TABLE history
  ADD CONSTRAINT FK_User_TO_history
    FOREIGN KEY (userid)
    REFERENCES User (id);

ALTER TABLE bookmark
  ADD CONSTRAINT FK_User_TO_bookmark
    FOREIGN KEY (userid)
    REFERENCES User (id);

ALTER TABLE rating
  ADD CONSTRAINT FK_User_TO_rating
    FOREIGN KEY (id)
    REFERENCES User (id);

ALTER TABLE suggestion
  ADD CONSTRAINT FK_User_TO_suggestion
    FOREIGN KEY (id)
    REFERENCES User (id);
