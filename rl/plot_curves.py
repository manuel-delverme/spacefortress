import numpy as np
import pickle
import matplotlib.pyplot as plt

plt.ion()

# fnames = [145,137,140,134]
# human = 1989
# plt.title('Autoturn Game, PPO')
# plt.plot([0,2700],[human,human],marker='+')

# fnames = [144,136,139,135]
# human = 216
# plt.title('Youturn Game, PPO')
# plt.plot([0,2700],[human,human],marker='+')

fnames = [159,160]
plt.title('Temporal Transfer Learning, 600ms')

for f in fnames:
  f1 = pickle.load(open("tr2/"+str(f)+"/learning_curves.p","rb"))
  X = []
  Y = []
  for k in sorted(f1.keys()):
    X.append(k)
    Y.append(f1[k][1])
  plt.plot(X,Y,marker='+')

# plt.legend(['Humans','SF-GRU: Default Rewards','SF-GRU: Dense Rewards','SF-FF: AECI','SF-GRU: AECI'],ncol=2)
plt.legend(['Without Transfer','With Transfer'])

plt.xlabel('Training Iteration')
plt.ylabel('Score')
