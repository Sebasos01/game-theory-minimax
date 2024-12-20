from itertools import product

def generate_sequences():
    sequences = []
    moves = ['L', 'R']
    for sequence in product(moves, repeat=4):
        seqStr = ''.join(sequence)
        sequences.append(seqStr)
    return sequences

def minmax(depth, sequence, maximizingPlayer, ai, sequence_to_index):
    if depth == 4:
        index = sequence_to_index[sequence]
        value = ai[index]
        return value, sequence
    else:
        moves = ['L', 'R']
        best_value = None
        best_sequence = None
        for move in moves:
            new_sequence = sequence + move
            next_player = not maximizingPlayer
            value, seq = minmax(depth + 1, new_sequence, next_player, ai, sequence_to_index)
            if best_value is None:
                best_value = value
                best_sequence = seq
            else:
                if maximizingPlayer:
                    if value > best_value:
                        best_value = value
                        best_sequence = seq
                    elif value == best_value and seq[depth] == 'L':
                        best_sequence = seq
                else:
                    if value < best_value:
                        best_value = value
                        best_sequence = seq
                    elif value == best_value and seq[depth] == 'L':
                        best_sequence = seq
    return best_value, best_sequence

def play_game(ai_values):
    if len(ai_values) != 16:
        return "Error, se deben ingresar 16 valores para la tupla de nodos terminales"
    sequences = generate_sequences()
    sequence_to_index = {seq: i for i, seq in enumerate(sequences)}
    depth = 0
    sequence = ''
    maximizingPlayer = True
    best_value, best_sequence = minmax(depth, sequence, maximizingPlayer, ai_values, sequence_to_index)
    return best_value, best_sequence

# Inciso A
ai_values = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
result_sequence = play_game(ai_values)
print("Secuencia óptima del juego: ", result_sequence)

# Inciso B
ai_values = (2, 7, 0, 6, 0, 1, 2, 0, 1, 9, 1, 3, 6, 4, 3, 7)
result_sequence = play_game(ai_values)
print("Secuencia óptima del juego: ", result_sequence)
