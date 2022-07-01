from django.db import models
from django.db.models.base import Model
from django.utils import tree


# Create your models here.
class HrEmployee(models.Model):
    id = models.AutoField(primary_key=True)
    emp_pin = models.TextField()
    emp_ssn = models.TextField(blank=True, null=True)
    emp_role = models.TextField(blank=True, null=True)
    emp_firstname = models.TextField()
    emp_lastname = models.TextField(blank=True, null=True)
    emp_username = models.TextField(blank=True, null=True)
    emp_pwd = models.TextField(blank=True, null=True)
    emp_timezone = models.TextField(blank=True, null=True)
    emp_phone = models.TextField(blank=True, null=True)
    emp_payroll_id = models.TextField(blank=True, null=True)
    emp_payroll_type = models.TextField(blank=True, null=True)
    emp_pin2 = models.TextField(blank=True, null=True)
    emp_photo = models.BinaryField(blank=True, null=True)
    emp_privilege = models.TextField(blank=True, null=True)
    emp_group = models.TextField(blank=True, null=True)
    emp_hiredate = models.DateTimeField(blank=True, null=True)
    emp_address = models.TextField(blank=True, null=True)
    emp_active = models.IntegerField()
    emp_firedate = models.DateTimeField(blank=True, null=True)
    emp_firereason = models.TextField(blank=True, null=True)
    emp_emergencyphone1 = models.TextField(blank=True, null=True)
    emp_emergencyphone2 = models.TextField(blank=True, null=True)
    emp_emergencyname = models.TextField(blank=True, null=True)
    emp_emergencyaddress = models.TextField(blank=True, null=True)
    emp_cardnumber = models.TextField(db_column='emp_cardNumber', blank=True, null=True)  # Field name made lowercase.
    emp_country = models.TextField(blank=True, null=True)
    emp_city = models.TextField(blank=True, null=True)
    emp_state = models.TextField(blank=True, null=True)
    emp_postal = models.TextField(blank=True, null=True)
    emp_fax = models.TextField(blank=True, null=True)
    emp_email = models.TextField(blank=True, null=True)
    emp_title = models.TextField(blank=True, null=True)
    emp_hourlyrate1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    emp_hourlyrate2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    emp_hourlyrate3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    emp_hourlyrate4 = models.TextField(blank=True, null=True)  # This field type is a guess.
    emp_hourlyrate5 = models.TextField(blank=True, null=True)  # This field type is a guess.
    emp_gender = models.IntegerField(blank=True, null=True)
    emp_birthday = models.DateTimeField(blank=True, null=True)
    emp_operationmode = models.IntegerField(blank=True, null=True)
    isselect = models.IntegerField(db_column='IsSelect', blank=True, null=True)  # Field name made lowercase.
    middleware_id = models.BigIntegerField(blank=True, null=True)
    nationalid = models.TextField(db_column='nationalID', blank=True, null=True)  # Field name made lowercase.
    department_id = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'hr_employee'

    def __str__(self):
        return self.emp_firstname + " " + self.emp_lastname


class AttDayDetails(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    att_date = models.DateTimeField()
    timetable_id = models.IntegerField(blank=True, null=True)
    checkin = models.DateTimeField(blank=True, null=True)
    checkout = models.DateTimeField(blank=True, null=True)
    roundin = models.DateTimeField(blank=True, null=True)
    roundout = models.DateTimeField(blank=True, null=True)
    workedminutes = models.IntegerField(db_column='workedMinutes', blank=True, null=True)  # Field name made lowercase.
    rworkedminutes = models.IntegerField(db_column='rworkedMinutes', blank=True,
                                         null=True)  # Field name made lowercase.
    breakminutes = models.IntegerField(db_column='breakMinutes', blank=True, null=True)  # Field name made lowercase.
    breakrealminutes = models.IntegerField(db_column='breakRealMinutes', blank=True,
                                           null=True)  # Field name made lowercase.
    sortindex = models.IntegerField()
    iuser1 = models.IntegerField(blank=True, null=True)
    iuser2 = models.IntegerField(blank=True, null=True)
    iuser3 = models.IntegerField(blank=True, null=True)
    cuser1 = models.TextField(blank=True, null=True)
    cuser2 = models.TextField(blank=True, null=True)
    cuser3 = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    wc = models.IntegerField(blank=True, null=True)
    workcode_id = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'att_day_details'


class AttDaySummary(models.Model):
    id = models.AutoField(primary_key=True)
    att_date = models.DateTimeField()
    item_results = models.TextField(blank=True, null=True)  # This field type is a guess.
    recordsfrom = models.DateTimeField(db_column='recordsFrom')  # Field name made lowercase.
    recordsto = models.DateTimeField(db_column='recordsTo')  # Field name made lowercase.
    iuser1 = models.IntegerField(blank=True, null=True)
    iuser2 = models.IntegerField(blank=True, null=True)
    iuser3 = models.IntegerField(blank=True, null=True)
    cuser1 = models.TextField(blank=True, null=True)
    cuser2 = models.TextField(blank=True, null=True)
    cuser3 = models.TextField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    dt_id = models.IntegerField()
    item_id = models.IntegerField()
    employee_id = models.IntegerField()
    timetable_id = models.IntegerField(blank=True, null=True)
    paycode_id = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'att_day_summary'


class AttPunches(models.Model):
    id = models.AutoField(primary_key=True)
    employee_id = models.IntegerField()
    punch_time = models.DateTimeField()
    workcode = models.IntegerField(blank=True, null=True)
    workstate = models.IntegerField(blank=True, null=True)
    verifycode = models.TextField(blank=True, null=True)
    terminal_id = models.IntegerField(blank=True, null=True)
    punch_type = models.TextField(blank=True, null=True)
    operator = models.TextField(blank=True, null=True)
    operator_reason = models.TextField(blank=True, null=True)
    operator_time = models.DateTimeField(blank=True, null=True)
    isselect = models.IntegerField(db_column='IsSelect', blank=True, null=True)  # Field name made lowercase.
    middleware_id = models.BigIntegerField(blank=True, null=True)
    attendance_event = models.TextField(blank=True, null=True)
    login_combination = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    annotation = models.TextField(blank=True, null=True)
    processed = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'att_punches'


class NewAppSalary(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.OneToOneField(HrEmployee, on_delete=models.CASCADE, blank=True, null=True)
    salary = models.FloatField(default=0.0)

    def __str__(self):
        return self.employee.emp_firstname + " " + self.employee.emp_lastname

    def employee_full_name(self):
        return self.employee.emp_firstname + " " + self.employee.emp_lastname


class EmployeeSalaryPaments(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(HrEmployee, on_delete=models.CASCADE, blank=True, null=True)
    month = models.TextField(blank=True, null=True)
    paidamount = models.FloatField(blank=True, null=True, max_length=7)
    paidtime = models.DateTimeField(auto_now_add=True, null=True)
    workinghours = models.FloatField(blank=True, null=True)
    overtimehours = models.FloatField(blank=True, null=True)
    advanceTaken = models.FloatField(blank=True, null=True)
    baseSalary = models.FloatField(blank=True, null=True)
    totalEarnings = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.employee.emp_firstname + " " + self.employee.emp_lastname + " Amount: " + str(
            self.paidamount) + " BDT"


class EmployeeAdvancePayment(models.Model):
    id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(HrEmployee, on_delete=models.CASCADE)
    month = models.TextField(blank=True, null=True, max_length=7)
    advanceamount = models.FloatField(blank=True, null=True)
    paidtime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employee.emp_firstname + " " + self.employee.emp_lastname + " Amount: " + str(
            self.advanceamount) + " BDT"
