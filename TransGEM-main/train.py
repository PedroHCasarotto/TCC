import os
import time
import argparse
import numpy as np
import pandas as pd
from tqdm import tqdm
from sklearn import metrics
from sklearn.metrics import precision_recall_curve

import heapq
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch_geometric.data import DataLoader, DataListLoader, Batch
from torch_geometric.nn import DataParallel
from torch.autograd import Variable

from TransGEM.utils import *
from TransGEM.gene_ex_encoder_upgraded import *
from TransGEM.dataset import load_dataset

# Load SELFIES dictionary
TGT_stoi=np.load(args.data_path+"TGT_stoi.npy", allow_pickle=True).item()
TGT_itos=np.load(args.data_path+"TGT_itos.npy", allow_pickle=True)

# Set device
device = torch.device(args.gpu if torch.cuda.is_available() else "cpu")

# Building training data

path = args.data_path+'train/'
train_path=args.data_path+"{}_train.csv".format(args.dataset)
val_path=args.data_path+"{}_val.csv".format(args.dataset)
test_path=args.data_path+"{}_test.csv".format(args.dataset)
train_dataset,valid_dataset,test_dataset,args.max_len,args.vocab_size = load_dataset(path, args.dataset, train_path, val_path, test_path)

# Building a model
from TransGEM.Model import TransGTM
Model = TransGTM(args.dataset, args)

# Training
from TransGEM.trainer import Trainer
print("\n########### Running in {} #############\n".format(device))
trainer = Trainer(Model, train_dataset, valid_dataset, test_dataset, device, args)
trainer.train()

