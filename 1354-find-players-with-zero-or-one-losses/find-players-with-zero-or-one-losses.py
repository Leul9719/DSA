class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = {}
        all_players = set()

        for winner, loser in matches:
            all_players.add(winner)
            all_players.add(loser)
            
            if loser in loss_count:
                loss_count[loser] += 1
            else:
                loss_count[loser] = 1
        
        no_loss = []
        one_loss = []
        
        for player in all_players:
            if player not in loss_count:
                no_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
    
        no_loss.sort()
        one_loss.sort()
        
        return [no_loss, one_loss]