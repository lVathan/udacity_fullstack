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
    #connect to the database
    conn = connect()
    curs=conn.cursor()
    #delete matches all matches from the tournament
    query = "delete from matches where tournament_id = 1"
    curs.execute(query)

    #commit the changes and then close the connection
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database."""
    #connect to the database
    conn = connect()
    curs=conn.cursor()
    #delete all records from the matches table where the tournament id is 1
    query = "delete from matches where tournament_id = 1"
    curs.execute(query)
    #delete all records of the players table
    query = "delete from players"
    curs.execute(query)
    #commit the changes and then close the connection
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    #connect to the database
    conn = connect()
    curs=conn.cursor()
    #query the table players for the number of entries
    query = "select count(*) from players"
    curs.execute(query)
    #save the number of players found
    player_count = curs.fetchall()[0][0]
    #close the connection and return the number of players
    conn.close()
    return player_count


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique)..
    """
    #sanitize the name provided by the user
    bleach.clean(name, strip=True)
    #connect to the database
    conn=connect()
    curs=conn.cursor()
    #enter the player name into the players table
    curs.execute("insert into players (name) values (%s)", (name,))
    #enter the player id, tournament id, number of wins, and number of matches into the matches table where the player id matches the name provided
    curs.execute("insert into matches (player_id, tournament_id, wins,num_matches) values ((select player_id from players where name = %s limit 1), 1, 0, 0)",(name,))
    #commit the changes and close the connection
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
    #connect to the database
    conn = connect()
    curs=conn.cursor()
    #get the player id, name, wins, and number of matches from the matches table, and order by the number of wins
    query = "select players.player_id, name, wins, num_matches from matches join players on matches.player_id=players.player_id order by wins desc"
    curs.execute(query)
    player_standings = curs.fetchall()
    #close the database connection and return the saved standings
    conn.close()
    return player_standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    #connect to the database
    conn=connect()
    curs=conn.cursor()
    #change the number of matches and number of wins for the winning player
    curs.execute("update matches set num_matches=num_matches+1, wins=wins+1 where player_id = %s", (winner,))
    #change the number of matches for the losing player
    curs.execute("update matches set num_matches=num_matches+1 where player_id = %s", (loser,))    
    #commit the changes to the database and close the connection
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
    #connect to the database
    conn=connect()
    curs=conn.cursor()
    #query the database for th eplayers id, name, and order by the number of wins
    query="select players.player_id, name from matches join players on matches.player_id=players.player_id order by wins desc"
    curs.execute(query)
    #initialize the pairings list and save the standings 
    pairings=[]
    standings=curs.fetchall()
    x=0
    #loop through the standings and pair off the players together and return the pairings
    while x < len(standings):
        pairings.append((standings[x][0],standings[x][1], standings[x+1][0], standings[x+1][1]))
        x=x+2
    return pairings

