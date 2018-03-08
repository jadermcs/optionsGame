class Replay(object):

    """
    For RL a memory of experiences must be written to train the batches
    with old experiences and returns in the form of (s, a, r, s').
    """
    def __init__(self, max_memory=100, discount=.9):
        """TODO: Docstring for __init__.

        :max_memory: The size of the memory container to avoid overflows.
        :discount: The penalty factor for future experiences.
        """
        self.max_memory = max_memory
        self.memory = list()
        self.discount = discount

    def remember(self, states, game_over):
        """Method to store the experiences in the class list.

        :states: The possible states.
        :game_over: If the game has end.
        """
        self.memory.append([states, game_over])
        # Remove oldest memory if list is full
        if len(self.memory) > self.max_memory:
            del self.memory[0]

    def get_batch(self, model, batch_size=32):
        """Interact to get the training data.

        :model: The NN to be trained.
        :batch_size: Size of each training sample.
        :returns: Training sample.

        """
        len_memory = len(self.memory)
        # Number of possible actions in the game.
        num_actions = model.outputshape[-1]
        # Existent states (game field dimension).
        env_dim = self.memory[0][0][0].shape[1]
        #We want to return an input and target vector with inputs from an observed state...
        inputs = np.zeros((min(len_memory, batch_size), env_dim))
        #...and the target r + gamma * max Q(s',a')
        #Note that our target is a matrix, with possible fields not only for the action taken but also
        #for the other possible actions. The actions not take the same value as the prediction to not affect them
        targets = np.zeros((inputs.shape[0], num_actions))
        #We draw states to learn from randomly
        for i, idx in enumerate(np.random.randint(0, len_memory,
                                                  size=inputs.shape[0])):
            """
            Here we load one transition <s, a, r, s'> from memory

            :state_t: initial state s
            :action_t: action taken a
            :reward_t: reward earned r
            :state_tp1: the state that followed s'
            """
            state_t, action_t, reward_t, state_tp1 = self.memory[idx][0]
            #We also need to know whether the game ended at this state
            game_over = self.memory[idx][1]
            #add the state s to the input
            inputs[i:i+1] = state_t
            # First we fill the target values with the predictions of the model.
            # They will not be affected by training (since the training loss for them is 0)
            targets[i] = model.predict(state_t)[0]
            """
            If the game ended, the expected reward Q(s,a) should be the final reward r.
            Otherwise the target value is r + gamma * max Q(s',a')
            """
            #  Here Q_sa is max_a'Q(s', a')
            Q_sa = np.max(model.predict(state_tp1)[0])

            #if the game ended, the reward is the final reward
            if game_over:  # if game_over is True
                targets[i, action_t] = reward_t
            else:
                # r + gamma * max Q(s',a')
                targets[i, action_t] = reward_t + self.discount * Q_sa
        return inputs, targets
