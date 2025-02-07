# Todo App

This is a simple **To-Do List** application built with [Flet](https://flet.dev/). It allows users to add, update, filter, and delete tasks.

## Features
- Add new tasks
- Mark tasks as "To-Do", "In Progress", or "Done"
- Delete tasks
- Filter tasks by status

## Installation
### Prerequisites
- Python 3 installed
- Virtual environment (recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/todo-app.git
   cd todo-app
   ```
2. Create and activate a virtual environment:
   ```sh
   make venv
   ```
3. Install dependencies:
   ```sh
   make install
   ```

## Usage
You can run the application using the provided **Makefile**:

### Run the application:
```sh
make flet-run
```

### Run on Web (optional port):
```sh
make flet-web PORT=8000
```

### Run on Android (optional port):
```sh
make flet-android PORT=3423
```
For Android setup, refer to [Testing on Android](https://flet.dev/docs/getting-started/testing-on-android).

### Run on iOS (optional port):
```sh
make flet-ios PORT=5000
```
For iOS setup, refer to [Testing on iOS](https://flet.dev/docs/getting-started/testing-on-ios).