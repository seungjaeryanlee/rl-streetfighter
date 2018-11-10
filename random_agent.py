import random
import time
from MAMEToolkit.sf_environment import Environment


roms_path = 'roms/'  # Replace this with the path to your ROMs
env = Environment('env1', roms_path)
print('[random] Loaded SF3 from ROM file')

# https://github.com/M-J-Murray/MAMEToolkit/blob/3041734391292376aa909938ea5b51030e3c0240/MAMEToolkit/sf_environment/Environment.py#L88
print('[random] Wait until learnable gameplay starts...')
frames = env.start()
print('[random] Start!')

game_done = False
while True:
    move_action = random.randint(0, 8)
    attack_action = random.randint(0, 9)
    # frames, reward, round_done, stage_done, game_done = env.step(move_action, attack_action)
    frames, reward, round_done, stage_done, game_done = env.step(0, 0)
    if game_done:
        break
    elif stage_done:
        print('[random] Stage finished: retrieving next state.')
        env.next_stage()
    elif round_done:
        print('[random] Round finished: retrieving next round.')
        env.next_round()

print('[random] Game finished: closing environment')
env.close()
