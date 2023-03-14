import datetime


class note:
    """Заметка"""

    def __init__(self, note_id, heading, body, date_created, date_edited):
        self.note_id: int = note_id
        self.heading: str = heading
        self.body: str = body
        self.date_created = date_created
        self.date_edited = date_edited

    def refresh_edited_datetime(self):
        self.date_edited = datetime.datetime.now()
        print(datetime.datetime.now())

    def change_body(self, body):
        self.body = body

    def change_heading(self, new_heading):
        self.heading = new_heading
        self.refresh_edited_datetime()

    def append(self, body_append):
        self.change_body(self.body + "" + body_append)
        self.refresh_edited_datetime()

    def get_body(self):
        return self.body
