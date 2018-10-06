# NoveltyDQN
Training a DQN with novelty search to solve OpenAI Bipedal Walker Hardcore


## Setting Up the Project

Download and install Anaconda on your machine 

Create an Anaconda virtual environment and name it NoveltyDQN

```commandline

# Activate the environment 
source activate NoveltyDQN**

# Install dependencies to run the project
conda install -c https://conda.anaconda.org/kne pybox2d
pip install pyglet 
pip install six
pip install cython
```

At this point, your project should be able to run. To run the project, run the following command in the root directory of the project
'''
python bipedal_walker.py
'''

Note that this project runs on python 3.5.6
