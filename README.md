# Daily Grind
#### Video Demo: https://www.youtube.com/watch?v=U99TeNtlIdk
#### Description:
    **Daily Grind** is a practical and user-friendly to-do list application designed to help teens efficiently manage their daily tasks. The app is geared toward making organization easy and accessible, whether it’s for keeping track of school assignments, personal goals, chores, or social activities. With its focus on simplicity, **Daily Grind** ensures that teens can keep up with their busy schedules without feeling overwhelmed.

    The app’s core functionality revolves around four main actions: viewing tasks, adding tasks, editing tasks, and removing tasks. These actions are straightforward and designed to be as intuitive as possible. The process begins with users creating tasks. Adding a task is as simple as typing in the description and hitting enter. The app then assigns each task a unique task number, making it easy to reference and manage later. This task numbering system is central to how the app organizes tasks, ensuring that each one is distinct and can be easily located when needed.

    The user interface is clean and modern, designed with teens in mind. Tasks are displayed in a table format, which makes the list easy to read and interact with. This table is generated using the `tabulate` module in Python, which provides a structured and visually appealing way to present data. The use of a tabulated format helps users quickly scan their tasks, making it easier to see what needs to be done at a glance.

    Now, let’s dive into the code that powers **Daily Grind**. The application is built in Python, using simple, yet powerful functions to manage the to-do list. The main components of the code include functions for adding, viewing, editing, and removing tasks.

    - **Adding Tasks:** The `add_task()` function is responsible for creating new tasks. When a user inputs a task description, the function assigns it a new task number by incrementing a counter. This task, along with its unique number, is then added to the list of tasks. The `tabulate` function is used to display tasks in a well-organized table, making it easy for users to see and manage their tasks.

    - **Viewing Tasks:** The `view_tasks()` function allows users to view their current tasks. If the list is empty, the app prompts users to start adding tasks. When tasks are present, they are displayed in a grid-like format, again utilizing `tabulate` for clarity and ease of reading. This function ensures that users can always see what they need to do at a glance, without any unnecessary clutter.

    - **Editing Tasks:** The `edit_task()` function provides flexibility for when users need to modify existing tasks. Since priorities can change, this function allows users to select a task by its number and update the description. The code handles this by first checking if there are tasks to edit and then verifying the task number before allowing changes. This feature is crucial for keeping the to-do list relevant and up-to-date, as it allows users to adjust their tasks as their day or week progresses.

    - **Removing Tasks:** Finally, the `remove_task()` function is there to help users clean up their to-do list. Once a task is completed or no longer needed, users can remove it from the list by entering its task number. This function is particularly useful for maintaining a focused and clutter-free list. By regularly removing completed tasks, users can keep their list manageable and ensure that they are only focusing on what’s important.

    The flow of the application is controlled by the `main()` function, which acts as the central hub. It continuously prompts the user for actions, guiding them through the process of managing their tasks. The choices are handled by the `get_user_action()` function, which displays options using the `tabulate` module and ensures that users can easily navigate through the app’s features.

    What makes **Daily Grind** stand out is its focus on user experience. The informal prompts and responses within the code make the app feel more relatable and engaging, especially for teens. For example, instead of simply stating “Invalid choice,” the app might say, “Oops! That’s not a valid option. Try again!” This kind of friendly interaction makes the app more enjoyable to use and less intimidating, encouraging teens to keep up with their tasks regularly.

    In summary, **Daily Grind** is a well-rounded to-do list application that combines a user-friendly interface with robust functionality. The Python code behind the app is designed to be simple and efficient, ensuring that all the key actions – adding, viewing, editing, and removing tasks – are easy to perform. The use of the `tabulate` module enhances the visual presentation, making the task list clear and organized. By focusing on both functionality and user experience, **Daily Grind** provides teens with an effective tool to manage their daily tasks and stay on top of their responsibilities, all while maintaining a fun and engaging interface.
