# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(prev_play, opponent_history=[]):
    if not prev_play:
        prev_play = 'R'
    opponent_history.append(prev_play)
    
    # Keep track of the last few moves to detect patterns
    last_three = opponent_history[-3:] if len(opponent_history) >= 3 else opponent_history
    
    # Strategy 1: Detect and counter Quincy's pattern (R,R,P,P,S)
    if len(opponent_history) >= 5:
        quincy_pattern = ['R', 'R', 'P', 'P', 'S']
        if all(opponent_history[-5+i] == quincy_pattern[i] for i in range(5)):
            next_move = {'R': 'P', 'P': 'S', 'S': 'R'}[quincy_pattern[len(opponent_history) % 5]]
            return next_move
    
    # Strategy 2: Counter Kris's strategy (responds to previous move)
    if len(opponent_history) >= 2:
        if opponent_history[-1] == opponent_history[-2]:
            # If the same move is repeated, Kris is likely playing
            return {'R': 'P', 'P': 'S', 'S': 'R'}[prev_play]
    
    # Strategy 3: Counter Mrugesh's strategy (most frequent in last 10)
    if len(opponent_history) >= 10:
        last_ten = opponent_history[-10:]
        most_frequent = max(set(last_ten), key=last_ten.count)
        if last_ten.count(most_frequent) >= 4:  # If a move appears 4 or more times
            return {'R': 'P', 'P': 'S', 'S': 'R'}[most_frequent]
    
    # Strategy 4: Counter Abbey's strategy
    if len(opponent_history) >= 3:
        # Look for patterns in pairs of moves
        last_two = ''.join(opponent_history[-2:])
        if last_two in ['RR', 'PP', 'SS']:
            # If opponent is repeating moves, predict the next move
            return {'R': 'P', 'P': 'S', 'S': 'R'}[prev_play]
    
    # Default strategy: Play the move that beats the opponent's most recent move
    return {'R': 'P', 'P': 'S', 'S': 'R'}[prev_play]
