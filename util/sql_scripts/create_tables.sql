CREATE TABLE areas(
  id uuid PRIMARY KEY NOT NULL,
  name TEXT NOT NULL,
  description TEXT NOT NULL
);


CREATE TABLE abilities(
  id uuid PRIMARY KEY NOT NULL,
  name TEXT NOT null,
  description TEXT NOT NULL,
  area_id uuid NOT NULL,
  FOREIGN KEY (area_id) REFERENCES areas(id)
);


CREATE TABLE questions(
  id uuid PRIMARY KEY NOT NULL,
  statement TEXT NOT NULL,
  answer TEXT NOT NULL,
  difficulty INTEGER NOT NULL,
  is_essay BOOLEAN NOT NULL,
  ability_id uuid NOT NULL,
  FOREIGN KEY (ability_id) REFERENCES abilities(id)
);

CREATE TABLE alternatives(
  id uuid PRIMARY KEY NOT NULL,
  text TEXT NOT NULL,
  question_id uuid NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE history_of_questions(
  id uuid PRIMARY KEY NOT NULL,
  date DATE NOT NULL,
  hit_level INTEGER NOT NULL,
  var_grade INTEGER NOT NULL,
  time INTERVAL NOT NULL,
  question_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE grades(
  id uuid PRIMARY KEY NOT NULL,
  grade INTEGER NOT NULL,
  question_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);


CREATE TABLE chats_messages(
  id uuid PRIMARY KEY NOT NULL,
  history_of_question_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  sequence INTEGER NOT NULL,
  role VARCHAR NOT NULL,
  content TEXT NOT NULL,
  create_date TIMESTAMP NOT NULL,
  FOREIGN KEY (history_of_question_id) REFERENCES history_of_questions(id)
);