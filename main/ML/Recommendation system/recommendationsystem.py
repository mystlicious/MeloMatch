import pandas as pd  
import pickle  

# Load the precomputed cosine similarity matrix from a pickle file  
def load_from_pickle(filename):  
    """  
    Load data from a pickle file.  
    Parameters:  
    - filename: The name of the pickle file.  
    Returns:  
    - The loaded data.  
    """  
    with open(filename, 'rb') as f:  
        return pickle.load(f)  

# Load the combined cosine similarity matrix  
cosine_sim_combined = load_from_pickle('cosine_sim_combined.pkl')  

# Load the DataFrame containing song details from final_dataset.csv  
df = pd.read_csv('final_dataset.csv')  # Ensure this file contains the necessary columns including 'track_name', 'artist', 'track_url', 'labels'  

# Function to generate recommendations based on similarity  
def get_recommendations(song_index, cosine_sim_combined, top_n=5):  
    """  
    Get song recommendations based on cosine similarity in combined features.  
    Parameters:  
    - song_index: The index of the song for which we want recommendations.  
    - cosine_sim_combined: The cosine similarity matrix for combined features-based similarity.  
    - top_n: The number of top recommendations to return.  
    Returns:  
    - None, but prints the recommended songs in the desired format.  
    """  
    # Get the base song's details  
    base_song = df.iloc[song_index]  
    base_song_name = base_song['track_name']  
    base_artist = base_song['artist']  
    base_song_url = base_song['track_url']  # track_url from the dataset  
    
    print(f"\nRecommended Songs Based on '{base_song_name}' by '{base_artist}' | {base_song_url}:\n")  

    # Get top recommendations based on combined features  
    sim_scores = list(enumerate(cosine_sim_combined[song_index]))  
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)  
    sim_scores = sim_scores[1:top_n+1]  # Exclude the song itself (index 0)  
    song_indices = [score[0] for score in sim_scores]  
    recommended_songs = df[['track_name', 'artist', 'track_url']].iloc[song_indices]  # Including track_url  

    # Print the recommendations without similarity scores  
    seen_songs = set()  
    for song in recommended_songs.itertuples(index=False):  
        song_key = (song.track_name, song.artist)  # Use track name and artist as a unique identifier  
        if song_key not in seen_songs:  # Check for duplicates  
            print(f"'{song.track_name}' by '{song.artist}' | {song.track_url}")  
            seen_songs.add(song_key)  

# Function to filter songs by mood  
def get_random_songs_by_mood(user_mood, num_songs=10):  
    """  
    Get a random list of songs based on the user's mood.  
    Parameters:  
    - user_mood: Mood of the user ('happy' or 'sad').  
    - num_songs: Number of songs to recommend.  
    Returns:  
    - A DataFrame with song details (track_name, artist, album, track_url).  
    """  
    # Convert user mood input to numeric labels (0 = sad, 1 = happy)  
    mood_label = 0 if user_mood.lower() == "sad" else 1  

    # Filter songs based on the mood label  
    filtered_songs = df[df['labels'] == mood_label]  

    # Randomly select a subset of songs  
    selected_songs = filtered_songs.sample(n=num_songs, random_state=None)  # No fixed seed for randomness  

    # Return only user-friendly details  
    return selected_songs[['track_name', 'artist', 'album', 'track_url']]  

# Main menu function  
def main_menu():  
    print("Welcome to the Song Recommendation System!")  
    print("Choose your option:")  
    print("1. Mood-based recommendation")  
    print("2. Similarity Search")  
    print("3. Exit")  # Added an exit option  
    
    choice = input("Enter your choice (1 or 2 or 3): ")  
    
    if choice == '1':  
        mood_based_recommendation()  
    elif choice == '2':  
        similarity_search()  
    elif choice == '3':  
        print("Thank you for using the system!")  
        return  # Exit the program  
    else:  
        print("Invalid choice. Please enter 1, 2, or 3.")  
        main_menu()  # Ask again for a valid choice  

# Mood-based recommendation function  
def mood_based_recommendation():  
    print("\nHow do you feel right now?")  
    print("1. Happy")  
    print("2. Sad")  
    
    mood_choice = input("Enter your choice (1 or 2): ")  
    
    if mood_choice == '1':  
        user_mood = "happy"  
    elif mood_choice == '2':  
        user_mood = "sad"  
    else:  
        print("Invalid choice. Please enter 1 or 2.")  
        return  
    
    # Generate random recommendations based on user mood  
    try:  
        recommendations = get_random_songs_by_mood(user_mood, num_songs=10)  

        print(f"\nHere are 10 {user_mood} songs for you:\n")  
        for i, row in enumerate(recommendations.itertuples(), start=1):  
            print(f"{i}. \"{row.track_name}\" by \"{row.artist}\" from the album \"{row.album}\" | Listen here: {row.track_url}")  

    except ValueError:  
        print("No songs found for the selected mood.")  

# Similarity search function  
def similarity_search():  
    song_name = input("\nEnter the song name: ")  
    
    # Find the song index based on the song name  
    song_index = df[df['track_name'].str.lower() == song_name.lower()].index  
    
    if not song_index.empty:  
        get_recommendations(song_index[0], cosine_sim_combined, top_n=5)  
    else:  
        print("Song not found. Please check the name and try again.")  

# Run the main menu  
if __name__ == "__main__":
    main_menu()
