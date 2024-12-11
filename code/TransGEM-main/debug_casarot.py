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

import selfies as sf
from rdkit import Chem, RDConfig
from rdkit.Chem import ChemicalFeatures, MolFromSmiles, AllChem
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from rdkit.Chem import AllChem as Chem
from rdkit.Chem.Draw import IPythonConsole
from rdkit.Chem import PandasTools
from rdkit.Chem import Draw
from rdkit import DataStructs

from TransGEM.utils import *
from TransGEM.gene_ex_encoder import *
from TransGEM.evaluation import *
from TransGEM.dataset import bulit_test_dataset
from TransGEM.Model import TransGTM

# Load SELFIES dictionary
TGT_stoi=np.load(args.data_path+"TGT_stoi.npy", allow_pickle=True).item()
TGT_itos=np.load(args.data_path+"TGT_itos.npy", allow_pickle=True)

# Set device
device = torch.device(args.gpu if torch.cuda.is_available() else "cpu")

# Load test data
df=pd.read_csv(args.data_path+"{}_test.csv".format(args.dataset))

print(df.head(10))