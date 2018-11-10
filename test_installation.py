import random
import time
from MAMEToolkit.sf_environment import Environment

roms_path = 'roms/'  # Replace this with the path to your ROMs
env = Environment('env1', roms_path)
print('[test] Loaded SF3 from ROM file')

# https://github.com/M-J-Murray/MAMEToolkit/blob/3041734391292376aa909938ea5b51030e3c0240/MAMEToolkit/sf_environment/Environment.py#L88
print('[test] Wait until learnable gameplay starts...')
frames = env.start()
print('[test] Start!')

env.close()
print('[test] Your installation is complete!')
