from app.main import db

def save_changes(data) -> None:
    db.session.add(data)
    db.session.commit()