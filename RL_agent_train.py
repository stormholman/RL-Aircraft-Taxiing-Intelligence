import Taxi_env
from stable_baselines3.common.env_checker import check_env
from stable_baselines3 import A2C, DQN, PPO
from stable_baselines3.common.callbacks import CheckpointCallback
import os
import gym

model_directory = 'models/PPO'  # change the algorithm name here if using something other than DQN
log_directory = 'logs'

if not os.path.exists(model_directory):
    os.makedirs(model_directory)

if not os.path.exists(log_directory):
    os.makedirs(log_directory)

env = Taxi_env.TaxiEnv()
env.reset()


def my_callback(saving_freq):
    chckpcallback = CheckpointCallback(save_freq=saving_freq, save_path='Check_points', name_prefix='PPO_RL')

    return chckpcallback


# lr: 0.0002, gamma: 0.95
def instantiate_model(myoption):
    if myoption == 1:
        model = PPO('MlpPolicy', env, verbose=2, tensorboard_log=log_directory, learning_rate=0.0002,
                    gamma=0.95)  # change DQN to whatever algorithm you want to use

    elif myoption == 2:
        my_path = input("WRITE PREVIOUS CHECKPOINT NUMBER OF STEPS: ")
        dir_path = 'Check_points/PPO_RL_' + str(my_path) + '_steps'
        model = PPO.load(dir_path, env=env)
    return model


if __name__ == '__main__':
    my_timesteps = 100000
    options = input("ENTER 1 FOR TRAINING NEW MODEL, ENTER 2 FOR RESUMING TRAINING: ")
    save_freq = 10000
    model = instantiate_model(int(options))
    chckpcallback = my_callback(save_freq)
    for i in range(1, 20):
        model.learn(total_timesteps=my_timesteps, callback=chckpcallback, reset_num_timesteps=False,
                    tb_log_name="PPO")  # change tb_log_name=DQN according to algorithm

        model.save("{}/{}".format(model_directory, my_timesteps * i))

# Run in terminal for tensorboard:
# python3 -m tensorboard.main --logdir ./gym-taxi/gym_taxi/envs/logs/PPO_0
