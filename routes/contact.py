from flask import Blueprint, request, jsonify
from models.contact import Contact
from utils.db import db

contact=Blueprint('contact',__name__)

@contact.route('/',methods=['GET'])
def getContactos():
    if request.method=='GET':
        data={}
        contactos=Contact.query.all()
        db.session.close()
        data['contactos']=contactos
        return jsonify(data)

@contact.route('/add',methods=['POST'])
def addContactos():
    if request.method=='POST':
        data={}
        body=request.get_json()
        fullname=body['fullname']
        email=body['email']
        phone=body['phone']

        new_contact=Contact(fullname, email, phone)
        db.session.add(new_contact)
        db.session.commit()
        db.session.close()
        return jsonify(data)

@contact.route('/update',methods=['POST'])
def updateContactos():
    if request.method=='POST':
        data={}
        body=request.get_json()
        id=body['id']
        contacto=Contact.query.get(id)
        contacto.fullname=body['fullname']
        contacto.email=body['email']
        contacto.phone=body['phone']
        
        db.session.commit()
        db.session.close()
        return jsonify(data)

@contact.route('/delete',methods=['POST'])
def deleteContactos():
    if request.method=='POST':
        data={}
        body=request.get_json()
        id=body['id']
        contacto=Contact.query.get(id)
        db.session.delete(contacto)
        db.session.commit()
        db.session.close()
        return jsonify(data)