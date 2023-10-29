# NeuralScan
This is an open-source application that uses Magnetoencephalography (MEG) signals and a deep neural network to detect neurological disorders.

# NeuralScan: A Detailed Guide for Usage and Contribution

## 1. Cloning the Repository

The first step to start contributing to the NeuroScan app is to clone the repository. This can be done by running the following command in your terminal:

```bash
git clone https://github.com/NeuroScan/NeuroScan.git
```

## 2. Setting up the Development Environment

Once you have cloned the repository, navigate into the project's directory:

```bash
cd NeuroScan
```

The NeuroScan app is developed using Python, so you need to have Python installed on your system. If you don't have Python installed, you can download it from the official Python website.

We recommend using a virtual environment for development. You can create a virtual environment using the following command:

```bash
python3 -m venv venv
```

Activate the virtual environment:

On Windows, run:

```bash
venv\Scripts\activate
```

On Unix or MacOS, run:

```bash
source venv/bin/activate
```

Now, install the required dependencies using:

```bash
pip install -r requirements.txt
```

## 3. Running Tests

To ensure that your changes do not break existing functionality, you should run tests before submitting a pull request. The NeuroScan app uses pytest for testing. You can run tests using the following command:

```bash
pytest
```

## 4. Making Changes

Now you are ready to make changes. Create a new branch for your changes:

```bash
git checkout -b your-branch-name
```

Make your changes and commit them:

```bash
git add .
git commit -m "Your commit message"
```

## 5. Submitting a Pull Request

Once you have made your changes, you can push them to the repository:

```bash
git push origin your-branch-name
```

Then, go to the NeuroScan GitHub page and click on "New pull request". Select your branch from the dropdown and click on "Create pull request".

## Conclusion

This guide should provide you with all the information needed to start contributing to the NeuroScan app. If you have any questions, feel free to open an issue on the GitHub repository. Happy coding!
