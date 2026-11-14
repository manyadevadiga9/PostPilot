# POSTPILOT – Multi-Platform Social Media Scheduling Engine

## 1. Project Overview

PostPilot is a Python-based social media scheduling application that helps users organize and manage posts across multiple social media platforms.

It allows users to create posts, schedule publishing times, validate captions, maintain a weekly posting calendar, and track published or missed posts.

## 2. Technologies Used

- Python
- JSON for data storage
- VS Code

## 3. Features

1. **Create New Post:** Create posts for Instagram, Facebook, X, and LinkedIn.
2. **Character Limit Validation:** Checks captions against the configured character limit for each platform.
3. **Minimum Scheduling Gap:** Prevents posts on the same platform from being scheduled less than 30 minutes apart.
4. **Weekly Posting Calendar:** Displays scheduled posts for a selected week.
5. **Mark as Published:** Allows users to update a post's status to Published.
6. **Missed Posts Tracking:** Identifies scheduled posts whose publishing time has passed.
7. **Hashtag Warning:** Warns users when a caption contains more than five hashtags.

## 4. Project Structure

```text
POSTPILOT PROJECT/
│
├── main.py
├── posts.json
└── README.md
```

- `main.py` – Main application code.
- `posts.json` – Stores post information.
- `README.md` – Project documentation.

## 5. How to Run the Project

1. Install Python on your computer.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

```bash
python main.py
```

5. Select an option from the application menu.

## 6. Data Storage

PostPilot uses a JSON file to store post details, including:

- Post ID
- Platform
- Caption
- Scheduled date and time
- Publishing status

The saved information remains available when the application is restarted.

## 7. Limitations

- The application does not directly publish posts to social media platforms.
- Posts are managed through a console-based interface.
- Missed posts are identified when the application checks their status; there is no background notification system.
- Best posting times are not automatically predicted in the current version.

## 8. Future Enhancements

- Integrate social media APIs for automatic publishing.
- Develop a web-based user interface.
- Add notifications and reminders.
- Suggest posting times using engagement data.
- Add user login and account management.

## 9. Conclusion

PostPilot provides a simple way to organize social media posts across multiple platforms. It demonstrates Python programming, input validation, date and time handling, file handling, and JSON-based data persistence.