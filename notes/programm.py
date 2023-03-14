import db_editor
from ui import ui
from db_editor import *
from pathlib import Path

db_path = "db.csv"
notelist: notelist = notelist()

if Path(db_path).exists():
    db_editor.load(db_path, notelist)

ui: ui = ui(notelist)
ui.run()
db_editor.save(db_path, notelist)