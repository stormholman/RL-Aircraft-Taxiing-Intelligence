# Reinforcement Learning - Aircraft Taxi Intelligence

## Introduction

- This repository consists of Implementations for manouvering an aircraft over a taxi circuit.
- I have implemented this using 2 Reinforcement Learning algorithms:
    1. Proximal Policy Optimization (PPO)
    2. Deep Q-Network (DQN)
- You can see a demo of this application [here](https://youtu.be/YSKC1OfMABE).

## Briefing the main application:
- Run RL_agent_train.py for traing/executing the model.
- Type option '1' to train a new model.
- Type option '2' to train the model from a certain amount of pretrained steps.
- There is a tensorboard option to visualize learning performance.

## Other files
- The coordinatefinder files help finding coordinates to create the taxi environment.
- The plot files function as a tool for plotting the results and sensitivity results.
- Taxi_env.py captures the environment and dynamics of the model.
- Walls.py & Goals.py help importing the walls and goals in the environment.
- The data folder holds the episodes, steps, laps of various runs with different settings (sensitivity runs).

## Resources
- Code for environment dynamics was inspired from [github](https://github.com/CodeAndAction/DDQN-Car-Racing)
- Airplane png file: [KindPNG](https://www.kindpng.com/imgv/ixmwJbm_transparent-top-png-aircraft-png-top-view-png/)
