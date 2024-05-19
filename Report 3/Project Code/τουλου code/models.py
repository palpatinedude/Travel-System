from db_connector import create_connection, close_connection

class Review:
    def __init__(self, review_id=None, reviewer_id=None, reviewee_id=None, rating=None, review_text=None, review_date=None):
        self.review_id = review_id
        self.reviewer_id = reviewer_id
        self.reviewee_id = reviewee_id
        self.rating = rating
        self.review_text = review_text
        self.review_date = review_date

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        if self.review_id is None:
            try:
                cursor.execute(
                    "INSERT INTO Review (reviewer_id, reviewee_id, rating, review_text) VALUES (%s, %s, %s, %s)", 
                    (self.reviewer_id, self.reviewee_id, self.rating, self.review_text)
                )
                connection.commit()
                self.review_id = cursor.lastrowid
                print("Review added successfully")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            try:
                cursor.execute(
                    "UPDATE Review SET reviewer_id=%s, reviewee_id=%s, rating=%s, review_text=%s WHERE review_id=%s",
                    (self.reviewer_id, self.reviewee_id, self.rating, self.review_text, self.review_id)
                )
                connection.commit()
                print("Review updated successfully")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
            finally:
                cursor.close()
                close_connection(connection)

    def delete(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Review WHERE review_id=%s", (self.review_id,))
            connection.commit()
            print("Review deleted successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_all(cls):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Review")
            reviews = cursor.fetchall()
            return [cls(*row) for row in reviews]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_id(cls, review_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Review WHERE review_id=%s", (review_id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)


class Response:
    def __init__(self, response_id=None, review_id=None, replier_id=None, reply_text=None, reply_date=None):
        self.response_id = response_id
        self.review_id = review_id
        self.replier_id = replier_id
        self.reply_text = reply_text
        self.reply_date = reply_date

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        if self.response_id is None:
            try:
                cursor.execute(
                    "INSERT INTO Response (review_id, replier_id, reply_text) VALUES (%s, %s, %s)",
                    (self.review_id, self.replier_id, self.reply_text)
                )
                connection.commit()
                self.response_id = cursor.lastrowid
                print("Response added successfully")
                cursor.execute("SELECT * FROM Review")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
        else:
            try:
                cursor.execute(
                    "UPDATE Response SET review_id=%s, replier_id=%s, reply_text=%s WHERE response_id=%s",
                    (self.review_id, self.replier_id, self.reply_text, self.response_id)
                )
                connection.commit()
                print("Response updated successfully")
            except Exception as e:
                print(f"Error: {e}")
                connection.rollback()
            finally:
                cursor.close()
                close_connection(connection)

    def delete(self):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM Response WHERE response_id=%s", (self.response_id,))
            connection.commit()
            print("Response deleted successfully")
        except Exception as e:
            print(f"Error: {e}")
            connection.rollback()
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_all(cls):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Response")
            responses = cursor.fetchall()
            return [cls(*row) for row in responses]
        except Exception as e:
            print(f"Error: {e}")
            return []
        finally:
            cursor.close()
            close_connection(connection)

    @classmethod
    def get_by_id(cls, response_id):
        connection = create_connection()
        cursor = connection.cursor()
        try:
            cursor.execute("SELECT * FROM Response WHERE response_id=%s", (response_id,))
            row = cursor.fetchone()
            if row:
                return cls(*row)
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        finally:
            cursor.close()
            close_connection(connection)