-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create sequence player_id_seq start 1;

create table players (
	player_id SERIAL primary key,
	name text
	);
alter table players alter player_id set default nextval('player_id_seq');

create sequence tournament_id_seq start 1;

create table tournaments (
	tournament_id SERIAL primary key,
	name text
	);

alter table tournaments alter tournament_id set default nextval('tournament_id_seq');

create table matches(
	player_id SERIAL references players,
	tournament_id SERIAL references tournaments,
	wins int,
	num_matches int,
	primary key (player_id, tournament_id)
	);

