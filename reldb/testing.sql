select * from (select players.player_id where mod(players.player_id, 2)=1 as id_1, name as player_1, players.player_id as id_2, name as player_2
from matches join players on matches.player_id=players.player_id 
group by wins),(select players.player_id where mod(players.player_id, 2)=0 as id_1, name as player_1, players.player_id as id_2, name as player_2
from matches join players on matches.player_id=players.player_id 
group by wins)