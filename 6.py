class WrongNumberOfPlayersError(Exception): pass
class NoSuchStrategyError(Exception): pass
class OnePlayerError(Exception): pass
class ZeroPlayersError(Exception): pass
def rps_game_winner(mass):
    win_move = {'P': 'R', 'R': 'S', 'S': 'P'}
    try:
        if type(mass) is not list:
            raise TypeError
        if len(mass)>2:
            raise WrongNumberOfPlayersError
        elif len(mass)==1:
            raise OnePlayerError
        elif len(mass)==0:
            raise ZeroPlayersError
        if mass[0][1] not in win_move or mass[1][1] not in win_move:
            raise NoSuchStrategyError
    except WrongNumberOfPlayersError:
        print('\033[31mWrongNumberOfPlayersError\033[0m')
    except OnePlayerError:
        print((f'{mass[0][0]} {mass[0][1]}','\033[31mNoSuchStrategyError\033[0m')[mass[0][1] not in win_move])
    except ZeroPlayersError:
        print('\033[31mZeroPlayersError\033[0m')
    except NoSuchStrategyError:
        print('\033[31mNoSuchStrategyError\033[0m')
    except TypeError:
        print('\033[41mTypeError\033[0m')
    else:
        if mass[0][1]==mass[1][1]:
            print(mass[0][0],mass[0][1])
        else:
            print((f'{mass[1][0]} {mass[1][1]}',f'{mass[0][0]} {mass[0][1]}')[win_move[mass[0][1]]==mass[1][1] ])




rps_game_winner(11)
rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'A']])
rps_game_winner([['player1', 'P'], ['player2', 'S']])
rps_game_winner([['player1', 'P'], ['player2', 'P']])
rps_game_winner([['player2', 'P']])
rps_game_winner([])
