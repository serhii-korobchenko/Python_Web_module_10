from models_mongo import Record, Phone, Adress, Email
import connect
from pymongo import MongoClient
from bson.objectid import ObjectId




# def look_up_DB (text):
#
#
#
#     """
#     SELECT r.name, r.created, p.phone_name
#     FROM records r
#     LEFT JOIN phones p ON r.id = p.rec_id
#     """
#     # result = session.query\
#     #     (Record.name, Record.created, Phone.phone_name, Email.email_name) \
#     #     .select_from(Record)\
#     #     .join(Email) \
#     #     .join(Adress) \
#     #     .join(Phone).all()
#     #
#     # print (result)
#     query_list = [(Record.name, Record.id), (Record.created, Record.id), (Email.email_name, Email.rec_id),\
#                   (Adress.adress_name, Adress.rec_id), (Phone.phone_name, Phone.rec_id)]
#     for item in query_list:
#
#         if session.query(item[0]).all():
#             #print(session.query(item[0], item[1]).all())
#             rec_id = session.query(item[1]).all()
#             #print(f'rec_id = {rec_id}')
#
#             for outer in session.query(item[0], item[1]).all():
#                 #print (outer[0])
#
#                 if type(outer[0]) != str:
#                     lookup_res = outer[0].strftime('%A %d %B %Y')
#                 else:
#                     lookup_res = outer[0]
#
#                 if lookup_res.lower().find(text.lower()) >= 0:
#                     print(
#                         f'Looked up text was found in next statement: "{lookup_res}" in record: "{session.query(Record.name).filter(Record.id == outer[1]).first()[0]}"')
#
#
#

def add_records_DB(name, phone):
    phone = Phone(name=phone)

    Record(name=name, phones=[phone, ]).save()



def change_phone_DB(name, new_phone):
    phone = Phone(name=new_phone)
    record = Record.objects(name=name)
    record.update(phones=[phone, ])


def add_phone_DB(name, phone):

    phone_add = Phone(name=phone)
    record = Record.objects(name=name)

    #for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(push__phones=phone_add)

def del_phone_DB(name, phone):

    phone_del = Phone(name=phone)
    record = Record.objects(name=name)

    #for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(pull__phones=phone_del)




def del_rec_DB(name):

    record = Record.objects(name=name)
    record.delete()

def add_email_DB(name, email):

    email_add = Email(name=email)
    record = Record.objects(name=name)

    # for r in record:
    #    print(r.to_mongo().to_dict())

    record.update_one(push__emails=email_add)

# def change_email_DB(name, new_email):
#
#
#     email1 = session.query(Email).filter(Email.rec_id == str(session.query(Record.id).filter(Record.name == name).first()[0]))
#     email1.update({'email_name': new_email})
#     session.commit()
#     session.close()
#
# def add_adress_DB(name, adress):
#
#
#     adress1 = Adress(adress_name=adress, rec_id=str(session.query(Record.id).filter(Record.name == name).first()[0]))
#     session.add(adress1)
#     session.commit()
#     session.close()
#
# def change_adress_DB(name, new_adress):
#
#
#     adress1 = session.query(Adress).filter(Adress.rec_id == str(session.query(Record.id).filter(Record.name == name).first()[0]))
#     adress1.update({'adress_name': new_adress})
#     session.commit()
#     session.close()






if __name__ == '__main__':
    add_records_DB('Andrii', '888888888')
    #change_phone_DB('Andrii', '111111111')
    #add_phone_DB('Andrii', '2222222222')
    #del_phone_DB('Andrii', '2222222222')
    #del_rec_DB('Bobo')
    add_email_DB('Andrii', '1@1.1')
    # change_email_DB('Bumba', '2@2.2')
    # add_adress_DB('Bumba', 'Vinica')
    # change_adress_DB('Bumba', 'Lviv')
    #look_up_DB ('11')





