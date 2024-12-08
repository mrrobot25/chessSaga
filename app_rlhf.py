import streamlit as st
import ollama
import chess.pgn
import csv
import os

# Function to extract game information from PGN
def extract_game_info_from_pgn(pgn_file):
    with open(pgn_file, 'r') as f:
        game = chess.pgn.read_game(f)

    game_info = {
        'players': {
            'white': game.headers.get('White'),
            'black': game.headers.get('Black')
        },
        'result': game.headers.get('Result'),
        'date': game.headers.get('Date'),
        'moves': [move.uci() for move in game.mainline_moves()]
    }
    return game_info

# Function to log feedback
def log_feedback(game_info, story, feedback, comment):
    try:
        feedback_file = "feedback_log.csv"
        file_exists = os.path.isfile(feedback_file)

        with open(feedback_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            if not file_exists:
                writer.writerow(["White Player", "Black Player", "Date", "Result", "Moves", "Generated Story", "Feedback", "Comment"])
            writer.writerow([
                game_info['players']['white'], game_info['players']['black'], game_info['date'],
                game_info['result'], ', '.join(game_info['moves']), story, feedback, comment
            ])
        st.success("Feedback logged successfully!")
    except Exception as e:
        st.error(f"Error logging feedback: {e}")

# Streamlit app
def main():
    # Initialize session state variables
    if "game_info" not in st.session_state:
        st.session_state.game_info = None
    if "story" not in st.session_state:
        st.session_state.story = None
    if "feedback_submitted" not in st.session_state:
        st.session_state.feedback_submitted = False

    # Load CSS file for styling
    with open("styles.css", "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # Title and Subheader
    st.markdown('<div class="title">ChessSaga: Chess Game to Story Generator</div>', unsafe_allow_html=True)
    st.markdown('<div class="subheader">Upload a PGN file to turn a chess match into a dramatic story!</div>', unsafe_allow_html=True)

    # File uploader widget
    uploaded_file = st.file_uploader("Choose a PGN file", type="pgn")

    if uploaded_file is not None:
        # Save the uploaded file temporarily
        with open("temp_game.pgn", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Extract game information from the uploaded PGN file
        st.session_state.game_info = extract_game_info_from_pgn("temp_game.pgn")

        # Prepare the prompt for the LLaMA model
        prompt = f"""
        Create an exciting and dramatic story about a chess match. The game was played between {st.session_state.game_info['players']['white']} (White) and {st.session_state.game_info['players']['black']} (Black) on {st.session_state.game_info['date']}.
        The game ended with the result of {st.session_state.game_info['result']}.
        The match proceeded with the following moves: {', '.join(st.session_state.game_info['moves'])}.
        Based on this information, create a fictionalized story with character dialogues, emotions, and a detailed description of the battle between the two players.
        """

        if st.button("Generate Story"):
            response = ollama.generate(
                model="llama3.1",
                prompt=prompt
            )
            st.session_state.story = response["response"]
            st.session_state.feedback_submitted = False  # Reset feedback state

    # Display game information and story if available
    if st.session_state.game_info and st.session_state.story:
        game_info = st.session_state.game_info
        story = st.session_state.story

        st.markdown('<div class="section-title">Game Information</div>', unsafe_allow_html=True)
        st.markdown(f"""
        <div class="game-info">
            <p><strong>White Player:</strong> {game_info['players']['white']}</p>
            <p><strong>Black Player:</strong> {game_info['players']['black']}</p>
            <p><strong>Date:</strong> {game_info['date']}</p>
            <p><strong>Result:</strong> {game_info['result']}</p>
            <p><strong>Moves:</strong> {', '.join(game_info['moves'])}</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="section-title">Generated Story</div>', unsafe_allow_html=True)
        st.markdown(f'<div class="story-box"><p>{story}</p></div>', unsafe_allow_html=True)

        # Feedback form
        if not st.session_state.feedback_submitted:
            st.markdown('<div class="section-title">Provide Your Feedback</div>', unsafe_allow_html=True)
            feedback = st.radio("How would you rate this story?", ["Amazing", "Needs Improvement"], key="feedback")
            user_comment = st.text_area("Additional comments (optional):", key="user_comment")

            if st.button("Submit Feedback"):
                if feedback:
                    log_feedback(game_info, story, feedback, user_comment)
                    st.session_state.feedback_submitted = True
                else:
                    st.warning("Please select a feedback option before submitting!")
        else:
            st.success("Thank you for your feedback!")

if __name__ == "__main__":
    main()
