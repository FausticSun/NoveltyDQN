import gym

if __name__ == "__main__":
    env = gym.make('BipedalWalkerHardcore-v2')
    env.reset()
    for _ in range(1000):
        env.render()
        env.step(env.action_space.sample()) # take a random action

