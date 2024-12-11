import torch

def list_available_gpus():
    if torch.cuda.is_available():
        num_gpus = torch.cuda.device_count()
        print(f"{num_gpus} GPU(s) available:")
        for i in range(num_gpus):
            print(f"  - GPU {i}: {torch.cuda.get_device_name(i)}")
    else:
        print("No GPU available.")

list_available_gpus()

# device = torch.device(f"cuda:{args.gpu}" if torch.cuda.is_available() else "cpu")
# print(f"Using device: {device}")  # This will print whether you're using CPU or which GPU




# Automatically use GPU if available
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Dummy model and data
model = torch.nn.Linear(10, 5).to(device)  # Move model to GPU
input_data = torch.randn(100, 10).to(device)  # Move input data to GPU

# Perform computation
output = model(input_data)  # This should happen on the GPU

# Check memory allocation on the GPU
if torch.cuda.is_available():
    print(f"Allocated memory: {torch.cuda.memory_allocated() / 1024**2} MB")
    print(f"Max memory allocated: {torch.cuda.max_memory_allocated() / 1024**2} MB")
