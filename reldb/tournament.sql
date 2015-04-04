-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
#create a sequence for the player_id that starts at 1 so each new player gets the next number in the sequence
create sequence player_id_seq start 1;

#create the table for the players
create table players (
	player_id SERIAL primary key,
	name text
	);
#set the rule so each new player gets the next value in the player sequence
alter table players alter player_id set default nextval('player_id_seq');

#create a sequence for the tornament id
create sequence tournament_id_seq start 1;

#create the table for the tournaments
create table tournaments (
	tournament_id SERIAL primary key,
	name text
	);

#set the rule so each new tournament gets the next value in the tournament sequence
alter table tournaments alter tournament_id set default nextval('tournament_id_seq');

#create the matches table where the primary key is a combination of the player_id and tournament id
create table matches(
	player_id SERIAL references players,
	tournament_id SERIAL references tournaments,
	wins int,
	num_matches int,
	primary key (player_id, tournament_id)
	);

