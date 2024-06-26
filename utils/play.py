import os
import gzip
import typing


import numpy as np
import click

import torch


# @click.command()
# @click.option(
#     "--file",
#     type=str,
#     default="/home/hli31/S2024_MLSYS/dlrm_datasets/fbgemm_t856_bs65536_0.pt",
#     help="Embedding bag data file",
# )
# @click.option(
#     "--scope",
#     nargs=2,
#     type=int,
#     default=(0, 0),
#     help="the Trace range, e.g. (1, 856)",
# )
# @click.option(
#     "--bs",
#     nargs=2,
#     type=int,
#     default=(0, 0),
#     help="the query range, e.g. (1, 65536)",
# )
# def main(file, scope, bs):
#     getDataset(file)
    
    
# def getDataset(file, factor=1):
#     try:
#         with gzip.open(file) as f:
#             indices, offsets, lengths = torch.load(f)
#     except:
#         indices, offsets, lengths = torch.load(file)
#     print(f"indices shape: {indices.shape}")
#     print(f"Offsets shape:, {offsets.shape}")
#     print(f"Lengths shape:, {lengths.shape}")
#     print()
    
#     print(f"Indices range: min {indices.min()}, max {indices.max()}")
#     print(f"Lengths range: min {lengths.min()}, max {lengths.max()}")

#     assert not torch.isinf(indices).any(), "Infinity found in indices"
#     assert not torch.isinf(lengths).any(), "Infinity found in lengths"

if __name__ == "__main__":
    config = "/home/hli31/S2024_MLSYS/Project-8/configs/prefetcher_transformer.yaml"
    d = torch.load("/home/hli31/S2024_MLSYS/Trace/fbgemm_t856_bs65536_0_trace_551_555.pt")
    a = torch.load("/home/hli31/S2024_MLSYS/Trace/fbgemm_t856_bs65536_0_trace_600_602.pt")
    print(d.shape)
    print(a.shape)
    print(len(torch.unique(d[:, 1])))
    print(len(torch.unique(a[:, 1])))
