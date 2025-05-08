import mesa.agent
import numpy as np
import pandas as pd
import seaborn as sns
import mesa
import matplotlib.pyplot as plt


class RiceBlastAgent(mesa.Agent):
    def __init__(self, model):
        super().__init__(model)

        self.spores = 1

    def say_hi(self):
        print(f"Hi, I am an agent, you can call me {self.unique_id!s}")

    def say_wealth(self):
        print(f"Hi I am agent {self.unique_id} and I have {self.spores} spores ")
    
    def exchange(self):
        if self.spores > 0:
            other_agent = self.random.choice(self.model.agents)
            if other_agent is not None:
                other_agent.spores += 1
                self.spores +=1

class RiceBlastModel(mesa.Model):
    def __init__(self, n, seed=None):
        super().__init__(seed=seed)
        self.num_agents = n

        RiceBlastAgent.create_agents(model=self, n=n)

    def step(self):
        self.agents.shuffle_do("exchange")
    

if __name__ == "__main__":
    model = RiceBlastModel(n=10, seed=42)

    for _ in range(20):
        model.step()

    agent_wealth = [a.spores for a in model.agents]
    # Create a histogram with seaborn
    g = sns.histplot(agent_wealth, discrete=True)
    g.set(
        title="Wealth distribution", xlabel="Wealth", ylabel="number of agents"
    );  

    plt.show()
