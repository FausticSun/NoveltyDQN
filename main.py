import gym

if __name__ == "__main__":
    env = gym.make('BipedalWalkerHardcore-v2')

    # get initial obsevation of the environment
    observation = env.reset()

    while (True):
        env.render()
        print(observation);

        # choose the action to take
        action = env.action_space.sample()

        observation, reward, isDone, info = env.step(action)

