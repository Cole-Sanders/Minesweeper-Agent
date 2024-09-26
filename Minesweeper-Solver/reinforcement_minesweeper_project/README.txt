The RL agent has 4 main files:
1. game.py: Contains the game creation
2. tester.py: Contains the testing code
3. train_ddqn.py: Contains the training code required
4. Models/ddqn.py: Contains the model class

To test out the pre-trained model, two options are available:
1. Let it play the game: Uncomment lines 144 to 146 and comment line 147 in tester.py
2. To verify the win rate: Comment lines 144 to 146 and uncomment line 147 in tester.py

In the terminal, run the code using:
python tester.py


Required libraries:
numpy
pandas
pytorch
numba
