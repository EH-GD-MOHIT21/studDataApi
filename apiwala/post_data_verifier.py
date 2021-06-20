class postverifier:
    fields = [
        "name_of_student",
        "age",
        "college_name",
        "year_of_study",
        "father_name",
        "course_enrolled",
        "email",
        "address",
        "phone_no"
    ]
    def DataisNull(self,data):
        try:
            if data['name_of_student'] == "" or data['name_of_student'] == None:
                return True
            elif data['age'] == "" or data['age'] == None:
                return True
            elif data['college_name'] == "" or data['college_name'] == None:
                return True
            elif data['year_of_study'] == "" or data['year_of_study'] == None:
                return True
            elif data['father_name'] == "" or data['father_name'] == None:
                return True
            elif data['course_enrolled'] == "" or data['course_enrolled'] == None:
                return True
            elif data['email'] == "" or data['email'] == None:
                return True
            elif data['address'] == "" or data['address'] == None:
                return True
            elif data['phone_no'] == "" or data['phone_no'] == None:
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return True
    def verifyphone(self,phone):
        if phone.isnumeric() and len(phone) == 10:
            return True
        else:
            return False
    def verify_name(self,name):
        try:
            names = name.split(' ')
            for elm in names:
                if not elm.isalpha():
                    return False
            return True
        except:
            return False

    def verify_year(self,year):
        try:
            a = int(year)
            if a <= 4 and a >=0 :
                return True
            return False
        except:
            return False
    def verify_age(self,age):
        try:
            age = int(age)
            if age <= 40 and age > 0:
                return True
            return False
        except:
            return False

    def verify_mail(self,mail):
        if mail.count('@') != 1:
            return False
        if '@.' in mail:
            return False
        if mail.count('.') == 0:
            return False
        Garbage = ['!','#','$','%','^','&','*','(',')','+','{','}','[',']',';',':',"'",'"','?','/','<','>','|','`','~',"\\"]
        for letter in mail:
            if letter in Garbage:
                return False
        return True