
from datetime import datetime, timedelta
import json
from pathlib import Path

DATA_FILE = "posts.json"


def load_posts():
    if not Path(DATA_FILE).exists():
        return []

    with open(DATA_FILE, "r") as file:
        saved_posts = json.load(file)

    for post in saved_posts:
        post["scheduled_time"] = datetime.fromisoformat(
            post["scheduled_time"]
        )

    return saved_posts


def save_posts():
    saved_posts = []

    for post in posts:
        item = post.copy()
        item["scheduled_time"] = item["scheduled_time"].isoformat()
        saved_posts.append(item)

    with open(DATA_FILE, "w") as file:
        json.dump(saved_posts, file, indent=4)


posts = load_posts()

CHARACTER_LIMITS = {
    "Instagram": 2200,
    "Facebook": 63206,
    "X": 280,
    "LinkedIn": 3000
}

MINIMUM_GAP = 30
MAX_HASHTAGS = 5


def create_post():
    print("\n===== CREATE A NEW POST =====")

    platforms = {
        "1": "Instagram",
        "2": "Facebook",
        "3": "X",
        "4": "LinkedIn"
    }

    print("\n1. Instagram")
    print("2. Facebook")
    print("3. X")
    print("4. LinkedIn")

    platform_choice = input("Choose platform: ")

    if platform_choice not in platforms:
        print("Invalid platform!")
        return

    platform = platforms[platform_choice]

    caption = input("\nEnter your post caption: ")
    # Optional Feature: Hashtag Count Warning
    hashtags = [
        word for word in caption.split()
        if word.startswith("#")
    ]

    if len(hashtags) > MAX_HASHTAGS:
        print("\nWARNING: Too many hashtags!")
        print("Hashtags used:", len(hashtags))
        print("Recommended maximum:", MAX_HASHTAGS)
    else:
        print("Hashtag count is acceptable.")

    limit = CHARACTER_LIMITS[platform]

    if len(caption) > limit:
        print("Caption exceeds character limit!")
        print("Maximum allowed:", limit)
        return

    print("Character limit validated successfully!")

    date = input("Enter scheduled date (YYYY-MM-DD): ")
    time = input("Enter scheduled time (HH:MM): ")

    try:
        scheduled_time = datetime.strptime(
            date + " " + time, "%Y-%m-%d %H:%M"
        )
    except ValueError:
        print("Invalid date or time format!")
        return

    for post in posts:
        if post["platform"] == platform:
            gap = abs(
                (scheduled_time - post["scheduled_time"]).total_seconds()
            ) / 60

            if gap < MINIMUM_GAP:
                print("Scheduling rejected!")
                print("Minimum gap is", MINIMUM_GAP, "minutes.")
                return

    post = {
         "id": max([post["id"] for post in posts], default=0) + 1,        "caption": caption,
        "platform": platform,
        "scheduled_time": scheduled_time,
        "status": "Scheduled"
    }

    posts.append(post)
    save_posts()

    print("\nPost created successfully!")
    print("Post ID:", post["id"])
    print("Platform:", platform)
    print("Scheduled:", scheduled_time)


# Feature 4: Weekly Posting Calendar
def view_weekly_calendar():
    print("\n===== WEEKLY POSTING CALENDAR =====")

    start_date = input("Enter week starting date (YYYY-MM-DD): ")

    try:
        monday = datetime.strptime(start_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format!")
        return

    if monday.weekday() != 0:
        print("Please enter a Monday date!")
        return

    for i in range(7):
        current_day = monday + timedelta(days=i)

        print("\n--------------------------------")
        print(current_day.strftime("%A - %d-%m-%Y"))
        print("--------------------------------")

        day_posts = [
            post for post in posts
            if post["scheduled_time"].date() == current_day
        ]

        day_posts.sort(key=lambda post: post["scheduled_time"])

        if not day_posts:
            print("No posts scheduled.")

        else:
            for post in day_posts:
                print("Time:", post["scheduled_time"].strftime("%H:%M"))
                print("Platform:", post["platform"])
                print("Caption:", post["caption"])
                print("Status:", post["status"])

# Feature 5A: Update missed post status
def update_missed_posts():
    current_time = datetime.now()
    updated = False

    for post in posts:
        if (post["status"] == "Scheduled"
                and post["scheduled_time"] < current_time):

            post["status"] = "Missed"
            updated = True

    if updated:
        save_posts()


# Feature 5B: View All Posts
def view_all_posts():
    update_missed_posts()

    print("\n===== ALL POSTS =====")

    if not posts:
        print("No posts available.")
        return

    for post in posts:
        print("\n----------------------------")
        print("Post ID:", post["id"])
        print("Platform:", post["platform"])
        print("Caption:", post["caption"])
        print("Scheduled:", post["scheduled_time"])
        print("Status:", post["status"])


# Feature 5C: Mark Post as Published
def mark_published():
    print("\n===== MARK POST AS PUBLISHED =====")

    if not posts:
        print("No posts available.")
        return

    post_id = input("Enter Post ID: ")

    try:
        post_id = int(post_id)
    except ValueError:
        print("Please enter a valid Post ID!")
        return

    for post in posts:
        if post["id"] == post_id:
            if post["status"] == "Published":
                print("This post is already published!")
                return

            post["status"] = "Published"
            save_posts()

            print("\nPost marked as Published successfully!")
            return

    print("Post ID not found!")


# Feature 5D: View Missed Posts
def view_missed_posts():
    update_missed_posts()

    print("\n===== MISSED POSTS =====")

    missed = [
        post for post in posts
        if post["status"] == "Missed"
    ]

    if not missed:
        print("No missed posts!")
        return

    for post in missed:
        print("\n----------------------------")
        print("Post ID:", post["id"])
        print("Platform:", post["platform"])
        print("Caption:", post["caption"])
        print("Scheduled:", post["scheduled_time"])
        print("Status:", post["status"])


print("===================================")
print("       WELCOME TO POSTPILOT")
print("  Multi-Platform Social Media Scheduler")
print("===================================")

while True:
    print("\n1. Create a New Post")
    print("2. View All Posts")
    print("3. View Weekly Calendar")
    print("4. Mark Post as Published")
    print("5. View Missed Posts")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    
    if choice == "1":
        create_post()

    elif choice == "2":
        view_all_posts()

    elif choice == "3":
        view_weekly_calendar()

    elif choice == "4":
        mark_published()

    elif choice == "5":
        view_missed_posts()

    elif choice == "6":
        print("Thank you for using PostPilot!")
        break

    else:
        print("Invalid choice! Please try again.")
