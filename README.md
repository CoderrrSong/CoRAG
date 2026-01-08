# CoRAG

A RAG system.

## Project Structure

```
CoRAG/
├── data/Pop/              # Test dataset
│   └── test.json         # Test samples
├── data_v33/Pop/         # Training dataset (preprocessed)
│   ├── train_labels.json      # Training labels
│   ├── train_labels_list.json # Training labels list
│   └── trans.py              # Data transformation script
├── model/
│   ├── generator-CoRAG/  # CoRAG Generator model (LoRA adapter)
│   └── reranker-CoRAG/   # CoRAG Reranker model (LoRA adapter)
├── run_train.py          # Training script
├── run_test.py           # Testing script
├── llm_local_prompt.py   # LLM Generate Function
└── utils.py              # Utility functions
```

## Quick Start

### Training

```bash
python run_train.py
```

Training data is located in the `data_v33/Pop/` directory.

### Testing

```bash
python run_test.py
```

Test data is located in the `data/Pop/` directory.

## Dataset

### Training Data (`data_v33/Pop/`)
- Preprocessed and annotated
- Contains complete training labels

### Test Data (`data/Pop/`)
- Used for model evaluation
- Contains test samples

## Models

This project uses LoRA (Low-Rank Adaptation) for fine-tuning:

- **generator-CoRAG**: Generator model adapter
- **reranker-CoRAG**: Reranker model adapter
