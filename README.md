# StudyFlow

A study planner API that tracks assignments and deadlines per course.
Built with FastAPI, SQLAlchemy and SQLite.

## Features
- Create, list, update and delete tasks
- Filter tasks by course or completion status
- Input validation and automated tests

## Run it
```bash
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Then open http://127.0.0.1:8000/docs for interactive API docs.

## Test it
```bash
pytest
```

## Roadmap
- [x] Task CRUD API with tests
- [ ] User accounts and JWT login
- [ ] Frontend
- [ ] AI-generated weekly study plan
- [ ] Deployment
