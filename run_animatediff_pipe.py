import argparse
from animatediff.cli import generate
import torch
from pathlib import Path


parser = argparse.ArgumentParser(description="Generate animation with Animatediff CLI")

# Add arguments to the parser
parser.add_argument( "--config_path", type=str,help="Path to the config for Animatediff")
parser.add_argument("--length", type=int, default=50, help="Length for the animation")
parser.add_argument("--width", type=int, default=400, help="Width for the animation")
parser.add_argument("--height", type=int, default=1200, help="Height for the animation")
parser.add_argument("--device", type=str, default='cuda:2', help="Device to eval")
parser.add_argument(
    "--out_dir", type=str, default='output_result_for_script_call', help="Directory to store result")

# Parse the arguments
args = parser.parse_args()

# Set the CUDA device
torch.cuda.set_device(args.device)

# Convert config path to a Path object
config_path = Path(args.config_path)

# Generate animation using the provided arguments
generate(
    config_path=config_path,
    length=args.length,
    width=args.width,
    height=args.height,
    out_dir = Path(args.out_dir),
)
