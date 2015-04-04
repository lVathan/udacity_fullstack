#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import bleach


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")



def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    curs=conn.cursor()
    query = "delete from matches where tournament_id = 1"
    curs.execute(query)
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    curs=conn.cursor()
    query = "delete from matches where tournament_id = 1"
    curs.execute(query)
    query = "delete from players"
    curs.execute(query)
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    curs=conn.cursor()
    query = "select count(*) from players"
    curs.execute(query)
    player_count = curs.fetchall()[0][0]
    conn.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    bleach.clean(name, strip=True)
    conn=connect()
    curs=conn.cursor()
    curs.execute("insert into players (name) values (%s)", (name,))
    curs.execute("insert into matches (player_id, tournament_id, wins,num_matches) values ((select player_id from players where name = %s limit 1), 1, 0, 0)",(name,))
    conn.commit()
    conn.close()




def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    curs=conn.cursor()
    query = "select players.player_id, name, wins, num_matches from matches join players on matches.player_id=players.player_id order by wins desc"
    curs.execute(query)
    player_standings = curs.fetchall()
    conn.close()
    return player_standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn=connect()
    curs=conn.cursor()
    curs.execute("update matches set num_matches=num_matches+1, wins=wins+1 where player_id = %s", (winner,))
    curs.execute("update matches set num_matches=num_matches+1 where player_id = %s", (loser,))    
    conn.commit()
    conn.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn=connect()
    curs=conn.cursor()
    query="select players.player_id, name from matches join players on matches.player_id=players.player_id order by wins desc"
    curs.execute(query)
    pairings=[]
    standings=curs.fetchall()
    x=0
    while x < len(standings):
        pairings.append((standings[x][0],standings[x][1], standings[x+1][0], standings[x+1][1]))
        x=x+2
    return pairings

