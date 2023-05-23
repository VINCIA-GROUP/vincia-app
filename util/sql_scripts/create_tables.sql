CREATE TABLE areas(
  id VARCHAR PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);


CREATE TABLE abilities(
  id VARCHAR PRIMARY KEY NOT NULL,
  name TEXT NOT null,
  description TEXT NOT NULL,
  area_id VARCHAR NOT NULL,
  FOREIGN KEY (area_id) REFERENCES areas(id)
);


CREATE TABLE questions(
  id VARCHAR PRIMARY KEY NOT NULL,
  statement TEXT NOT NULL,
  answer TEXT NOT NULL,
  difficulty INTEGER NOT NULL,
  is_essay BOOLEAN NOT NULL,
  ability_id VARCHAR NOT NULL,
  FOREIGN KEY (ability_id) REFERENCES abilities(id)
);

CREATE TABLE alternatives(
  id VARCHAR PRIMARY KEY NOT NULL,
  text TEXT NOT NULL,
  question_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE history_of_questions(
  id VARCHAR PRIMARY KEY NOT NULL,
  date DATE NOT NULL,
  hit_level INTEGER NOT NULL,
  var_grade INTEGER NOT NULL,
  time INTERVAL NOT NULL,
  question_id VARCHAR NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE grades(
  id VARCHAR PRIMARY KEY NOT NULL,
  grade INTEGER NOT NULL,
  question_id VARCHAR NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);


