# Text_summarization
please note place the pre-trained model files in the model/ directory. 
model_path: [https://drive.google.com/file/d/1o4lwHqudwirRJzVXBk3XxBTzOe4RXBmL/view?usp=sharing](https://drive.google.com/file/d/1Cf5bLVwngaK95bYHEqdfQGiUZttT4EL2/view?usp=drive_link)

### README.md for Text Summarization Project

# Text Summarization Project

Welcome to the Text Summarization Project! This project aims to automatically generate concise and coherent summaries from lengthy documents using advanced Natural Language Processing (NLP) techniques.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)

## Overview

The Text Summarization Project leverages Python and various NLP libraries to preprocess text data and train machine learning models that generate text summaries. The project includes a web application built with Flask for user interaction and visualization of results.

## Features

- **Text Preprocessing**: Clean and structure input text data for model training.
- **Model Training**: Train machine learning models to generate text summaries.
- **Web Application**: A user-friendly interface to input text and view generated summaries.
- **Visualization**: Display summaries and model performance metrics.

## Installation

To get started with the Text Summarization Project, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/text-summarization-project.git
    cd text-summarization-project
    ```

2. Create a virtual environment:
    ```bash
    python -m venv env
    source env/bin/activate  # On Windows, use `env\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Jupyter notebook to preprocess the data and train the model:
    ```bash
    jupyter notebook text-summarization-project.ipynb
    ```

2. Start the Flask web application:
    ```bash
    flask run
    ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the web interface.

## Project Structure

The project repository is structured as follows:

```
aniketbakre/Text_summarization
|   .gitignore
|   app.py
|   LICENSE
|   README.md
|   requirements.txt
|   text-summarization-project.ipynb
|   Text_summarizer_sample.JPG
|
+---model
|       config.json
|       generation_config.json
|       merges.txt
|       rng_state.pth
|       scheduler.pt
|       special_tokens_map.json
|       tokenizer_config.json
|       trainer_state.json
|       training_args.bin
|       vocab.json
|
\---templates
        index.html
```

- `app/`: Contains the Flask application files.
- `models/`: Directory for storing trained models.(you should download the model and stored from given link)
- `notebooks/`: Jupyter notebooks for data preprocessing and model training.
- `data/`: Directory for storing datasets.
- `requirements.txt`: List of project dependencies.
- `app.py`: Entry point to start the Flask web application.

## Model Training

The model training process involves the following steps:

1. **Data Preprocessing**: Load and clean the dataset to prepare it for training.
2. **Model Training**: Use machine learning algorithms to train the text summarization model.
3. **Evaluation**: Evaluate the model's performance using metrics such as ROUGE scores.
4. **Fine-Tuning**: Adjust model parameters to improve performance.

## Results

The project demonstrates the effectiveness of the text summarization model through various examples. The generated summaries are evaluated for coherence and conciseness, with performance metrics provided in the notebook.

## Contributing

Contributions are welcome! If you have any ideas or suggestions for improvement, please open an issue or create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for checking out the Text Summarization Project! If you have any questions or need further assistance, feel free to reach out. Happy summarizing!
