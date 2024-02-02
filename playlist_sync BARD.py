import os
import shutil  # Import shutil for copy2

# Define paths using Docker environment variables
base_playlist_folder = os.environ.get('BASE_PLAYLIST_FOLDER', '/mnt/media/Music/00_Exported_Playlists/')
new_playlist_folder = os.environ.get('NEW_PLAYLIST_FOLDER', '/mnt/media/MusicBee/Music_Sync/')
new_music_folder = os.environ.get('NEW_MUSIC_FOLDER', '/mnt/media/MusicBee/Music_Sync/')
base_music_source = os.environ.get('BASE_MUSIC_SOURCE', '/mnt/media/Music/')  # Add this line

# Iterate through all playlists in the base folder and its subfolders
for root, dirs, files in os.walk(base_playlist_folder):
    for file in files:
        if file.endswith('.m3u'):
            # Construct paths for the current playlist
            base_playlist_path = os.path.join(root, file)
            new_playlist_path = os.path.join(new_playlist_folder, file)

            # Copy the playlist file with metadata preservation
            os.makedirs(os.path.dirname(new_playlist_path), exist_ok=True)
            shutil.copy2(base_playlist_path, new_playlist_path)  # Use shutil.copy2

            with open(base_playlist_path, 'r') as base_playlist_file:
                # Read lines and process each track
                for line in base_playlist_file:
                    # Strip leading and trailing whitespaces, and relative folder paths
                    track_path = line.strip("./")
                    
                    print("track_paths")
                    print(track_path)

                    
                    print("base_music_source")
                    print(base_music_source)
                    print("new_music_folder")
                    print(new_music_folder)

                    # Construct the full path to the track using the base music source
                    full_track_path = os.path.join(base_music_source, track_path)
                    print("full_track_paths")
                    print(full_track_path)

                    # Construct the new music path using the new music folder
                    new_music_path = os.path.join(new_music_folder, track_path)  # Use track_path directly
                    print("new_music_path")
                    print(new_music_path)

                    # Create new paths if they don't exist
                    os.makedirs(os.path.dirname(new_music_path), exist_ok=True)

                    # Create hard link for the track
                    os.link(full_track_path, new_music_path)

print("Playlists copied and tracks hard linked successfully.")
