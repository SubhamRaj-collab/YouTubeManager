import json

def load_data():
    try:
        with open('yt_videos.txt', 'r') as file:
            test = json.load(file)
            # print("This is test data: ", test, "of type: ", type(test))
            return test
    except FileNotFoundError:
        return []
    
def save_data_helper(videos):
    with open('yt_videos.txt', 'w') as file:
        json.dump(videos, file)

def list_all_videos(videos):
    print("\n")
    print("*"*80)

    if len(videos) == 0:
        print("\n")
        print("*"*80)
        print("No Videos available")
        print("*"*80)
    for index, video in enumerate(videos, start = 1):
        print(f'{index}. Video "{video["name"]}" of duration -> {video["time"]}')
        
    print("*"*80)

def add_video(videos):
    name = input("Enter the name of the video: ")
    time = input("Enter the time of the video: ")
    videos.append({"name":name, "time":time})
    save_data_helper(videos)

def update_video(videos):
    list_all_videos(videos)
    index = int(input("Please provide the index of the video to be updated"))
    
    if index > 0  and index <= len(videos):
        name = input("Enter the name of the video to be updated: ")
        duration = input("Enter the duration of the new video to be updated.")
        videos[index-1]['name'] = name
        videos[index-1]['time'] = duration
        save_data_helper(videos)
        list_all_videos(videos)
    else:
        print("Index is Invalid. Please provide correct input.")

def delete_video(videos):
    list_all_videos(videos)
    index = int(input("Please Enter the index of the video to be deleted: "))
    if index > 0 and index <= len(videos):
        del videos[index-1]
        save_data_helper(videos)
    else:
        print("Invalid index selected.")
    
    list_all_videos(videos)

def main():

    videos = load_data()

    while True:
        print("\n Youtube Manager | Choose one of the option: ")
        print("1. List all Youtube Videos")
        print("2. Add a youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5. Exit the App")
        choice = input("Enter you Choice: ")

        # print(videos)

        match choice: 

            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                break
            case _:
                print("Invalid Input. Please try another input.")

if __name__ == "__main__": #if there is any method named main.py in this file, then excute that method
    main()
