# NLP Coursework - PUSL3189

This repository contains the implementation and solutions for the NLP coursework assigned for the module **PUSL3189 - Natural Language Processing**. The coursework covers various NLP concepts such as data collection, preprocessing, sentiment analysis, topic modeling, clustering, and more, using Python and associated libraries.

## Repository Structure

```
    ├── nlp_chatbot                          # Folder for the NLP chatbot implementation
    │   ├── __pycache__                      # Python cache files
    │   ├── requirements.txt                 # Dependencies for the chatbot
    │   ├── app.py                           # API endpoint for the backend
    │   ├── chat.py                          # Chat structure
    │   ├── Neural.py                        # PyTorch model
    │   ├── nltk_code.py                     # NLTK code for the chat model
    │   ├── sl_chatbot.py                    # Streamlit frontend for the chatbot
    │   ├── slcommands.json                  # Dataset for the chatbot
    │   ├── sldata.pth                       # Data file generated from training
    │   └── training.py                      # Script to train the JSON file and create the .pth file
    ├── requirements_NLPcode.txt             # Dependencies for NLPCode environment
    ├── requirements_topicmodel.txt          # Dependencies for topicmodelenv environment
    ├── model.ipynb                          # Jupyter Notebook with full assignment code
    │                                         # (Includes comments on which environment to use)
    ├── scrape.py                            # Script used to scrape the data
    ├── t_content                            # Folder containing all outputs from model.ipynb
    ├── Scraped_content                      # Folder containing the scraped content
```

---

## How to Use

### 1. Setting Up Virtual Environments
Instead of including large `venv` folders, create virtual environments locally using the provided `requirements` files:

#### Creating Virtual Environments
Use the following commands to set up virtual environments for the respective parts of the project:

- **NLPCode**:
  ```bash
  python -m venv NLPCode
  source NLPCode/bin/activate  # On Linux/Mac
  NLPCode\Scripts\activate   # On Windows
  pip install -r requirements_NLPcode.txt
  ```

- **topicmodelenv**:
  ```bash
  python -m venv topicmodelenv
  source topicmodelenv/bin/activate  # On Linux/Mac
  topicmodelenv\Scripts\activate   # On Windows
  pip install -r requirements_topicmodel.txt
  ```

- **nlpchat**:
  ```bash
  python -m venv nlpchat
  source nlpchat/bin/activate  # On Linux/Mac
  nlpchat\Scripts\activate   # On Windows
  pip install -r nlp_chatbot/requirements.txt
  ```

### 2. Running the Scripts

#### (a) Data Scraping
1. Activate the `NLPCode` environment.
2. Run the `scrape.py` script to scrape and collect data:
   ```bash
   python scrape.py
   ```
   Outputs will be saved in the `Scraped_content` folder.

#### (b) Jupyter Notebook for Coursework Tasks
1. Open `model.ipynb` in Jupyter Notebook.
2. Follow the comments in the notebook for guidance on which virtual environment to activate for each task.

#### (c) NLP Chatbot
1. Activate the `nlpchat` environment.
2. Run the backend API:
   ```bash
   python app.py
   ```
3. Open another terminal in the same environment and run the Streamlit frontend:
   ```bash
   streamlit run sl_chatbot.py
   ```
4. Access the chatbot through the Streamlit web interface.

---

## Author
This project was developed as part of the NLP coursework for the **PUSL3189** module. By Vimuthu Thesara

---
