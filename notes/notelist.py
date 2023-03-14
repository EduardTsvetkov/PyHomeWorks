import datetime

from note import note

class notelist:
    """Книжка с записями"""

    max_id = 0
    notes: dict[int, note] = dict()

    def __init__(self):
        print("Записная книжка создана")

    def refresh_max_id(self, new_max_id):
        """Обновляет max_id в записной книжке"""
        self.max_id = new_max_id

    def import_note(self, note_id, heading, body, date_created, date_edited):
        if note_id > self.max_id:
            self.max_id = note_id
        self.notes[note_id] = note(note_id, heading, body, date_created, date_edited)

    def add_note(self, heading, body):
        self.max_id += 1
        self.notes[self.max_id] = note(self.max_id, heading, body, datetime.datetime.now(), datetime.datetime.now())

    def change_note_body(self, note_id, body):
        self.notes[note_id].change_body(body)
        self.notes[note_id].refresh_edited_datetime()

    def add_note_body(self, note_id, body):
        self.notes[note_id].append(body)
        self.notes[note_id].refresh_edited_datetime()

    def change_note_heading(self, note_id, new_heading):
        self.notes[note_id].change_heading(new_heading)
        self.notes[note_id].refresh_edited_datetime()

    def delete_note(self, note_id):
        if note_id in self.notes.keys():
            del self.notes[note_id]

    def read_note(self, note_id) -> str:
        if note_id in self.notes.keys():
            current_note = self.notes[note_id]
            note_string = "№ {0}\nДата создания: {1}\nДата изменения: {2}\n\n{3}\n\n{4}".format(
                str(current_note.note_id), str(current_note.date_created), str(current_note.date_edited),
                current_note.heading, current_note.body)
        else:
            note_string = "Заметки с таким номером не найдено"
        return note_string

    def filter_notes (self, note_id, heading, body) -> dict[int, note]:
        answer = {}
        for Note in self.notes.values():
            if note_id == Note.note_id or Note.heading.find(heading) or Note.body.find(body):
                answer[Note.note_id] = Note
        return answer

    def get_note(self, note_id) -> note:
        return self.notes[note_id]



