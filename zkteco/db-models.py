# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Pushqueue(models.Model):
    id = models.AutoField(blank=True, null=True)
    content = models.TextField(db_column='Content')  # Field name made lowercase.
    destination = models.TextField(db_column='Destination')  # Field name made lowercase.
    cuser1 = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Pushqueue'


class Reporttemplate(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    title = models.TextField(db_column='Title')  # Field name made lowercase.
    template = models.BinaryField(db_column='Template', blank=True, null=True)  # Field name made lowercase.
    reportid = models.TextField(db_column='ReportID')  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ReportTemplate'


class SysConfig(models.Model):
    id = models.AutoField(db_column='ID', blank=True, null=True)  # Field name made lowercase.
    configtype = models.SmallIntegerField(db_column='ConfigType', unique=True)  # Field name made lowercase.
    data = models.BinaryField(db_column='Data', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Sys_Config'


class AcGroup(models.Model):
    id = models.AutoField(blank=True, null=True)
    acgroup_id = models.IntegerField()
    acgroup_name = models.TextField(blank=True, null=True)
    acgroup_holidayvalid = models.BooleanField(db_column='acgroup_holidayValid', blank=True, null=True)  # Field name made lowercase.
    acgroup_verifystytle = models.IntegerField(blank=True, null=True)
    timezone1 = models.IntegerField(blank=True, null=True)
    timezone2 = models.IntegerField(blank=True, null=True)
    timezone3 = models.IntegerField(blank=True, null=True)
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ac_group'


class AcHolidaysetting(models.Model):
    holiday_id = models.AutoField()
    holiday_name = models.TextField(blank=True, null=True)
    holiday_start = models.DateTimeField(blank=True, null=True)
    holiday_end = models.DateTimeField(blank=True, null=True)
    actimezoneid = models.IntegerField(db_column='acTimezoneId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ac_holidaysetting'


class AcTimezone(models.Model):
    timezone_id = models.AutoField()
    timezone_name = models.TextField(blank=True, null=True)
    timezone_sunstart = models.DateTimeField(db_column='timezone_SunStart', blank=True, null=True)  # Field name made lowercase.
    timezone_sunend = models.DateTimeField(db_column='timezone_SunEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_monstart = models.DateTimeField(db_column='timezone_MonStart', blank=True, null=True)  # Field name made lowercase.
    timezone_monend = models.DateTimeField(db_column='timezone_MonEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_tuesstart = models.DateTimeField(db_column='timezone_TuesStart', blank=True, null=True)  # Field name made lowercase.
    timezone_tuesend = models.DateTimeField(db_column='timezone_TuesEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_wedstart = models.DateTimeField(db_column='timezone_WedStart', blank=True, null=True)  # Field name made lowercase.
    timezone_wedend = models.DateTimeField(db_column='timezone_WedEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_thursstart = models.DateTimeField(db_column='timezone_ThursStart', blank=True, null=True)  # Field name made lowercase.
    timezone_thursend = models.DateTimeField(db_column='timezone_ThursEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_fristart = models.DateTimeField(db_column='timezone_FriStart', blank=True, null=True)  # Field name made lowercase.
    timezone_friend = models.DateTimeField(db_column='timezone_FriEnd', blank=True, null=True)  # Field name made lowercase.
    timezone_satstart = models.DateTimeField(db_column='timezone_SatStart', blank=True, null=True)  # Field name made lowercase.
    timezone_satend = models.DateTimeField(db_column='timezone_SatEnd', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ac_timezone'


class AcUnlockcomb(models.Model):
    id = models.AutoField(blank=True, null=True)
    unlockcomb_id = models.IntegerField(db_column='unlockComb_id')  # Field name made lowercase.
    unlockcomb_name = models.TextField(db_column='unlockComb_name', blank=True, null=True)  # Field name made lowercase.
    acgroup1 = models.IntegerField(blank=True, null=True)
    acgroup2 = models.IntegerField(blank=True, null=True)
    acgroup3 = models.IntegerField(blank=True, null=True)
    acgroup4 = models.IntegerField(blank=True, null=True)
    acgroup5 = models.IntegerField(blank=True, null=True)
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ac_unlockComb'


class AcUserprivilege(models.Model):
    id = models.AutoField(blank=True, null=True)
    isusergroup = models.BooleanField(db_column='isUserGroup', blank=True, null=True)  # Field name made lowercase.
    verifystytle = models.IntegerField(blank=True, null=True)
    disable = models.BooleanField(blank=True, null=True)
    employee_id = models.IntegerField()
    terminal_id = models.IntegerField()
    timezone1 = models.IntegerField(blank=True, null=True)
    timezone2 = models.IntegerField(blank=True, null=True)
    timezone3 = models.IntegerField(blank=True, null=True)
    acgroup_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ac_userPrivilege'


class AttDaytype(models.Model):
    id = models.AutoField(blank=True, null=True)
    dt_code = models.IntegerField()
    dt_desc = models.TextField(blank=True, null=True)
    export_code = models.TextField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_DayType'


class AttDepartmentleavetype(models.Model):
    id = models.AutoField(blank=True, null=True)
    dl_code = models.IntegerField()
    yearlylimit = models.TextField(db_column='yearlyLimit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    department_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_DepartmentLeaveType'


class AttEmployeeleavetype(models.Model):
    id = models.AutoField(blank=True, null=True)
    el_code = models.IntegerField()
    yearlylimit = models.TextField(db_column='yearlyLimit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_EmployeeLeaveType'


class AttStatisticitem(models.Model):
    id = models.AutoField(blank=True, null=True)
    item_code = models.IntegerField()
    item_desc = models.TextField(blank=True, null=True)
    item_type = models.IntegerField(blank=True, null=True)
    export_code = models.TextField(blank=True, null=True)
    isdeleted = models.BooleanField(db_column='isDeleted', blank=True, null=True)  # Field name made lowercase.
    sign = models.TextField(blank=True, null=True)
    yearlylimit = models.TextField(db_column='yearlyLimit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    item_mode = models.IntegerField(db_column='item_Mode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_StatisticItem'


class AttBreak(models.Model):
    id = models.AutoField(blank=True, null=True)
    break_name = models.TextField(blank=True, null=True)
    break_start = models.DateTimeField()
    break_end = models.DateTimeField()
    break_deductminute = models.IntegerField(blank=True, null=True)
    break_autodeduct = models.BooleanField(blank=True, null=True)
    break_needcheck = models.BooleanField(blank=True, null=True)
    break_advance = models.DateTimeField(blank=True, null=True)
    break_delay = models.DateTimeField(blank=True, null=True)
    break_validworktime = models.BooleanField(db_column='break_ValidWorkTime', blank=True, null=True)  # Field name made lowercase.
    break_overcount = models.BooleanField(blank=True, null=True)
    break_overcount_paycode = models.IntegerField(blank=True, null=True)
    break_overminutes = models.IntegerField(blank=True, null=True)
    break_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_break'


class AttBreakDetails(models.Model):
    id = models.AutoField(blank=True, null=True)
    breakout = models.DateTimeField(blank=True, null=True)
    breakin = models.DateTimeField(blank=True, null=True)
    minutes = models.IntegerField(blank=True, null=True)
    roundminutes = models.IntegerField(blank=True, null=True)
    remark = models.TextField(blank=True, null=True)
    ddetail_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_break_details'


class AttBreakTimetable(models.Model):
    break_id = models.IntegerField()
    timetable_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_break_timetable'


class AttDayDetails(models.Model):
    id = models.AutoField(blank=True, null=True)
    employee_id = models.IntegerField()
    att_date = models.DateTimeField()
    timetable_id = models.IntegerField(blank=True, null=True)
    checkin = models.DateTimeField(blank=True, null=True)
    checkout = models.DateTimeField(blank=True, null=True)
    roundin = models.DateTimeField(blank=True, null=True)
    roundout = models.DateTimeField(blank=True, null=True)
    workedminutes = models.IntegerField(db_column='workedMinutes', blank=True, null=True)  # Field name made lowercase.
    rworkedminutes = models.IntegerField(db_column='rworkedMinutes', blank=True, null=True)  # Field name made lowercase.
    breakminutes = models.IntegerField(db_column='breakMinutes', blank=True, null=True)  # Field name made lowercase.
    breakrealminutes = models.IntegerField(db_column='breakRealMinutes', blank=True, null=True)  # Field name made lowercase.
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

    class Meta:
        managed = False
        db_table = 'att_day_details'


class AttDaySummary(models.Model):
    id = models.AutoField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'att_day_summary'


class AttDepartmentShift(models.Model):
    id = models.AutoField(blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    noenddate = models.BooleanField(db_column='NoEndDate', blank=True, null=True)  # Field name made lowercase.
    department_id = models.IntegerField()
    shift_id = models.IntegerField()
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_department_shift'


class AttDepartmentSmartshift(models.Model):
    id = models.AutoField(blank=True, null=True)
    department_id = models.IntegerField()
    shift_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_department_smartshift'


class AttEmployeeShift(models.Model):
    id = models.AutoField(blank=True, null=True)
    startdate = models.DateTimeField(db_column='startDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='endDate', blank=True, null=True)  # Field name made lowercase.
    noenddate = models.BooleanField(db_column='NoEndDate', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField()
    shift_id = models.IntegerField()
    modifydate = models.DateTimeField(db_column='modifyDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_employee_shift'


class AttEmployeeSmartshift(models.Model):
    id = models.AutoField(blank=True, null=True)
    employee_id = models.IntegerField()
    shift_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_employee_smartshift'


class AttEmployeeTempShift(models.Model):
    id = models.AutoField(blank=True, null=True)
    schdate = models.DateTimeField(db_column='schDate', blank=True, null=True)  # Field name made lowercase.
    employee_id = models.IntegerField(blank=True, null=True)
    daytypecode = models.IntegerField(db_column='dayTypeCode')  # Field name made lowercase.
    timetable_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    paycode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_employee_temp_shift'


class AttEmployeeZone(models.Model):
    employee_id = models.IntegerField()
    zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_employee_zone'


class AttExceptionassign(models.Model):
    id = models.AutoField(blank=True, null=True)
    exception_date = models.DateTimeField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)
    daytypecode = models.IntegerField(db_column='dayTypeCode')  # Field name made lowercase.
    timetable_id = models.IntegerField(blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    starttime = models.DateTimeField(blank=True, null=True)
    endtime = models.DateTimeField(blank=True, null=True)
    paycode_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_exceptionassign'


class AttFlexibletimetable(models.Model):
    id = models.AutoField(blank=True, null=True)
    daychangeat = models.DateTimeField(db_column='dayChangeAt', blank=True, null=True)  # Field name made lowercase.
    requirework = models.IntegerField(db_column='requireWork', blank=True, null=True)  # Field name made lowercase.
    firstinlastout = models.BooleanField(db_column='firstInLastOut', blank=True, null=True)  # Field name made lowercase.
    enableot = models.BooleanField(db_column='enableOT', blank=True, null=True)  # Field name made lowercase.
    otl1available = models.BooleanField(blank=True, null=True)
    otl1minutes = models.IntegerField(blank=True, null=True)
    otl2available = models.BooleanField(blank=True, null=True)
    otl2minutes = models.IntegerField(blank=True, null=True)
    otl3available = models.BooleanField(blank=True, null=True)
    otl3minutes = models.IntegerField(blank=True, null=True)
    timetable_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_flexibleTimetable'


class AttPunches(models.Model):
    id = models.AutoField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'att_punches'


class AttShift(models.Model):
    id = models.AutoField(blank=True, null=True)
    shift_name = models.TextField()
    cycle_available = models.BooleanField()
    cycle_type = models.IntegerField(blank=True, null=True)
    cycle_parameter = models.IntegerField(blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    defaultshift = models.BooleanField(db_column='defaultShift', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_shift'


class AttShiftDetails(models.Model):
    id = models.AutoField(blank=True, null=True)
    shift_date = models.DateTimeField()
    daytypecode = models.IntegerField(db_column='dayTypeCode', blank=True, null=True)  # Field name made lowercase.
    timetable_paycode = models.IntegerField(blank=True, null=True)
    shift_id = models.IntegerField()
    timetable_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'att_shift_details'


class AttTerminal(models.Model):
    id = models.AutoField(blank=True, null=True)
    terminal_no = models.IntegerField()
    terminal_status = models.IntegerField()
    terminal_name = models.TextField(blank=True, null=True)
    terminal_location = models.TextField(blank=True, null=True)
    terminal_category = models.IntegerField()
    terminal_type = models.TextField(blank=True, null=True)
    terminal_connectpwd = models.TextField(blank=True, null=True)
    terminal_domainname = models.TextField(blank=True, null=True)
    terminal_dateformat = models.TextField(blank=True, null=True)
    terminal_tcpip = models.TextField(blank=True, null=True)
    agr_version = models.TextField(db_column='AGR_version', blank=True, null=True)  # Field name made lowercase.
    terminal_port = models.IntegerField(blank=True, null=True)
    terminal_baudrate = models.IntegerField(blank=True, null=True)
    terminal_users = models.IntegerField(blank=True, null=True)
    terminal_fingerprints = models.IntegerField(blank=True, null=True)
    terminal_faces = models.IntegerField(blank=True, null=True)
    terminal_palms = models.IntegerField(blank=True, null=True)
    terminal_fvs = models.IntegerField(blank=True, null=True)
    terminal_punches = models.IntegerField(blank=True, null=True)
    isselect = models.IntegerField(db_column='IsSelect', blank=True, null=True)  # Field name made lowercase.
    terminal_sn = models.BigIntegerField(blank=True, null=True)
    terminal_sns = models.TextField(blank=True, null=True)
    policy = models.IntegerField(blank=True, null=True)
    first_connect = models.BooleanField(blank=True, null=True)
    terminal_desc = models.TextField(blank=True, null=True)
    terminal_photostamp = models.TextField(blank=True, null=True)
    terminal_attlogstamp = models.TextField(db_column='terminal_AttLogStamp', blank=True, null=True)  # Field name made lowercase.
    punchstamp = models.DateTimeField(db_column='PunchStamp', blank=True, null=True)  # Field name made lowercase.
    isfromwdms = models.IntegerField(db_column='isfromWDMS', blank=True, null=True)  # Field name made lowercase.
    connection_model = models.IntegerField(blank=True, null=True)
    terminal_zem = models.TextField(blank=True, null=True)
    terminal_firmversion = models.TextField(blank=True, null=True)
    terminal_admins = models.IntegerField(blank=True, null=True)
    p2puid = models.TextField(db_column='p2pUID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_terminal'


class AttTerminalEvents(models.Model):
    id = models.AutoField(blank=True, null=True)
    occurtime = models.DateTimeField(blank=True, null=True)
    actionname = models.TextField(blank=True, null=True)
    contentdata = models.TextField(blank=True, null=True)
    verifymode = models.TextField(blank=True, null=True)
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_terminal_events'


class AttTerminalZone(models.Model):
    terminal_id = models.IntegerField()
    zone_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_terminal_zone'


class AttTimetable(models.Model):
    id = models.AutoField(blank=True, null=True)
    timetabletype = models.IntegerField(db_column='timetableType', blank=True, null=True)  # Field name made lowercase.
    timetable_color = models.IntegerField(blank=True, null=True)
    timetable_name = models.TextField(blank=True, null=True)
    timetable_start = models.DateTimeField(blank=True, null=True)
    timetable_end = models.DateTimeField(blank=True, null=True)
    timetable_checkin_begin = models.DateTimeField(blank=True, null=True)
    timetable_checkout_end = models.DateTimeField(blank=True, null=True)
    usedforsmartshift = models.BooleanField(db_column='usedForSmartShift', blank=True, null=True)  # Field name made lowercase.
    timetable_checkin_end = models.DateTimeField(blank=True, null=True)
    timetable_checkout_begin = models.DateTimeField(blank=True, null=True)
    requirework = models.IntegerField(db_column='requireWork', blank=True, null=True)  # Field name made lowercase.
    timetable_late = models.BooleanField(blank=True, null=True)
    timetable_latecome = models.IntegerField(blank=True, null=True)
    timetable_early = models.BooleanField(blank=True, null=True)
    timetable_earlyout = models.IntegerField(blank=True, null=True)
    countabsentlateexceed = models.BooleanField(db_column='countAbsentLateExceed', blank=True, null=True)  # Field name made lowercase.
    countabsentlateexceedmins = models.IntegerField(db_column='countAbsentLateExceedMins', blank=True, null=True)  # Field name made lowercase.
    withoutinaslateallday = models.BooleanField(db_column='withoutInAsLateAllDay', blank=True, null=True)  # Field name made lowercase.
    countabsentearlyexceed = models.BooleanField(db_column='countAbsentEarlyExceed', blank=True, null=True)  # Field name made lowercase.
    countabsentearlyexceedmins = models.IntegerField(db_column='countAbsentEarlyExceedMins', blank=True, null=True)  # Field name made lowercase.
    withoutoutasearlyallday = models.BooleanField(db_column='withoutOutAsEarlyAllDay', blank=True, null=True)  # Field name made lowercase.
    enableot = models.BooleanField(db_column='enableOT', blank=True, null=True)  # Field name made lowercase.
    earlycomeaswork = models.BooleanField(db_column='earlyComeAsWork', blank=True, null=True)  # Field name made lowercase.
    countearlycomeexceedmins = models.IntegerField(db_column='countEarlyComeExceedMins', blank=True, null=True)  # Field name made lowercase.
    lateoutaswork = models.BooleanField(db_column='lateOutAsWork', blank=True, null=True)  # Field name made lowercase.
    countlateoutexceedmins = models.IntegerField(db_column='countLateOutExceedMins', blank=True, null=True)  # Field name made lowercase.
    firstinlastout = models.BooleanField(db_column='firstInLastOut', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='isDefault', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_timetable'


class AttTimetableRoundrule(models.Model):
    id = models.AutoField(blank=True, null=True)
    timefrom = models.DateTimeField()
    timeto = models.DateTimeField()
    roundtime = models.DateTimeField()
    timetable_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'att_timetable_roundrule'


class AttWorkcode(models.Model):
    id = models.AutoField(blank=True, null=True)
    wc_code = models.IntegerField()
    wc_name = models.TextField()
    middleware_code = models.TextField(blank=True, null=True)
    middleware_id = models.BigIntegerField(blank=True, null=True)
    wc_type = models.BigIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    hourly_payment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'att_workcode'


class AttWorkstate(models.Model):
    id = models.AutoField(blank=True, null=True)
    ws_code = models.IntegerField()
    ws_alias = models.TextField()

    class Meta:
        managed = False
        db_table = 'att_workstate'


class AttZone(models.Model):
    id = models.AutoField(blank=True, null=True)
    zone_code = models.IntegerField()
    clientid = models.BigIntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    zonename = models.TextField(db_column='ZoneName')  # Field name made lowercase.
    zoneid = models.BigIntegerField(db_column='zoneID', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    iuser1 = models.IntegerField(blank=True, null=True)
    cuser1 = models.TextField(blank=True, null=True)
    isselect = models.IntegerField(db_column='IsSelect', blank=True, null=True)  # Field name made lowercase.
    defaultzone = models.IntegerField(db_column='defaultZone', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'att_zone'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HrAttendancerule(models.Model):
    id = models.AutoField(blank=True, null=True)
    smartshiftdisplaycolor = models.IntegerField(db_column='smartShiftDisplayColor', blank=True, null=True)  # Field name made lowercase.
    requirepunchforleave = models.BooleanField(db_column='requirePunchForLeave', blank=True, null=True)  # Field name made lowercase.
    activeattstatus = models.BooleanField(db_column='activeAttStatus', blank=True, null=True)  # Field name made lowercase.
    minimumtime = models.IntegerField(db_column='minimumTime', blank=True, null=True)  # Field name made lowercase.
    hourlydaychangeat = models.DateTimeField(db_column='hourlyDayChangeAt', blank=True, null=True)  # Field name made lowercase.
    hourlyfirstinlastout = models.BooleanField(db_column='hourlyFirstInLastOut', blank=True, null=True)  # Field name made lowercase.
    hourlyactiveattstatus = models.BooleanField(db_column='hourlyActiveAttStatus', blank=True, null=True)  # Field name made lowercase.
    hourlyminimumtime = models.IntegerField(db_column='hourlyMinimumTime', blank=True, null=True)  # Field name made lowercase.
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_attendanceRule'


class HrBiotemplate(models.Model):
    id = models.AutoField(blank=True, null=True)
    valid_flag = models.IntegerField()
    is_duress = models.IntegerField()
    bio_type = models.IntegerField()
    version = models.TextField()
    data_format = models.IntegerField()
    template_no = models.IntegerField()
    template_no_index = models.IntegerField()
    template_data = models.TextField(blank=True, null=True)
    size = models.IntegerField()
    employee_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_biotemplate'


class HrCompany(models.Model):
    id = models.AutoField(blank=True, null=True)
    cmp_code = models.TextField(blank=True, null=True)
    cmp_dateformat = models.TextField(blank=True, null=True)
    cmp_timeformat = models.TextField(blank=True, null=True)
    cmp_name = models.TextField()
    cmp_operationmode = models.IntegerField(blank=True, null=True)
    cmp_address1 = models.TextField(blank=True, null=True)
    cmp_address2 = models.TextField(blank=True, null=True)
    cmp_city = models.TextField(blank=True, null=True)
    cmp_state = models.TextField(blank=True, null=True)
    cmp_country = models.TextField(blank=True, null=True)
    cmp_postal = models.TextField(blank=True, null=True)
    cmp_phone = models.TextField(blank=True, null=True)
    cmp_fax = models.TextField(blank=True, null=True)
    cmp_email = models.TextField(blank=True, null=True)
    cmp_logo = models.BinaryField(blank=True, null=True)
    cmp_showlogoinreport = models.BooleanField(db_column='cmp_showlogoInreport', blank=True, null=True)  # Field name made lowercase.
    cmp_website = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_company'


class HrDeleteEmployee(models.Model):
    id = models.AutoField(blank=True, null=True)
    emp_pin = models.TextField()
    terminal_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_delete_employee'


class HrDepartment(models.Model):
    id = models.AutoField(blank=True, null=True)
    dept_code = models.IntegerField()
    dept_name = models.TextField()
    dept_parentcode = models.IntegerField()
    usecode = models.BooleanField(db_column='useCode', blank=True, null=True)  # Field name made lowercase.
    dept_operationmode = models.IntegerField(blank=True, null=True)
    middleware_id = models.BigIntegerField(blank=True, null=True)
    defaultdepartment = models.IntegerField(db_column='defaultDepartment', blank=True, null=True)  # Field name made lowercase.
    description = models.TextField(blank=True, null=True)
    company_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_department'


class HrEmployee(models.Model):
    id = models.AutoField(blank=True, null=True)
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

    class Meta:
        managed = False
        db_table = 'hr_employee'


class HrEmployeeGroup(models.Model):
    employee_id = models.IntegerField()
    groupitem_id = models.IntegerField(db_column='groupItem_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hr_employee_group'


class HrGroup(models.Model):
    id = models.AutoField(blank=True, null=True)
    group_name = models.TextField()
    employees = models.TextField()

    class Meta:
        managed = False
        db_table = 'hr_group'


class HrGroupitem(models.Model):
    id = models.AutoField(blank=True, null=True)
    grp_item_id = models.IntegerField()
    grp_item_desc = models.TextField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_groupItem'


class HrHolidayDetails(models.Model):
    id = models.AutoField(blank=True, null=True)
    hor_code = models.IntegerField(blank=True, null=True)
    hor_name = models.TextField(blank=True, null=True)
    holidaysotmode = models.IntegerField(db_column='HolidaysOTMode', blank=True, null=True)  # Field name made lowercase.
    holidaysotenabled = models.BooleanField(db_column='HolidaysOTEnabled', blank=True, null=True)  # Field name made lowercase.
    holidaysot1limit = models.TextField(db_column='HolidaysOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    holidaysot2limit = models.TextField(db_column='HolidaysOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    holidaysot3limit = models.TextField(db_column='HolidaysOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    hor_cycletype = models.IntegerField(db_column='hor_cycleType', blank=True, null=True)  # Field name made lowercase.
    hor_days = models.IntegerField(blank=True, null=True)
    hor_date = models.DateTimeField(blank=True, null=True)
    hor_month_cycleyear = models.IntegerField(db_column='hor_month_cycleYear', blank=True, null=True)  # Field name made lowercase.
    hor_day_cycleyear = models.IntegerField(db_column='hor_day_cycleYear', blank=True, null=True)  # Field name made lowercase.
    hor_month_cycledate = models.IntegerField(db_column='hor_month_cycleDate', blank=True, null=True)  # Field name made lowercase.
    hor_weeks_cycledate = models.IntegerField(db_column='hor_weeks_cycleDate', blank=True, null=True)  # Field name made lowercase.
    hor_week_cycledate = models.IntegerField(db_column='hor_week_cycleDate', blank=True, null=True)  # Field name made lowercase.
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_holiday_details'


class HrPayclass(models.Model):
    id = models.AutoField(blank=True, null=True)
    weekdayotmode = models.IntegerField(db_column='WeekDayOTMode', blank=True, null=True)  # Field name made lowercase.
    sundayot1limit = models.TextField(db_column='SundayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sundayot2limit = models.TextField(db_column='SundayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    sundayot3limit = models.TextField(db_column='SundayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mondayot1limit = models.TextField(db_column='MondayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mondayot2limit = models.TextField(db_column='MondayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    mondayot3limit = models.TextField(db_column='MondayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tuesdayot1limit = models.TextField(db_column='TuesdayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tuesdayot2limit = models.TextField(db_column='TuesdayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    tuesdayot3limit = models.TextField(db_column='TuesdayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wednesdayot1limit = models.TextField(db_column='WednesdayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wednesdayot2limit = models.TextField(db_column='WednesdayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    wednesdayot3limit = models.TextField(db_column='WednesdayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thursdayot1limit = models.TextField(db_column='ThursdayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thursdayot2limit = models.TextField(db_column='ThursdayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    thursdayot3limit = models.TextField(db_column='ThursdayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fridayot1limit = models.TextField(db_column='FridayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fridayot2limit = models.TextField(db_column='FridayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    fridayot3limit = models.TextField(db_column='FridayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saturdayot1limit = models.TextField(db_column='SaturdayOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saturdayot2limit = models.TextField(db_column='SaturdayOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    saturdayot3limit = models.TextField(db_column='SaturdayOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weekendsotmode = models.IntegerField(db_column='WeekendsOTMode', blank=True, null=True)  # Field name made lowercase.
    weekendsotenabled = models.BooleanField(db_column='WeekendsOTEnabled', blank=True, null=True)  # Field name made lowercase.
    weekendsot1limit = models.TextField(db_column='WeekendsOT1Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weekendsot2limit = models.TextField(db_column='WeekendsOT2Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weekendsot3limit = models.TextField(db_column='WeekendsOT3Limit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    weekendset = models.TextField(db_column='WeekendSet', blank=True, null=True)  # Field name made lowercase.
    company_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hr_payclass'


class HrPaycode(models.Model):
    id = models.AutoField(blank=True, null=True)
    pc_code = models.IntegerField()
    pc_desc = models.TextField(blank=True, null=True)
    pc_type = models.IntegerField(blank=True, null=True)
    export_code = models.TextField(blank=True, null=True)
    pc_delete = models.BooleanField(blank=True, null=True)
    sign = models.TextField(blank=True, null=True)
    min_value = models.TextField(blank=True, null=True)  # This field type is a guess.
    unit = models.IntegerField(blank=True, null=True)
    round_type = models.IntegerField(blank=True, null=True)
    deduct = models.BooleanField(blank=True, null=True)
    yearlylimit = models.TextField(db_column='yearlyLimit', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    pc_mode = models.IntegerField(db_column='pc_Mode', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'hr_paycode'


class HrTemplate(models.Model):
    id = models.AutoField(blank=True, null=True)
    effective = models.IntegerField()
    template_type = models.IntegerField(blank=True, null=True)
    template_len = models.IntegerField(blank=True, null=True)
    template_str = models.TextField(blank=True, null=True)
    isforce = models.IntegerField(db_column='isForce', blank=True, null=True)  # Field name made lowercase.
    flag = models.IntegerField(blank=True, null=True)
    template_index = models.IntegerField()
    action_group = models.IntegerField(blank=True, null=True)
    salt = models.TextField(blank=True, null=True)
    pwd_str = models.TextField(blank=True, null=True)
    employee_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'hr_template'


class Message(models.Model):
    id = models.AutoField(blank=True, null=True)
    middle_message_id = models.BigIntegerField()
    message_code = models.IntegerField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(blank=True, null=True)
    title = models.TextField()
    content = models.TextField(blank=True, null=True)
    message_type = models.IntegerField(blank=True, null=True)
    send_emp_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class Message2Entity(models.Model):
    id = models.AutoField(blank=True, null=True)
    readed = models.IntegerField()
    accept_emp_id = models.IntegerField(blank=True, null=True)
    message_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message2entity'


class MessageZone(models.Model):
    zone_id = models.IntegerField()
    message_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'message_zone'


class PayDepartmentworkcode(models.Model):
    id = models.AutoField(blank=True, null=True)
    wc_code = models.IntegerField()
    department_id = models.IntegerField(blank=True, null=True)
    hourly_payment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_DepartmentWorkCode'


class PayEmployeeworkcode(models.Model):
    id = models.AutoField(blank=True, null=True)
    wc_code = models.IntegerField()
    employee_id = models.IntegerField(blank=True, null=True)
    hourly_payment = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_EmployeeWorkCode'


class PayLoandetail(models.Model):
    id = models.AutoField(blank=True, null=True)
    employee_id = models.IntegerField()
    hiredate = models.DateTimeField(db_column='hireDate')  # Field name made lowercase.
    loandate = models.DateTimeField(db_column='loanDate')  # Field name made lowercase.
    loanamount = models.TextField(db_column='loanAmount')  # Field name made lowercase. This field type is a guess.
    interestrate = models.TextField(db_column='interestRate')  # Field name made lowercase. This field type is a guess.
    totalamount = models.TextField(db_column='totalAmount')  # Field name made lowercase. This field type is a guess.
    repaymentstart = models.DateTimeField(db_column='repaymentStart')  # Field name made lowercase.
    repaymentperiod = models.IntegerField(db_column='repaymentPeriod')  # Field name made lowercase.
    perperiod = models.TextField(db_column='perPeriod')  # Field name made lowercase. This field type is a guess.
    actualamount = models.TextField(db_column='actualAmount')  # Field name made lowercase. This field type is a guess.
    loantype = models.IntegerField(db_column='loanType')  # Field name made lowercase.
    loanreason = models.TextField(db_column='loanReason', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.TextField(db_column='approvedBy')  # Field name made lowercase.
    remark = models.TextField(blank=True, null=True)
    repaytype = models.IntegerField(db_column='repayType')  # Field name made lowercase.
    settled = models.BooleanField(blank=True, null=True)
    settleddate = models.DateTimeField(db_column='settledDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pay_LoanDetail'


class PayLoanrepayment(models.Model):
    id = models.AutoField(blank=True, null=True)
    loan_id = models.IntegerField()
    payrecordid = models.IntegerField(db_column='PayRecordID')  # Field name made lowercase.
    timeperiod = models.TextField(db_column='TimePeriod')  # Field name made lowercase.
    periodstart = models.DateTimeField(db_column='periodStart')  # Field name made lowercase.
    periodend = models.DateTimeField(db_column='periodEnd')  # Field name made lowercase.
    amount = models.TextField()  # This field type is a guess.
    repaid = models.TextField()  # This field type is a guess.
    remain = models.TextField()  # This field type is a guess.
    totalremain = models.TextField(db_column='TotalRemain')  # Field name made lowercase. This field type is a guess.
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_LoanRepayment'


class PayEmpdetail(models.Model):
    id = models.AutoField(blank=True, null=True)
    payment_type = models.SmallIntegerField(blank=True, null=True)
    bank_name = models.TextField(blank=True, null=True)
    bank_account = models.IntegerField(blank=True, null=True)
    bank_accounts = models.TextField(blank=True, null=True)
    national_id = models.IntegerField(blank=True, null=True)
    national_ids = models.TextField(blank=True, null=True)
    agent_id = models.IntegerField(blank=True, null=True)
    agent_ids = models.TextField(blank=True, null=True)
    agent_account = models.IntegerField(blank=True, null=True)
    agent_accounts = models.TextField(blank=True, null=True)
    employee_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pay_empDetail'


class PayFormula(models.Model):
    id = models.AutoField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    paymenttype = models.SmallIntegerField(db_column='PaymentType', blank=True, null=True)  # Field name made lowercase.
    enabled = models.BooleanField(db_column='Enabled', blank=True, null=True)  # Field name made lowercase.
    formulatype = models.SmallIntegerField(db_column='FormulaType', blank=True, null=True)  # Field name made lowercase.
    formulaexpression = models.TextField(db_column='FormulaExpression', blank=True, null=True)  # Field name made lowercase.
    remarks = models.TextField(db_column='Remarks', blank=True, null=True)  # Field name made lowercase.
    issystem = models.BooleanField(db_column='IsSystem', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pay_formula'


class PayFormularesult(models.Model):
    id = models.AutoField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    formulatype = models.IntegerField(db_column='formulaType')  # Field name made lowercase.
    formula_id = models.IntegerField(blank=True, null=True)
    salaryrecord_id = models.IntegerField(db_column='salaryRecord_Id', blank=True, null=True)  # Field name made lowercase.
    result = models.TextField(db_column='Result')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_formulaResult'


class PayReimbursement(models.Model):
    id = models.AutoField(blank=True, null=True)
    employee_id = models.IntegerField()
    rdate = models.DateTimeField(db_column='RDate')  # Field name made lowercase.
    amount = models.TextField()  # This field type is a guess.
    investtype = models.IntegerField(db_column='investType')  # Field name made lowercase.
    typeother = models.TextField(db_column='typeOther', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.TextField(db_column='approvedBy')  # Field name made lowercase.
    remarks = models.TextField(blank=True, null=True)
    forcash = models.BooleanField(db_column='forCash', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pay_reimbursement'


class PaySalaryrecord(models.Model):
    id = models.AutoField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    timeperiod = models.TextField(db_column='TimePeriod', blank=True, null=True)  # Field name made lowercase.
    datestart = models.DateTimeField(db_column='DateStart')  # Field name made lowercase.
    dateend = models.DateTimeField(db_column='DateEnd')  # Field name made lowercase.
    epin = models.TextField(db_column='ePin', blank=True, null=True)  # Field name made lowercase.
    basicsalary = models.TextField(db_column='BasicSalary')  # Field name made lowercase. This field type is a guess.
    otherearnings = models.BinaryField(db_column='OtherEarnings', blank=True, null=True)  # Field name made lowercase.
    otherdeductions = models.BinaryField(db_column='OtherDeductions', blank=True, null=True)  # Field name made lowercase.
    totalotherearnings = models.TextField(db_column='TotalOtherEarnings')  # Field name made lowercase. This field type is a guess.
    totalotherdeductions = models.TextField(db_column='TotalOtherDeductions')  # Field name made lowercase. This field type is a guess.
    netpay = models.TextField(db_column='NetPay')  # Field name made lowercase. This field type is a guess.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    reimbursementtotal = models.TextField(db_column='ReimbursementTotal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    repaymenttotal = models.TextField(db_column='RepaymentTotal', blank=True, null=True)  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_salaryRecord'


class PaySalarysetting(models.Model):
    id = models.AutoField(blank=True, null=True)
    fordepartment = models.BooleanField(db_column='forDepartment', blank=True, null=True)  # Field name made lowercase.
    dcode = models.IntegerField(db_column='dCode', blank=True, null=True)  # Field name made lowercase.
    epin = models.TextField(db_column='ePin', blank=True, null=True)  # Field name made lowercase.
    salarymode = models.SmallIntegerField(db_column='salaryMode')  # Field name made lowercase.
    w_startfrom = models.SmallIntegerField(db_column='w_StartFrom')  # Field name made lowercase.
    b_startfrom = models.SmallIntegerField(db_column='b_StartFrom')  # Field name made lowercase.
    s_startfrom_first = models.SmallIntegerField(db_column='s_StartFrom_First')  # Field name made lowercase.
    s_startfrom_second = models.SmallIntegerField(db_column='s_StartFrom_Second')  # Field name made lowercase.
    m_startfrom = models.SmallIntegerField(db_column='m_StartFrom')  # Field name made lowercase.
    salarydayroundenabled = models.BooleanField(db_column='salaryDayRoundEnabled', blank=True, null=True)  # Field name made lowercase.
    salary_day_from1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_to1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_as1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_from2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_to2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_as2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_from3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_to3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_as3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_above = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_day_as = models.TextField(blank=True, null=True)  # This field type is a guess.
    salaryhourroundenabled = models.BooleanField(db_column='salaryHourRoundEnabled', blank=True, null=True)  # Field name made lowercase.
    salary_hour_from1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_to1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_as1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_from2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_to2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_as2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_from3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_to3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    salary_hour_as3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wagehourroundenabled = models.BooleanField(db_column='wageHourRoundEnabled', blank=True, null=True)  # Field name made lowercase.
    wage_hour_from1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_to1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_as1 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_from2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_to2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_as2 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_from3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_to3 = models.TextField(blank=True, null=True)  # This field type is a guess.
    wage_hour_as3 = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_salarysetting'


class PaySalarystructure(models.Model):
    id = models.AutoField(db_column='Id', blank=True, null=True)  # Field name made lowercase.
    fordepartment = models.BooleanField(db_column='forDepartment', blank=True, null=True)  # Field name made lowercase.
    dcode = models.IntegerField(db_column='dCode', blank=True, null=True)  # Field name made lowercase.
    epin = models.TextField(db_column='ePin', blank=True, null=True)  # Field name made lowercase.
    effective_date = models.DateTimeField()
    basicsalary = models.TextField(db_column='BasicSalary')  # Field name made lowercase. This field type is a guess.

    class Meta:
        managed = False
        db_table = 'pay_salarystructure'


class PaySalarystructureFormula(models.Model):
    id = models.AutoField(blank=True, null=True)
    formula_id = models.IntegerField(db_column='Formula_Id', blank=True, null=True)  # Field name made lowercase.
    salarystructure_id = models.IntegerField(db_column='SalaryStructure_Id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pay_salarystructure_formula'


class SysDatafilter(models.Model):
    id = models.AutoField(blank=True, null=True)
    datafilter_desc = models.TextField()
    data_ranger = models.TextField()

    class Meta:
        managed = False
        db_table = 'sys_datafilter'


class SysLog(models.Model):
    id = models.AutoField(blank=True, null=True)
    tablename = models.TextField(db_column='TableName', blank=True, null=True)  # Field name made lowercase.
    operatetype = models.TextField(db_column='OperateType', blank=True, null=True)  # Field name made lowercase.
    operator = models.TextField(db_column='Operator', blank=True, null=True)  # Field name made lowercase.
    log_date = models.DateTimeField(blank=True, null=True)
    message = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_log'


class SysMenu(models.Model):
    id = models.AutoField(blank=True, null=True)
    menuflag = models.TextField(db_column='MenuFlag')  # Field name made lowercase.
    menuno = models.TextField(db_column='MenuNo')  # Field name made lowercase.
    parentno = models.TextField(db_column='ParentNo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysPrivilege(models.Model):
    id = models.AutoField(blank=True, null=True)
    privilege_name = models.TextField()
    menu_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_privilege'


class SysRole(models.Model):
    id = models.AutoField(blank=True, null=True)
    role_name = models.TextField()
    remark = models.TextField(blank=True, null=True)
    role_type = models.IntegerField(blank=True, null=True)
    defaultrole = models.IntegerField(db_column='defaultRole', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sys_role'


class SysRoleDatafilter(models.Model):
    role_df_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role_datafilter'


class SysRoleRights(models.Model):
    role_pri_id = models.IntegerField()
    role_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_role_rights'


class SysUser(models.Model):
    id = models.AutoField(blank=True, null=True)
    username = models.TextField()
    user_pwd = models.TextField(blank=True, null=True)
    user_email = models.TextField()
    remark = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_user'


class SysUserRole(models.Model):
    role_id = models.IntegerField()
    userid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sys_user_role'


class WorkcodeZone(models.Model):
    zone_id = models.IntegerField()
    workcode_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'workcode_zone'


class ZkprotoControlQueue(models.Model):
    id = models.AutoField(blank=True, null=True)
    action = models.IntegerField()
    target = models.IntegerField()
    info = models.TextField()
    replace_zoneid = models.BigIntegerField(db_column='replace_zoneId')  # Field name made lowercase.
    create_time = models.DateTimeField(blank=True, null=True)
    sendout_time = models.DateTimeField(blank=True, null=True)
    return_time = models.DateTimeField(blank=True, null=True)
    return_flag = models.IntegerField(blank=True, null=True)
    language_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zkproto_control_queue'


class ZkprotoSyncQueue(models.Model):
    id = models.AutoField(blank=True, null=True)
    op_id = models.BigIntegerField()
    action = models.IntegerField()
    info = models.TextField()
    pressedtime = models.BigIntegerField()
    zone_clientid = models.BigIntegerField(db_column='zone_clientID', blank=True, null=True)  # Field name made lowercase.
    sendout_time = models.DateTimeField(blank=True, null=True)
    return_time = models.DateTimeField(blank=True, null=True)
    return_flag = models.IntegerField(blank=True, null=True)
    language_str = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zkproto_sync_queue'
