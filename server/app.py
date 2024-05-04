#!/usr/bin/env python3

# Standard library imports
from flask import Flask, request, session, jsonify, make_response
from flask_restful import Resource
from flask_migrate import Migrate

# Remote library imports
from models.user import User
from models.doctor import Doctor
from models.appointment import Appointment
from sqlalchemy.exc import IntegrityError
import datetime

# Local imports
from config import app, db, api
# Add your model imports

# @app.before_request
class CheckSession(Resource):
    def get(self):
        user = User.query.filter(User.id == session.get('user_id')).first()
        if user:
            return user.to_dict(), 200
        else:
            return {'message': '401: Not Authorized'}, 401
        
class GetUsers(Resource):
    def get(self):
        users = [user.to_dict() for user in User.query.all()]
        return users, 200 
    
class UserDetails(Resource):
    def get(self, id):
        if not session["user_id"]:
            return {"error":"unauthorized"}, 
        user = User.query.filter(User.id == id).first()
        return user.to_dict(), 200
            
class Signup(Resource):

    # def get(self):
    #     users = [user.to_dict() for user in User.query.all()]
    #     return users, 200 

    def post(self):
        password = request.get_json().get('password')
        birthdate_string = request.get_json().get('birthdate'),
        birthdate = datetime.datetime.strptime(birthdate_string[0],"%Y-%m-%d")
   
        user = User(
        username = request.get_json().get('username'),
        first_name = request.get_json().get('first_name'),
        last_name = request.get_json().get('last_name'),
        sex = request.get_json().get('sex'),
        bio = request.get_json().get('bio')
        )

        user.password_hash = password 
        user.birthdate = birthdate
        try:
            session['user_id'] = user.id
            db.session.add(user)
            db.session.commit()

            return user.to_dict(), 201

        except ValueError as exc:
            return {'message': exc}, 422
        
class Login(Resource):
    def post(self):
        
        user = User.query.filter(User.username == request.get_json()['username']).first()

        if not user:
            return {'error': 'Unauthorized'}, 401
        
        session['user_id'] = user.id
        return user.to_dict()

class Logout(Resource):
    def delete(self): 

        if not session['user_id']:
            return {'error': 'Unauthorized'}, 401

        session['user_id'] = None
        return {'message': '204: No Content'}, 204
    
class Call_Doctor(Resource):
    def get(self):

        doctors= [doc.to_dict() for doc in Doctor.query.all()]
        return doctors, 200
    
class DoctorDetails(Resource):
    def get(self, id):
        doctor = Doctor.query.filter_by(id=id).first().to_dict()
        return doctor, 200
    

        
class CreateAppointment(Resource):
    def post(self):
        date = request.get_json().get("date"),
        date_string=datetime.datetime.strptime(date[0], '%Y-%m-%dT%H:%M:%S.%fZ') 
        breakpoint()
        appointment = Appointment(
            user_id = request.get_json().get("user_id"),
            doctor_id = request.get_json().get("doctor_id"),
    )
        appointment.date = date_string
        try:
            session['user_id'] = appointment.id
            db.session.add(appointment)
            db.session.commit()

            return appointment.to_dict(), 201

        except ValueError as exc:
            return {'message': exc}, 422
    
# Views go here!
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(Call_Doctor, '/doctor', endpoint='doctor')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(GetUsers, '/users', endpoint="users")
api.add_resource(UserDetails, '/account/<int:id>')
api.add_resource(DoctorDetails, '/doctor/<int:id>')
api.add_resource(CreateAppointment, '/create', endpoint="create")

@app.route('/')
def index():
    return '<h1>Project Server</h1>'

# @app.route("/signup", methods=['GET','POST'])
# def signup():
#     if request.method == 'GET':
#         # print(([user.to_dict() for user in User.query.all()]))
#         return make_response(jsonify([user.to_dict() for user in User.query.all()]))
    
#     if request.method == 'POST':
#         data = request.get_json()
#         user = User(username=data.get('username'), first_name=data.get('first_name'),last_name=data.get('last_name'),birthdate=data.get('birthdate'),sex=data.get('sex'), bio=data.get('bio'))

#         db.session.add(user)
#         db.session.commit()

#         return make_response(
#             jsonify(
#                 {'id': user.id, 'username': user.username, 'first_name': user.first_name, 'last_name': user.last_name, "birthdate":user.birthdate, "sex":user.sex, "bio":user.bio }))
        

if __name__ == '__main__':
    app.run(port=5555, debug=True)

