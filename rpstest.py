import gym
import rpsgym

env = gym.make('RPS-v0')
policy = rpsgym.WeightedAgent(0,0,1)
env.add_partner_policy(rpsgym.WeightedAgent(0,1,1))

obs = env.reset()

numgames = 100
rewards = []
for game in range(numgames):
    env.reset()
    done = False
    while not done:

        action = policy.get_action(obs, False)

        obs, reward, done, _ = env.step(action)
        rewards.append(reward)
env.close()
print(f"numwin: {len([x for x in rewards if x == 1])/numgames}")
print(f"numtie: {len([x for x in rewards if x == 0])/numgames}")
print(f"numlose: {len([x for x in rewards if x == -1])/numgames}")