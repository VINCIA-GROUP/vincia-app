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

CREATE TABLE abilities_rating(
  id uuid PRIMARY KEY NOT NULL,
  rating INTEGER NOT NULL,
  rating_deviation INTEGER NOT NULL,
  volatility FLOAT4 NOT NULL,
  ability_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  last_rating_update DATE NOT NULL,
  FOREIGN KEY (ability_id) REFERENCES abilities(id)
);

CREATE TABLE adaptive_question_selection(
  id uuid PRIMARY KEY NOT NULL,
  create_at DATE NOT NULL,
  question_id uuid NOT NULL,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE history_of_user_rating_updates(
  id uuid PRIMARY KEY NOT NULL,
  create_at DATE NOT NULL,
  rating INTEGER NOT NULL,
  rating_deviation INTEGER NOT NULL,
  volatility FLOAT4 NOT NULL,
  user_id VARCHAR NOT null,
  ability_id uuid NOT null,
  FOREIGN KEY (ability_id) REFERENCES abilities(id)
);


CREATE TABLE history_of_questions(
  id uuid PRIMARY KEY NOT NULL,
  create_at DATE NOT NULL,
  hit_level INTEGER NOT NULL,
  time interval ,
  question_id uuid NOT NULL,
  history_of_user_rating_update_id uuid,
  user_id VARCHAR NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id),
  FOREIGN KEY (history_of_user_rating_update_id) REFERENCES history_of_user_rating_updates(id)
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


CREATE TABLE history_of_question_rating_updates(
  id uuid PRIMARY KEY NOT NULL,
  create_at DATE NOT NULL,
  rating INTEGER NOT NULL,
  rating_deviation INTEGER NOT NULL,
  volatility FLOAT4 NOT NULL,
  question_id uuid NOT NULL,
  FOREIGN KEY (question_id) REFERENCES questions(id)
);

CREATE TABLE teste(
	id uuid PRIMARY KEY NOT NULL,
	message VARCHAR NOT NULL
);




