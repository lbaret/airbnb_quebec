import random
import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader
from torch.optim import Optimizer


# Classe pour la construction du Dataset
class AirbnbDataset(Dataset):
    def __init__(self, X, y, **kwargs):
        super(AirbnbDataset, self).__init__(**kwargs)
        self.X = X
        self.y = y

    def __getitem__(self, index):
        return self.X[index], self.y[index]

    def __len__(self):
        return len(self.X)


# Split train / test / valid
def split_data(X: np.ndarray, y: np.ndarray, train_ratio=0.8, valid_ratio=0.1):
    train_size = int(len(X) * train_ratio)
    valid_size = int(len(X) * valid_ratio)

    all_indexes = [i for i in range(len(X))]
    train_indexes = random.sample(all_indexes, k=train_size)  # Without replacement
    rem_indexes = list(set(all_indexes) - set(train_indexes))
    valid_indexes = random.sample(rem_indexes, k=valid_size)
    test_indexes = list(set(rem_indexes) - set(valid_indexes))

    if valid_size == 0:
        return X[train_indexes], X[test_indexes], y[train_indexes], y[test_indexes]

    return X[train_indexes], X[valid_indexes], X[test_indexes], y[train_indexes], y[valid_indexes], y[test_indexes]


def convert_tensor(*arrays, dtype: torch.dtype):
    return tuple([torch.tensor(arr, dtype=dtype) for arr in arrays])


# Fonctions de Deep Learning
def train(model: nn.Module, optimizer: Optimizer, loss: nn.Module, train_loader: DataLoader,
          valid_loader: DataLoader = None, epochs: int = 100, gpu: int = None, scheduler=None) -> tuple:
    """
    :param model: torch ML model
    :param optimizer: torch optimizer algorithm
    :param loss: loss function
    :param train_loader: training set
    :param valid_loader: validation set
    :param epochs: number of epochs
    :param gpu: gpu number
    :param scheduler: Learning Rate scheduler
    :return: train accuracy, train loss, validation accuracy, validation loss
    """
    # GPU
    if gpu is not None:
        model = model.cuda(gpu)

    epochs_train_loss = []
    epochs_valid_loss = []
    for ep in range(epochs):
        model.training = True

        all_losses = []
        for i, (inputs, targets) in enumerate(train_loader):
            # GPU
            if gpu is not None:
                inputs = inputs.cuda(gpu)
                targets = targets.float().cuda(gpu)

            predictions = model(inputs).squeeze()
            err = loss(predictions, targets)

            # Machine is learning
            err.backward()
            optimizer.step()
            optimizer.zero_grad()

            # Clean GPU
            if gpu is not None:
                err = err.detach().cpu()
                inputs = inputs.cpu()
                targets = targets.cpu()
                predictions = predictions.cpu()
                torch.cuda.empty_cache()

            all_losses.append(err)

            print(
                f'\rBatch : {i + 1} / {len(train_loader)} - Loss : {err:.2e}',
                end='')

        train_loss = np.vstack(all_losses).mean()

        # Historic
        epochs_train_loss.append(train_loss)

        if scheduler is not None:
            scheduler.step()

        # Validation step
        if valid_loader is not None:
            valid_loss = valid(model, loss, valid_loader, gpu)
            # Historic
            epochs_valid_loss.append(valid_loss)
            print(
                f'\rEpoch : {ep + 1} - Train Loss : {train_loss:.2e} - '
                f'- Valid Loss : {valid_loss:.2e}')
        else:
            # Display epoch information
            print(f'\rEpoch : {ep + 1} - Train Loss : {train_loss:.2e}')

    if valid_loader is not None:
        return epochs_train_loss, epochs_valid_loss

    return epochs_train_loss


def valid(model: nn.Module, loss: nn.Module, valid_loader: DataLoader, gpu) -> tuple:
    """
    :param model: torch ML model
    :param loss: loss function
    :param valid_loader: validation set
    :param gpu: gpu number
    :return: loss, accuracy
    """
    model.training = False
    with torch.no_grad():
        all_losses = []
        for i, (inputs, targets) in enumerate(valid_loader):
            if gpu is not None:
                inputs = inputs.cuda(gpu)
                targets = targets.float().cuda(gpu)

            predictions = model(inputs).squeeze()
            err = loss(predictions, targets)

            all_losses.append(err.detach().cpu())

            # Clean GPU
            if gpu is not None:
                err = err.cpu()
                inputs = inputs.cpu()
                targets = targets.cpu()
                predictions = predictions.cpu()
                torch.cuda.empty_cache()

            print(f'\rValid batch : {i + 1} / {len(valid_loader)}', end='')

        all_losses = torch.hstack(all_losses)

        return all_losses.mean()


def test(model: nn.Module, loss: nn.Module, test_loader: DataLoader, gpu: int = None) -> tuple:
    """
    :param model: torch ML model
    :param loss: loss function
    :param test_loader: test set (DataLoader)
    :param gpu: gpu number
    :return: loss, accuracy
    """
    model.training = False
    with torch.no_grad():
        all_losses = []
        for i, (inputs, targets) in enumerate(test_loader):
            if gpu is not None:
                inputs = inputs.cuda(gpu)
                targets = targets.float().cuda(gpu)

            predictions = model(inputs).squeeze()
            err = loss(predictions, targets)

            all_losses.append(err.detach().cpu())

            # Clean GPU
            if gpu is not None:
                err = err.cpu()
                inputs = inputs.cpu()
                targets = targets.cpu()
                predictions = predictions.cpu()
                torch.cuda.empty_cache()

            print(f'\rTest batch : {i + 1} / {len(test_loader)}', end='')

        all_losses = torch.vstack(all_losses)
        return all_losses.mean()


def predict(model: nn.Module, tensor_data: torch.Tensor, gpu: int = None) -> torch.Tensor:
    """
    :param model: torch ML model
    :param tensor_data: tensor of examples
    :param gpu: gpu number (default = None)
    :return: tensor of model predictions
    """
    model.training = False

    if gpu is not None:
        model = model.cuda(gpu)
        tensor_data = tensor_data.cuda(gpu)

    with torch.no_grad():
        predictions = model(tensor_data).squeeze().cpu()

    return predictions
