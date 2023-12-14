import matplotlib.pyplot as plt

def lossGraph(trainingLossHistory: list, testingLossHistory: list, 
              trainingAccuracyHistory: list, testingAccuracyHistory: list, epochs: int) -> object:
  _, ax = plt.subplots(nrows=1, ncols=2, figsize=(20, 5))
  ax[0].set_title("Training/Testing Loss")
  ax[0].plot(trainingLossHistory, label="training loss", c='red')
  ax[0].plot(testingLossHistory, label="testing loss", c='blue')
  ax[0].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[0].set_xlabel("Epochs")
  ax[0].set_ylabel("Loss")
  ax[0].legend()

  ax[1].set_title("Training/Testing Accuracy")
  ax[1].plot(trainingAccuracyHistory, label="training accuracy", c='red')
  ax[1].plot(testingAccuracyHistory, label="testing accuracy", c='blue')
  ax[1].set_xticks(range(0, epochs), range(1, epochs+1))
  ax[1].set_xlabel("Epochs")
  ax[1].set_ylabel("Accuracy")
  ax[1].legend()

  plt.tight_layout()
  plt.show()
  

