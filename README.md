# musicbee_playlist_sync
An unconventional solution to keep my MusicBee playlists in sync with my phone, leveraging my NAS.

**The Idea:**

* MusicBee exports static versions of my auto playlists.
* This script reads those playlists, copies them to a new location, and creates hard links for the music files there.
* Syncthing then keeps the new playlist folder in sync with my phone.

**Why This Method?**

* The MusicBee Wi-Fi sync app wasn't playing ball.
* I wanted to sync music even when my desktop is off.

**Transparency Time:**

* This tool was "coded" with the help of ChatGPT 3.5 and Google Bard.
* It's a personal project and might break at any moment.
* I'm no coder at all, but I can tinker my way through, so that's what you can see here.

**Bard/GPT Files**
Given my frequent shifts between the two LMSs and experimentation with what works better, I use these two files to track the origin of the code. They are entirely optional and not included in the docker container.

**# **Version 1.0**
After numerous trials and errors, the script now accomplishes its task without crashing, reaching what I consider a release stage. It's still a bit buggy, throwing errors on some files, but those seem like minor details.

**SetUp:**

**Docker Container (Recommended):**

* Grab it from Docker Hub: https://hub.docker.com/repository/docker/tobiasdax/musicbee_playlist_sync/general
* Set these environment variables (using container paths, not host paths):
    * BASE_PLAYLIST_FOLDER: Path to the original playlists folder.
    * NEW_PLAYLIST_FOLDER: Path to save the new playlists (same relative music location as originals).
    * NEW_MUSIC_FOLDER: Path to link the music files to (I use the same path as NEW_PLAYLIST_FOLDER).
    * BASE_MUSIC_SOURCE: Path to your original music files.
* Mount a volume containing all these folders.

**Local Run:**

* Should work if you have permissions to create hard links.

**Collaboration:**

Anyone keen to help tidy up the code or make improvements is welcome!

**To-Do**
- [x] Get an initial version running
- [ ] Find out why i get so many ´[Errno 17] File exists´ errors while creating the Hardlinks
- [ ] Find out why musicbee sometimes messes up capitalization in the filepaths
- [ ] Setup the Docker so it runs regularly 
- [ ] Find out how syncthing reacts when i just delete and recreate the whole folder every time i run the tool