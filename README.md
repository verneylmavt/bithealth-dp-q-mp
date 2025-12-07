# Bithealth Associate AI Engineer Pre Test: Data Processing + SQL Querying + Mini Project

This project contains the solution for the Technical Test in the context of a hospital AI system. It consists of three parts:

1. **Python - Basic Data Processing**  
   This part includes a Jupyter notebook for processing patient data. The notebook filters patient records based on age and symptom count, then outputs the results.
2. **Querying – SQL for Patient Visit Insights**  
   This part writes an SQL query to retrieve patient visit insights based on given criteria. The query extracts the most recent visits to the Neurology department, where the patient is over 50 years old and has at least 3 recorded symptoms.
3. **End-to-End Mini Project**  
   This part implements a FastAPI service that uses an LLM to recommend the most relevant hospital department based on a patient’s symptoms. It uses LangChain to communicate with the LLM and generate recommendations.

Feel free to inspect each part, run it locally, and modify as needed. [Click here to learn more about the project: bithealth-dp-q-mp/assets/Bithealth AI Pre Test.pdf](https://github.com/verneylmavt/bithealth-dp-q-mp/blob/89527f24e90d03517fd7a24a7f506ec45ffc9328/assets/Bithealth%20AI%20Pre%20Test.pdf).

## 📁 Project Structure

```
bithealth-dp-q-mp
│
├─ 1. Python - Basic Data Processing/
│  ├─ patients.csv              # Original patients data
│  ├─ filtered_patients.csv     # Filtered patients data
│  └─ filter_patients.ipynb     # Jupyter notebook for filtering patients
│
├─ 2. Querying – SQL for Patient Visit Insights/
│  ├─ query.txt                 # SQL query for patient visit insights
│  └─ query_patients.ipynb      # Jupyter notebook for querying patient visits
│
├─ 3. End-to-End Mini Project/
│  ├─ .env                      # Environment variables
│  └─ app/
│     ├─ llm_chain.py           # LLM chain logic
│     ├─ main.py                # Main application file
│     └─ models.py              # Request/Response definitions
│
└─ requirements.txt             # Python deps
```

## ⚙️ Local Setup

0. Make sure to have the prerequisites:

   - Git
   - Python
   - Conda or venv

1. Clone the repository:

   ```bash
    git clone https://github.com/verneylmavt/bithealth-dp-q-mp.git
    cd bithealth-dp-q-mp
   ```

2. Create environment and install dependencies:

   ```bash
   conda create --name bithealth-dp-q-mp python=3.11
   conda activate bithealth-dp-q-mp

   pip install -r requirements.txt
   ```

3. Run each part:
   1. **Python - Basic Data Processing**
      1. Navigate to first part directory:
         ```bash
          cd "1. Python - Basic Data Processing"
         ```
      2. Open the `filter_patients.ipynb` in Jupyter Notebook:
         ```bash
         jupyter notebook filter_patients.ipynb
         ```
      3. Execute all cells
      4. Check the filtered results in `filtered_patients.csv`
   2. **Querying – SQL for Patient Visit Insights**
      1. Navigate to second part directory:
         ```bash
          cd "2. Querying – SQL for Patient Visit Insights"
         ```
      2. Inspect the SQL Query in `query.txt`:
         ```bash
         start query.txt
         ```
      3. Open the `query_patients.ipynb` in Jupyter Notebook:
         ```bash
         jupyter notebook query_patients.ipynb
         ```
      4. Execute all cells
   3. **End-to-End Mini Project**
      1. Navigate to third part directory:
         ```bash
          cd "3. End-to-End Mini Project"
         ```
      2. Fill the required Google API Key in `.env`
      3. Run the FastAPI app:
         ```bash
         uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
         ```
      4. Make an API Call to `POST /recommend`:
         ```bash
         curl -X POST "http://localhost:8000/recommend" \
         -H "Content-Type: application/json" \
         -d '{"gender": "female", "age": 62, "symptoms": ["pusing", "mual", "sulit berjalan"]}'
         ```
      5. Alternatively, open the API documentation and see it interactively:
         ```bash
         start "http://127.0.0.1:8000/docs"
         ```
         ![API Docummentation](https://github.com/verneylmavt/bithealth-dp-q-mp/blob/89527f24e90d03517fd7a24a7f506ec45ffc9328/assets/chrome_IaRDL2Jh3R.gif)
