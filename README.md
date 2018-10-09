# NoveltyDQN
Training a DQN with novelty search to solve OpenAI Bipedal Walker Hardcore


## Setting Up the Project

Download and install Anaconda on your machine 

Create an Anaconda virtual environment and name it NoveltyDQN
`conda create --name NoveltyDQN python=3.5.6`

```commandline
# Activate the environment 
source activate NoveltyDQN**

# Install openai gym
pip install gym 
conda install pytorch torchvision -c pytorch

# Box2D requirement in order to run the environment
pip install box2d-py

```

At this point, your project should be able to run. To run the project, run the following command in the root directory of the project
'''
python main.py
'''

To run [PyTorch DQN tutorial](https://pytorch.org/tutorials/intermediate/reinforcement_q_learning.html), install matplotlib with
'''
pip install matplotlib
'''
and run
'''
python reinforcement_q_learning.py
'''

Note that this project runs on python 3.5.6
