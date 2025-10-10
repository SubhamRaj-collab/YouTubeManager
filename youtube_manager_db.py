# Using sqlitedb to store the youtube videos data

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
    cursor.execute("SELECT * from videos")
    list = []
    list = cursor.fetchall()
    print(list)
    for row in cursor.fetchall():
        print(row)


def add_video(name, time):
    cursor.execute("INSERT into videos (name, time) VALUES (?, ?)", (name, time))
    con.commit()

def update_video(new_name, time, video_id):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, time, video_id)) # As the details are in tuple, so we are taking the values also in tuple
    con.commit()

def delete_video(video_id):
    cursor.execute("Delete from videos WHERE id = ?", (video_id,)) #We cannot write as just (video_id) because it is not considered as tuple. To make it tuple we add a comma if only one value is provided.
    con.commit()

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
                print("Exiting the app...")
                break

            case _:
                print("Invalid Input.")

    con.close() 

if __name__ == "__main__":
    main()