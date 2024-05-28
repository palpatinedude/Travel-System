import sys
sys.path.append('../database/')
from db_connector import create_connection

class Membership:
    def __init__(self, membership_id=None, membership_type=None, duration=None, membership_status=None, created_date=None):
        self.membership_id = membership_id
        self.membership_type = membership_type
        self.duration = duration
        self.membership_status = membership_status
        self.created_date = created_date

    def save(self):
        connection = create_connection()
        try:
            with connection.cursor() as cursor:
                if self.membership_id is None:
                    cursor.execute("INSERT INTO Membership (membership_type, duration, membership_status, created_date) VALUES (%s, %s, %s, %s)",
                                   (self.membership_type, self.duration, self.membership_status, self.created_date))
                    self.membership_id = cursor.lastrowid
                else:
                    cursor.execute("UPDATE Membership SET membership_type = %s, duration = %s, membership_status = %s, created_date = %s WHERE membership_id = %s",
                                   (self.membership_type, self.duration, self.membership_status, self.created_date, self.membership_id))
                connection.commit()
        except Exception as e:
            print(f"Database error: {e}")
            connection.rollback()
        finally:
            connection.close()

    def update(self, membership_type=None, duration=None, membership_status=None, created_date=None):
        if membership_type is not None:
            self.membership_type = membership_type
        if duration is not None:
            self.duration = duration
        if status is not None:
            self.membership_status = membership_status
        if created_date is not None:
            self.created_date = created_date

        self.save()