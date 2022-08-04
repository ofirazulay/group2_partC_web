from utilities.db.db_manager import dbManager
from flask import session



class user:
    def _init_(self):
     pass

    def login(self, email, password):
        query = "SELECT * FROM users WHERE email ='%s' AND password ='%s'"% (email, password)
        ans = dbManager.fetch(query)
        if len(ans) == 0:
            return 'notFound'
        ans = ans[0]
        return (ans[0], ans[1], ans[2], ans[3], ans[4], ans[5])

    def sign_in_fun(self, full_name, date_of_birth, email,phone_number,username,password):
        if self.check_exist_user(email,username)=='email Exist':
            return 'email Exist'
        if self.check_exist_user(email,username)=='userName Exist':
            return 'userName Exist'
        else:
            query = "INSERT INTO users(full_name,date_of_birth,email,phone_number,username,password) VALUES ('%s','%s', '%s','%s','%s','%s')" %  (full_name, date_of_birth, email,phone_number,username,password)
            ans = dbManager.commit(query)
            return (ans)

    def update_user(self, userEmail, full_name,phone,password):
        if full_name != '':
            query = "UPDATE users SET full_name='%s'  WHERE email='%s' ;" % (full_name, userEmail)
        ans= dbManager.commit(query)
        if phone != '':
            query = "UPDATE users SET  phone_number='%s'  WHERE email='%s' ;" % (phone, userEmail)
            ans= dbManager.commit(query)
        if password != '':
            query = "UPDATE users SET  password='%s'  WHERE email='%s' ;" % (password, userEmail)
            ans= dbManager.commit(query)
        return ans

    def check_exist_user(self ,email, username):
        query = "select * FROM users WHERE email='%s';" % email
        users_with_same_email = dbManager.fetch(query)

        query = "select * FROM users WHERE username='%s';" % username
        users_with_same_name = dbManager.fetch(query)

        if len(users_with_same_email)!=0:
            return 'email Exist'
        if len(users_with_same_name) != 0:
            return 'userName Exist'
        else:
            return False





class contact:
    def _init_(self):
        pass

    def Add_contact(self, full_name, email, phone_number,review,now):
        query = "INSERT INTO contact_us(full_name,email,phone_number,review,ContactDate) VALUES ('%s', '%s', '%s','%s','%s')" % (full_name,email, phone_number,review,now)
        ans = dbManager.commit(query)
        return (ans)



class treatmentsManue:
    def _init_(self):
        pass

    def getTreatmentsMenu_Details(self):
        query = 'select * FROM treatments_type'
        ans = dbManager.fetch(query)
        return (ans)





class treatments:
    def _init_(self):
        pass
    def searchTreatments(self, user_email):
        query = "select * FROM treatments WHERE user_email='%s';" % user_email
        myTreatments = dbManager.fetch(query)
        return myTreatments


    def availableSlots(self, treatment_type):
        query = "select t.treatment_date, t.treatment_day, t.treatment_hour, t.branch_name, i.full_name from treatments as t join therapists as i on t.therapist_id= i.id where  i.treatment_type= '%s' AND t.user_email is NULL order by 1,2,3;" % treatment_type
        availableSlots= dbManager.fetch(query)
        return availableSlots

    def filteredSlots(self, treatment_type, branchName, day):
        query = "select t.treatment_date, t.treatment_day, t.treatment_hour, t.branch_name, i.full_name from treatments as t join therapists as i on t.therapist_id= i.id where  i.treatment_type= '%s' AND t.branch_name like '%s' AND t.treatment_day like '%s' AND t.user_email is NULL order by 1,2,3;" % (treatment_type, branchName, day)
        availableSlots= dbManager.fetch(query)
        return availableSlots

    def deletedTreatment(self, dateToDelete,dayToDelete,hourToDelete,TetapistToDelete,branchToDelete):
        print(dateToDelete)
        print(hourToDelete)
        print(TetapistToDelete)
        print(session['userEmail'])
        # query = "UPDATE treatments set user_email= '%s' ,ordered= '%s' where treatment_date='%s' AND treatment_hour= '%s'AND therapist_id= '%s';" % (session['userEmail'],0,dateToDelete,hourToDelete,TetapistToDelete)
        queryToRemove = "DELETE FROM treatments  where treatment_date='%s' AND treatment_hour= '%s'AND therapist_id= '%s';" % (dateToDelete,hourToDelete,TetapistToDelete)
        deletedTreatment = dbManager.commit(queryToRemove)

        queryToAddInstead="insert into treatments (treatment_date, treatment_day,treatment_hour,branch_name,therapist_id) values ('%s','%s','%s','%s','%s');" % (dateToDelete,dayToDelete,hourToDelete,branchToDelete,TetapistToDelete)
        newToAddInstead = dbManager.commit(queryToAddInstead)


        return True

    #order new Treatment

    def orderTreatment(self, treatment_type, dateToOrder,hourToOrder,TetapistToOrder,branchToOrder):
        print(self.gstNumOfReminingCards(treatment_type))
        if self.gstNumOfReminingCards(treatment_type) >0:
            self.remove1cardFromMembershipCards(treatment_type)
            self.InsertNewTreatment( dateToOrder,hourToOrder,TetapistToOrder,branchToOrder)
            return True
        else:
            return False

    def gstNumOfReminingCards(self, treatment_type):
        print(treatment_type)
        email = session['userEmail']

        query = "select totalNumOfTreatmentsRemaining FROM membership_card WHERE user_email='%s'AND treatment_type='%s' ;" % (email ,treatment_type)
        availableCards = dbManager.fetch(query)
        if len(availableCards)==0:
            return 0
        else:
            ans = availableCards
            return ans[0][0]


    def remove1cardFromMembershipCards(self, treatment_type):
        reminingCardsToUpdate=self.gstNumOfReminingCards(treatment_type)
        newNumOfCards=reminingCardsToUpdate-1
        query = "UPDATE membership_card set totalNumOfTreatmentsRemaining= '%s' where user_email='%s' AND treatment_type= '%s';" % (newNumOfCards,session['userEmail'],treatment_type)
        dbManager.commit(query)

    def InsertNewTreatment(self, dateToOrder,hourToOrder,TetapistToOrder,branchToOrder):
        terapistId=self.GetTetapistIdByName(TetapistToOrder,branchToOrder)
        query = "UPDATE treatments set user_email= '%s' ,ordered= '%s' where treatment_date='%s' AND treatment_hour= '%s'AND therapist_id= '%s';" % (session['userEmail'],1,dateToOrder,hourToOrder,terapistId)
        dbManager.commit(query)


    def GetTetapistIdByName(self, TetapistToOrder, branchToOrder):
        query = "select id FROM therapists WHERE full_name='%s'AND branch_name='%s' ;" % (TetapistToOrder ,branchToOrder)
        terapistId = dbManager.fetch(query)
        return terapistId[0][0]





class membershipCard:
    def _init_(self):
        pass
    def membership_card(self, user_email):
        query = "select * FROM membership_card WHERE user_email='%s';" % user_email
        membership_card = dbManager.fetch(query)
        return membership_card

    def calculateFullPrice(self):
        query1 = "select treatment_price from treatments_type where treatment_type='Shiatsu';"
        priceS = dbManager.fetch(query1)
        print("firstSQL")
        query2 = "select treatment_price from treatments_type where treatment_type='Reflexology';"
        priceR = dbManager.fetch(query2)
        query3 = "select treatment_price from treatments_type where treatment_type='Chinese acupuncture';"
        priceC = dbManager.fetch(query3)
        print("third")
        finalPrice = self.checkPrice(priceS[0][0], priceR[0][0], priceC[0][0])
        print(finalPrice)
        return finalPrice

    def checkPrice(self, priceS, priceR, priceC):

        fullPrice = int(priceS) * int(session['numOfShiazu'])+ int(priceR) * int(session['numOfReflexology']) + int(priceC) * int(session['numOfChinese'])
        if int(session['numOfChinese']) + int(session['numOfReflexology']) + int(session['numOfShiazu'])> 9:
            fullPrice = fullPrice * 0.9
            return fullPrice
        if int(session['numOfChinese']) + int(session['numOfReflexology']) + int(session['numOfShiazu']) > 4:
            fullPrice = fullPrice * 0.95
            return fullPrice
        else:
            return fullPrice

class payment:
    def _init_(self):
        pass

    def new_payment_fun(self, fullname,email,address,city,zip,cardname,cardnumber,expmonth,expyear,cvv ):
        query = "insert into payments (full_name,email,address,city,ZIP,card_Holder,credit_card_number,exp_month,exp_year,cvv ) values ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');" % (fullname,email,address,city,zip,cardname,cardnumber,expmonth,expyear,cvv)
        newpayment = dbManager.commit(query)
        self.uploadMembershipCard()
        return newpayment

    def uploadMembershipCard(self):
        print(session['userEmail'])
        queryS = dbManager.fetch("select * from membership_card where treatment_type='Shiatsu' AND user_email = '%s';" % session['userEmail'])
        print(queryS)
        queryR = dbManager.fetch("select * from membership_card where treatment_type='Reflexology' AND user_email = '%s';" % session['userEmail'])
        print(queryR)
        queryC = dbManager.fetch("select * from membership_card where treatment_type='Chinese acupuncture' AND user_email = '%s';" % session['userEmail'])

        if len(queryS) == 0:
            dbManager.commit("insert into membership_card values ('%s', '%s', '%s' , '%s') " % (session['userEmail'], 'Shiatsu', session['numOfShiazu'], session['numOfShiazu']))
        else:
            dbManager.commit("UPDATE membership_card set totalNumOfTreatmentsRemaining= '%s', totalNumOfTreatmentsTotal='%s' where user_email='%s' AND treatment_type= 'Shiatsu';" % (int(queryS[0][2])+ int(session['numOfShiazu']), int(queryS[0][3])+ int(session['numOfShiazu']), session['userEmail']))

        if len(queryR) == 0:
            dbManager.commit("insert into membership_card values ('%s', '%s', '%s' , '%s') " % (session['userEmail'], 'Reflexology', session['numOfReflexology'], session['numOfReflexology']))

        else:
            dbManager.commit("UPDATE membership_card set totalNumOfTreatmentsRemaining= '%s', totalNumOfTreatmentsTotal='%s' where user_email='%s' AND treatment_type= 'Reflexology';" % (int(queryR[0][2])+ int(session['numOfReflexology']), int(queryR[0][3])+ int(session['numOfReflexology']), session['userEmail']))

        if len(queryC) == 0:
            dbManager.commit("insert into membership_card values ('%s', '%s', '%s' , '%s') " % (session['userEmail'], 'Chinese acupuncture', session['numOfChinese'], session['numOfChinese']))
        else:
            dbManager.commit("UPDATE membership_card set totalNumOfTreatmentsRemaining= '%s', totalNumOfTreatmentsTotal='%s' where user_email='%s' AND treatment_type= 'Chinese acupuncture';" % (int(queryC[0][2])+ int(session['numOfChinese']), int(queryC[0][3])+ int(session['numOfChinese']), session['userEmail']))



treatmentsManue = treatmentsManue()
contact=contact()
user=user()
treatments=treatments()
membershipCard=membershipCard()
payment=payment()