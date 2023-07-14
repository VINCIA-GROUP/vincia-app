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
  rating INTEGER NOT NULL,
  rating_deviation INTEGER NOT NULL,
  volatility FLOAT4 NOT NULL,
  last_rating_update DATE NOT NULL,
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
  create_at DATE NOT NULL,
  answer_at DATE,
  hit_level INTEGER,
  rating INTEGER,
  rating_deviation INTEGER,
  volatility FLOAT4,
  time INTERVAL,
  question_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE abilities_rating(
  id uuid PRIMARY KEY NOT NULL,
  rating INTEGER NOT NULL,
  rating_deviation INTEGER NOT NULL,
  volatility FLOAT4 NOT NULL,
  abilitie_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (abilitie_id) REFERENCES abilities(id)
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