# Income Predictor using Machine Learning

A machine learning web application that predicts whether an individual's annual income exceeds $50K based on demographic and employment-related attributes. The model is trained on census data and served through a Flask web interface.

---

## Table of Contents

- [About the Project](#about-the-project)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Clone the Repository](#clone-the-repository)
  - [Install Dependencies](#install-dependencies)
  - [Run the Application](#run-the-application)
- [How to Upload Your Own Changes](#how-to-upload-your-own-changes)
- [Accessing the Application](#accessing-the-application)
- [Contributing](#contributing)
- [Author](#author)

---

## About the Project

This project uses a pre-trained machine learning model to classify income into two categories: above or below $50K per year. The user provides inputs such as age, education, occupation, and hours worked per week, and the model returns a prediction.

The model is serialized as a `.pkl` file and loaded at runtime by the Flask application, making deployment straightforward without any retraining steps.

---

## Tech Stack

- Python 3.x
- Flask (web framework)
- scikit-learn (machine learning)
- pandas / numpy (data processing)
- pickle (model serialization)

---

## Project Structure

```
Income_Predictor_using_ML/
|-- app.py              # Main Flask application
|-- model.pkl           # Pre-trained ML model
|-- requirment.txt      # Python dependencies
|-- .gitignore          # Files excluded from version control
```

---

## Prerequisites

Before you begin, make sure the following are installed on your system:

- Python 3.7 or higher — https://www.python.org/downloads/
- pip (comes bundled with Python)
- Git — https://git-scm.com/downloads

You can verify your installations by running:

```bash
python --version
pip --version
git --version
```

---

## Getting Started

### Clone the Repository

Open your terminal and run the following command to clone the project to your local machine:

```bash
git clone https://github.com/shlokchorge2929/Income_Predictor_using_ML.git
```

Navigate into the project directory:

```bash
cd Income_Predictor_using_ML
```

### Install Dependencies

It is recommended to use a virtual environment to avoid conflicts with other Python projects.

**Create and activate a virtual environment (optional but recommended):**

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS/Linux:
```bash
python -m venv venv
source venv/bin/activate
```

**Install the required packages:**

```bash
pip install -r requirment.txt
```

### Run the Application

Once the dependencies are installed, start the Flask development server:

```bash
python app.py
```

You should see output similar to:

```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

---

## How to Upload Your Own Changes

If you have forked this repository and want to push your changes back to GitHub, follow these steps:

**Step 1: Stage your changes**

```bash
git add .
```

**Step 2: Commit with a message**

```bash
git commit -m "Your descriptive commit message here"
```

**Step 3: Push to GitHub**

```bash
git push origin main
```

If you are pushing for the first time after cloning, you may need to set the upstream branch:

```bash
git push -u origin main
```

To upload a new file or update the model, simply place it in the project directory, then repeat the add, commit, and push steps above.

---

## Accessing the Application

Once the server is running, open your browser and go to:

```
http://127.0.0.1:5000
```

or equivalently:

```
http://localhost:5000
```

Fill in the input form with the required details and click the predict button. The application will return whether the estimated income is above or below $50K per year.

**To stop the server**, go back to your terminal and press `Ctrl + C`.

---

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit them: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a pull request on GitHub

---

## Author

**Shlok Chorge**
GitHub: [@shlokchorge2929](https://github.com/shlokchorge2929)

---

> This project is intended for educational purposes. The predictions made by the model are based on historical census data and should not be used for real-world financial decisions.
