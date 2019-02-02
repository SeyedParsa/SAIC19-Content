def qlearning_update(self, state, action, nextState, reward):
    self.alpha = 0.9
    estimatedQ = self.alhpa * (reward + self.computeValueFromQValues(nextState)) + (1-self.alpha)*self.qvalues[(state,action)]
    self.qValues[(state,action)] = estimatedQ