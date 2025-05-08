# Django + Celery Project

This is a simple project demonstrating the integration of **Django** with **Celery** for background task processing, using **Redis** as the message broker.

---

## 🚀 **Features**

* Asynchronous background task processing with Celery
* Redis as a message broker and result backend
* Django JSON response for task status

---

## 🛠️ **Requirements**

Make sure you have the following installed:

* Python 3.8+
* Django 4.x
* Celery 5.x
* Redis Server

You can install the dependencies using:

```bash
pip install django celery redis
```

---

## ⚙️ **Project Setup**

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd <your-repo-directory>
   ```

2. **Run Redis Server:**

   ```bash
   redis-server
   ```

3. **Start Celery Worker:**

   ```bash
   celery -A celery_project worker --loglevel=info
   ```

4. **Run Django Server:**

   ```bash
   python manage.py runserver
   ```

5. **Access the Application:**

   Navigate to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 **Project Structure**

```plaintext
celery_project/
├── celery_project/
│   ├── __init__.py
│   ├── settings.py
│   ├── celery.py
│   ├── urls.py
│   └── wsgi.py
├── myapp/
│   ├── __init__.py
│   ├── tasks.py
│   ├── views.py
│   └── models.py
├── manage.py
└── venv/
```

---

## 📌 **API Endpoint**

* \`\` - Triggers a background addition task and returns a JSON response with the task ID:

  **Response:**

  ```json
  {
    "task_id": "some-task-id"
  }
  ```

---

## 🔎 **Task Status Check (Optional)**

To check the status of your task:

```python
from celery.result import AsyncResult

result = AsyncResult('some-task-id')
print(result.status)  # PENDING, STARTED, SUCCESS
print(result.result)  # Task result after completion
```

---

## ✅ **Testing**

Run the server and navigate to `http://127.0.0.1:8000/`. You should see a JSON response with the task ID. You can then verify the worker logs for task execution.

---

## ✨ **Future Improvements**

* Add periodic tasks with Celery Beat
* Integrate Flower for task monitoring
* Implement retry logic for failed tasks

---

## 📜 **License**

MIT License

---

Happy coding! 😊
