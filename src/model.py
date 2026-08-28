from datetime import datetime, timezone

class Task:

    def __init__(self, id, description, status = "todo"):

        self.id = id
        self.description = description
        self.status = status

        self.createdAt = datetime.now(timezone.utc)
        self.updatedAt = datetime.now(timezone.utc)

    def change_id(self, id):
        self.id = id
        self.updatedAt = datetime.now(timezone.utc)

    def change_description(self, description):
        self.description = description
        self.updatedAt = datetime.now(timezone.utc)

    def change_status(self, status):
        if status == "todo" or status == "done" or status == "in-progress":
            self.status = status
            self.updatedAt = datetime.now(timezone.utc)
