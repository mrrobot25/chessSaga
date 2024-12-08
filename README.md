
# ChessSaga: Chess Game to Story Generator

**ChessSaga** is an interactive app that transforms chess games into dramatic, fictionalized stories. By uploading a PGN (Portable Game Notation) file, users can generate exciting narratives that turn each chess move into a thrilling tale. The app captures the intensity of chess matches, adding character dialogues, emotions, and detailed descriptions of the battle between two players.

## Features

- Upload a **PGN file** of a chess game.
- Generates a **dramatic story** based on the game's moves, players, and results.
- Option to **provide feedback** on the generated story.
- **Feedback is logged** for improvement and future versions of the app.

## Installation

To run **ChessSaga** locally, follow the steps below:

### Prerequisites
- Python 3.x
- Streamlit
- Ollama (for model integration)
- Chess library (for parsing PGN files)

### Steps to run the app:

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   streamlit run app.py
   ```

4. Open the app in your browser (usually at `http://localhost:8501`).

## Usage

1. Upload a **PGN file** to the app.
2. Click on **Generate Story** to create a dramatic narrative.
3. Read the generated story, and provide feedback on the story quality.
4. Feedback is stored in a CSV file for future analysis.

## Technologies Used

- **Streamlit** for building the app interface.
- **Ollama** model (LLaMA) for generating stories.
- **Chess library** for reading PGN files and extracting game information.
- **CSV** for storing feedback.

## Feedback

Your feedback is valuable! Feel free to rate the generated story as **Amazing** or **Needs Improvement**, and add any additional comments to help us improve the app.

## License

This project is licensed under the MIT License

## Acknowledgements

- Special thanks to the creators of the **Streamlit** and **Chess** libraries.
- Thanks to **Ollama** for providing the LLaMA model used for story generation.
