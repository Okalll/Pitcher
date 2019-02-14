from . import db

class Pitch:

    all_pitch = []


def save_pitch(self):
        Pitch.all_pitches.append(self)

@classmethod
def clear_pitches(cls):
    Pitch.all_pitchess.clear()

@classmethod
def get_pitch(cls, title):

    response = []

    for pitch in cls.all_pitches:
            if pitch.title == title:
                response.append(pitch)

    return response

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
