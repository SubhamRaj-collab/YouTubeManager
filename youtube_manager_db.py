import sqlite3

con = sqlite3.connect('yt_vds.db')

cursor = con.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS videos (
               id INTEGER PRIMARY KEY,
               name TEXT NOT NULL, 
               time TEXT NOT NULL
    )
''')

def list_videos():
    pass

def add_video(name, time):
    pass

def update_video(name, time, video_id):
    pass

def delete_video(video_id):
    pass

def main():
    
    while True:

        print("\nYoutube Manager with DB")
        print("1. List all youtube videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video")
        print("4. Delete a youtube video")
        print("5. Exit the app")
        
        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                list_videos()

            case 2:
                name = input("Enter the video name: ")
                time = input("Enter the video duration: ")
                add_video(name, time)    

            case 3:
                video_id = int(input("Enter the Video Id to be Updated: "))
                name = input("Enter the new video name: ")
                time = input("Enter the duration of the new video: ")
                update_video(name, time, video_id)

            case 4:
                video_id = int(input("Enter the Video Id to be Deleted: "))
                delete_video(video_id)

            case 5:
                break

            case _:
                print("Invalid Input.")

if __name__ == "__main__":
    main()