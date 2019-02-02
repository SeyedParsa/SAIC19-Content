def qlearning_update(self, state, action, nextState, reward):
    estimatedQ = reward + self.computeValueFromQValues(nextState)
    self.qValues[(state,action)] = estimatedQ