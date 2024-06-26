from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from sqlalchemy.ext.hybrid import hybrid_property


from config import db

class Appointment(db.Model, SerializerMixin):
    __tablename__ = 'appointments'
        
    serialize_rules = ("-doctor.appointments", '-user.appointments')

    id = db.Column(db.Integer, primary_key =True)
    date = db.Column(db.DateTime, server_default=db.func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    doctor_id = db.Column(db.Integer, db.ForeignKey('doctors.id'))

    doctor = db.relationship("Doctor", back_populates = "appointments")
    user = db.relationship("User", back_populates = "appointments")