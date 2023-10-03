import copy
import PySimpleGUI as sg
import sqlite3
import os

class Error(Exception):
    pass
class TypeError(Error):
    pass
class ValueError(Error):
    pass

class passw:
    t = False
    k = False
    username = 'abc'
    password = 'abc'
    def authority(self):
        layout = [[sg.Text("A.O.A - Welcome To Basheer Enterprises!\n", size=(35,2), font=("Helvetica", 14))],
            [sg.Text('Username ID: ', size=(35), font=("Helvetica", 14))],
            [sg.InputText(key='username', size=(40,3), font=("Helvetica", 12))],
            [sg.Text('Enter Password: ', size=(35), font=("Helvetica", 14))],
            [sg.InputText(key='password', size=(40,9), font=("Helvetica", 12))],
            [sg.Button('Submit', bind_return_key=True)]]
        window = sg.Window('Management', resizable=True).Layout(layout)
        event, values = window.read()

        for i in range(3):
            if event == 'Submit':
                m = values['username'].lower()
                if (m == passw.username):
                    passw.t = True
                    break
                else:
                    sg.popup("Wrong Username!")
                    passw.k = False
                    return False

        if (passw.t == True):
            for j in range(3):
                w = values['password'].lower()
                if (w == passw.password):
                        sg.popup("YOU HAVE BEEN SUCCESSFULLY LOGGED IN!")
                        passw.k = True
                        window.close()
                        return True
                else:
                        sg.popup("Wrong Password!")
                        passw.k = False
                        return False
        else:
            passw.k = False
            return False
        
    def check(self):
        if passw.k == True:
            return True
        else:
            sg.popup("You have Entered Wrong Credentials!\nYou have been LOGGED - OUT!")
            return False
#----------------------------------------------------
class teacher:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.timeSlots = {
            'Mon': ['----'] * 8,
            'Tue': ['----'] * 8,
            'Wed': ['----'] * 8,
            'Thu': ['----'] * 8,
            'Fri': ['----'] * 8
        }
        self.timeSlots['Wed'][6] = '-VC-'
        self.timeSlots['Wed'][7] = 'SLOT'

class batch:
    def __init__(self, dept, batch, section):
        self.dept = dept
        self.batch = batch
        self.section = section
        self.subjects = []
        self.timeSlots = {
            'Mon': ['----'] * 8,
            'Tue': ['----'] * 8,
            'Wed': ['----'] * 8,
            'Thu': ['----'] * 8,
            'Fri': ['----'] * 8
        }
        self.timeSlots['Wed'][6] = '-VC-'
        self.timeSlots['Wed'][7] = 'SLOT'

class subject:
    def __init__(self, name, noOfLectPerWeek, slotsPerWeek):
        self.name = name
        self.noOfLectPerWeek = noOfLectPerWeek
        self.slotsPerWeek = slotsPerWeek
        self.dayCount = 0
        self.weekCount = 0

def scheduling(currBatch):
    # --------------------------------------------------------
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    # --------------------------------------------------------
    for day in days:
        for subj in subjects:
            for i in range(len(teachers)):
                if subj.name in teachers[i].subjects:
                    currTeacher = teachers[i]
            for slot in range(8):
                if subj.name in currBatch.subjects:
                    if subj.noOfLectPerWeek == 3 and subj.slotsPerWeek == 1:
                        if currBatch.timeSlots[day][slot] == '----' and currTeacher.timeSlots[day][slot] == '----' and subj.dayCount == 0 and subj.weekCount < 3:
                            currTeacher.timeSlots[day][slot] = subj.name
                            currBatch.timeSlots[day][slot] = subj.name
                            subj.dayCount += 1
                            subj.weekCount += 1
                    elif subj.noOfLectPerWeek == 2 and subj.slotsPerWeek == 2:
                        if slot < 6:
                            if currBatch.timeSlots[day][slot] == '----' and currTeacher.timeSlots[day][slot] == '----' and subj.dayCount == 0 and subj.weekCount < 2:
                                if currBatch.timeSlots[day][slot + 1] == '----' and currTeacher.timeSlots[day][slot + 1] == '----':
                                    currTeacher.timeSlots[day][slot] = subj.name
                                    currTeacher.timeSlots[day][slot + 1] = subj.name
                                    currBatch.timeSlots[day][slot] = subj.name
                                    currBatch.timeSlots[day][slot + 1] = subj.name
                                    subj.dayCount += 1
                                    subj.weekCount += 1
                    elif subj.noOfLectPerWeek == 1 and subj.slotsPerWeek == 2:
                        if slot < 6:
                            if currBatch.timeSlots[day][slot] == '----' and currTeacher.timeSlots[day][slot] == '----' and subj.dayCount == 0 and subj.weekCount < 1:
                                if currBatch.timeSlots[day][slot + 1] == '----' and currTeacher.timeSlots[day][slot + 1] == '----':
                                    currTeacher.timeSlots[day][slot] = subj.name
                                    currTeacher.timeSlots[day][slot + 1] = subj.name
                                    currBatch.timeSlots[day][slot] = subj.name
                                    currBatch.timeSlots[day][slot + 1] = subj.name
                                    subj.dayCount += 1
                                    subj.weekCount += 1
                    elif subj.noOfLectPerWeek == 1 and subj.slotsPerWeek == 3:
                        if slot < 5:
                            if currBatch.timeSlots[day][slot] == '----' and currTeacher.timeSlots[day][slot] == '----' and subj.dayCount == 0 and subj.weekCount < 1:
                                if currBatch.timeSlots[day][slot + 1] == '----' and currTeacher.timeSlots[day][slot + 1] == '----':
                                    if currBatch.timeSlots[day][slot + 2] == '----' and currTeacher.timeSlots[day][slot + 2] == '----':
                                        currTeacher.timeSlots[day][slot] = subj.name
                                        currTeacher.timeSlots[day][slot + 1] = subj.name
                                        currTeacher.timeSlots[day][slot + 2] = subj.name
                                        currBatch.timeSlots[day][slot] = subj.name
                                        currBatch.timeSlots[day][slot + 1] = subj.name
                                        currBatch.timeSlots[day][slot + 2] = subj.name
                                        subj.dayCount += 1
                                        subj.weekCount += 1

            # --------------------SQL_Database------------------------
            cursor.execute("INSERT INTO teacher_time_tables VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (currTeacher.name, day, currTeacher.timeSlots[day][0], currTeacher.timeSlots[day][1], currTeacher.timeSlots[day][2], currTeacher.timeSlots[day][3], currTeacher.timeSlots[day][4], currTeacher.timeSlots[day][5],  currTeacher.timeSlots[day][6],  currTeacher.timeSlots[day][7]))
            # --------------------------------------------------------
        for subj in subjects:
            subj.dayCount = 0
    for subj in subjects:
        subj.weekCount = 0
    # --------------------------------------------------------
    conn.commit()
    conn.close()
    # --------------------------------------------------------

def makeupClassScheduling(currBatch, currTeacher, makeupSubj, makeupDay):
    batchTimeTable = copy.deepcopy(currBatch.timeSlots)
    teacherTimeTable = copy.deepcopy(currTeacher.timeSlots)

    for day in days:
        for subj in subjects:
            for i in range(len(teachers)):
                if subj.name in teachers[i].subjects:
                    currTeacher = teachers[i]
            for slot in range(8):
                if subj.name in currBatch.subjects:
                    if day == makeupDay and subj.name == makeupSubj.name:
                        if subj.noOfLectPerWeek == 3 and subj.slotsPerWeek == 1:
                            if batchTimeTable[day][slot] == '----' and teacherTimeTable[day][slot] == '----' and subj.dayCount == 0:    
                                batchTimeTable[day][slot] = makeupSubj.name
                                teacherTimeTable[day][slot] = makeupSubj.name
                                subj.dayCount += 1
                    elif subj.noOfLectPerWeek == 2 and subj.slotsPerWeek == 2:
                        if slot < 6:
                            if day == makeupDay and subj.name == makeupSubj.name:
                                if batchTimeTable[day][slot] == '----' and teacherTimeTable[day][slot] == '----' and subj.dayCount == 0:
                                    if batchTimeTable[day][slot + 1] == '----' and teacherTimeTable[day][slot + 1] == '----':
                                        batchTimeTable[day][slot] = makeupSubj.name
                                        batchTimeTable[day][slot + 1] = makeupSubj.name
                                        teacherTimeTable[day][slot] = makeupSubj.name
                                        teacherTimeTable[day][slot + 1] = makeupSubj.name
                                        subj.dayCount += 1
                    elif subj.noOfLectPerWeek == 1 and subj.slotsPerWeek == 2:
                        if slot < 6:   
                            if day == makeupDay and subj.name == makeupSubj.name:  
                                if batchTimeTable[day][slot] == '----' and teacherTimeTable[day][slot] == '----' and subj.dayCount == 0:
                                    if batchTimeTable[day][slot + 1] == '----' and teacherTimeTable[day][slot + 1] == '----':
                                        batchTimeTable[day][slot] = makeupSubj.name
                                        batchTimeTable[day][slot + 1] = makeupSubj.name
                                        teacherTimeTable[day][slot] = makeupSubj.name
                                        teacherTimeTable[day][slot + 1] = makeupSubj.name
                                        subj.dayCount += 1
                    elif subj.noOfLectPerWeek == 1 and subj.slotsPerWeek == 3:
                        if slot < 5:
                            if day == makeupDay and subj.name == makeupSubj.name:
                                if batchTimeTable[day][slot] == '----' and teacherTimeTable[day][slot] == '----' and subj.dayCount == 0:                      
                                    if batchTimeTable[day][slot + 1] == '----' and teacherTimeTable[day][slot + 1] == '----':
                                        if batchTimeTable[day][slot + 2] == '----' and teacherTimeTable[day][slot + 2] == '----':
                                            batchTimeTable[day][slot] = makeupSubj.name
                                            batchTimeTable[day][slot + 1] = makeupSubj.name
                                            batchTimeTable[day][slot + 2] = makeupSubj.name
                                            teacherTimeTable[day][slot] = makeupSubj.name
                                            teacherTimeTable[day][slot + 1] = makeupSubj.name
                                            teacherTimeTable[day][slot + 2] = makeupSubj.name
                                            subj.dayCount += 1                         
        for subj in subjects:
            subj.dayCount = 0
                                            
    displayBatchTimeTable(batchTimeTable, currBatch.dept, currBatch.batch, currBatch.section)
    displayTeacherTimeTable(teacherTimeTable, currTeacher.name)

def deleteSpecificBatch(currBatch):
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    for day in days:
        for subj in subjects:
            for i in range(len(teachers)):
                if subj.name in teachers[i].subjects:
                    currTeacher = teachers[i]
            for slot in range(8):
                if subj.name in currBatch.subjects:
                    if currBatch.timeSlots[day][slot] == subj.name and currTeacher.timeSlots[day][slot] == subj.name:
                        currTeacher.timeSlots[day][slot] = '----'
                        cursor.execute("UPDATE teacher_time_tables SET '_0830_0920' = ? AND '_0930_1020' = ? AND '_1030_1120' = ? AND '_1130_1220' = ? AND '_1230_0120' = ? AND '_0130_0220' = ? AND '_0230_0320' = ? WHERE teacher_name = ? AND day = ?", (currTeacher.timeSlots[day][0], currTeacher.timeSlots[day][1], currTeacher.timeSlots[day][2], currTeacher.timeSlots[day][3], currTeacher.timeSlots[day][4], currTeacher.timeSlots[day][5], currTeacher.timeSlots[day][6], currTeacher.timeSlots[day][7],currTeacher.name, day))
    conn.commit()
    cursor.close()
    conn.close()
                        
def displayBatchTimeTable(batchTimeTable, dept, batch, section):
        layout = [[sg.Table(values=[(day, batchTimeTable[day][0], batchTimeTable[day][1], batchTimeTable[day][2], batchTimeTable[day][3], batchTimeTable[day][4], batchTimeTable[day][5], batchTimeTable[day][6], batchTimeTable[day][7]) for day in days],
                            headings=['Day   ', '8:00 - 8:50', '9:00 - 9:50','10:00 - 10:50', '11:00 - 11:50','12:00 - 12:50', '01:00 - 01:50','02:00 - 02:50','03:00 - 03:50'],
                            num_rows=20,
                            justification='left',
                            auto_size_columns=True,
                            font=('Helvetica', 14),
                            row_height=15)],
                  [sg.Button("Confirm", bind_return_key=True)]]
        window = sg.Window("Time Table for Batch  " + dept + '-' + batch + '-' + section + ' :', resizable=True).Layout(layout)
        event, values = window.read()
        if event in (None, 'Confirm'):
            window.close()
            return
        window.close()
                                                    
def displayTeacherTimeTable(teacherTimeTable, teacherName):
        layout = [[sg.Table(values=[(day, teacherTimeTable[day][0], teacherTimeTable[day][1], teacherTimeTable[day][2], teacherTimeTable[day][3], teacherTimeTable[day][4], teacherTimeTable[day][5],  teacherTimeTable[day][6],  teacherTimeTable[day][7]) for day in days],
                            headings=['Day   ', '8:00 - 8:50', '9:00 - 9:50','10:00 - 10:50', '11:00 - 11:50','12:00 - 12:50', '01:00 - 01:50','02:00 - 02:50','03:00 - 03:50'],
                            num_rows=20,
                            justification='left',
                            auto_size_columns=True,
                            font=('Helvetica', 14),
                            row_height=15)],
                  [sg.Button("Confirm", bind_return_key=True)]]
        window = sg.Window("Time Table for Lecturer  "+teacherName+ ' :', resizable=True).Layout(layout)
        event, values = window.read()
        if event in (None, 'Confirm'):
            window.close()
            return
        window.close()
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
def Add_Teachers(teachers):
    layout = [[sg.Text("Enter Teacher Name: ", size=(35), font=("Helvetica", 14))],
              [sg.Input(key='x', size=(40,3), font=("Helvetica", 12))],
              [sg.Button("Submit", bind_return_key=True), sg.Button("Cancel")]]
    window = sg.Window("Add Teacher").Layout(layout)
    event, values = window.Read()
    window.close()
    if event != "Cancel":
        x = values['x']
        teachers.append(teacher(x))

    #--------------------SQL_Database------------------------
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teachers (teacher_name) VALUES (?)", (x,))
    conn.commit()
    cursor.close()
    conn.close()
    #--------------------------------------------------------
    add_another = sg.popup_yes_no('Want to Add Another Teacher?', title='Add More')
    if add_another == 'Yes':
        Add_Teachers(teachers)
# ----------------------------------------------------------
def Add_Subjects(subjects,teachers):
    teacher_names = [teacher.name for teacher in teachers]
    teacher_dict = {name: index for index, name in enumerate(teacher_names, start=1)}
    while True:
        schemes = [
            '3 theory lectures of 50 minutes',
            '2 theory lectures of 1 hour and 30 minutes',
            '1 theory lecture of 1 hour and 40 minutes',
            '1 lab session of 2 hours and 30 minutes',
        ]
        layout = [
            [sg.Text("Enter Subject Name: ", size=(35), font=("Helvetica", 14))], 
            [sg.Input(key='name', size=(40,3), font=("Helvetica", 12))],
            [sg.Text('Available Teachers:', size=(35), font=("Helvetica", 14))],
            [sg.Listbox(values=teacher_names, size=(30, 6), font=("Helvetica", 14), key='-TEACHER_LIST-')],
            [sg.Text('Enter Teacher Name for This Subject: ', size=(35), font=("Helvetica", 14))], 
            [sg.Input(key='teacher_name', size=(40,3), font=("Helvetica", 12))],
            [sg.Text('Weekly Lecture Plan:', size=(35), font=("Helvetica", 14))],
            [[sg.Radio(scheme, "LECTURE_PLAN", key=f"-{scheme}-", size=(35), font=("Helvetica", 14))] for scheme in schemes],
            [sg.Button('Add Subject', bind_return_key=True), sg.Button('Cancel')]]
        window = sg.Window('Allot Subjects', layout)

        event, values = window.read()
        if event in (None, 'Cancel'):
            window.close()
            return

        name = values['name']
        teacher_name = values['teacher_name']

        if teacher_name not in teacher_dict:
            sg.popup('Invalid Teacher Name. Please Select a Valid Name.')

        subjTeacherOption = teacher_dict[teacher_name]
        subjTeacher = teachers[subjTeacherOption - 1]

        lect_plan_choice = next(scheme for scheme in schemes if values[f"-{scheme}-"])

        if lect_plan_choice == '3 theory lectures of 50 minutes':
                    lecture_count = 3
                    lab_count = 1
        elif lect_plan_choice == '2 theory lectures of 1 hour and 30 minutes':
                    lecture_count = 2
                    lab_count = 2
        elif lect_plan_choice == '1 theory lecture of 1 hour and 40 minutes':
                    lecture_count = 1
                    lab_count = 2
        elif lect_plan_choice == '1 lab session of 2 hours and 30 minutes':
                    lecture_count = 1
                    lab_count = 3

        subjects.append(subject(name, lecture_count, lab_count))
        subjTeacher.subjects.append(subjects[-1].name)
        sg.popup('Subject Added Successfully.')
        break
    # --------------------SQL_Database------------------------
    xx = []
    xx.append(subjTeacher.subjects)
    subject_list = ",".join(str(x) for x in xx)
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO subjects VALUES (?, ?, ?)", (name, lecture_count, lab_count))
    cursor.execute("UPDATE teachers SET subjects = ? WHERE teacher_name = ?", (subject_list, teacher_name))
    conn.commit()
    cursor.close()
    conn.close()
    # --------------------------------------------------------
    add_another_subject = sg.popup_yes_no('Want to Add Another Subject?', title='Add More')
    if add_another_subject == 'Yes':
        window.close()
        Add_Subjects(subjects,teachers)
    else:
        window.close()    
# ----------------------------------------------------------
def Teachers_off(teachers,days,dayTimings):
    teacher_names = [teacher.name for teacher in teachers]
    teacher_dict = {name: index for index, name in enumerate(teacher_names, start=1)}
    layout = [
            [sg.Text('Want To Off Teachers:', size=(35), font=("Helvetica", 14))],
            [sg.Radio("Full Day", "DAY", key="1", size=(35), font=("Helvetica", 14))],
            [sg.Radio("Specific Slot", "DAY", key="2", size=(35), font=("Helvetica", 14))],
            [sg.Button('Confirm', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window('Selection', layout)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return   
    window.close()
    while True:
        if values["1"]:
            while True:
                layout = [
                    [sg.Text('Available Teachers:', size=(35), font=("Helvetica", 14))],
                    [sg.Listbox(values=teacher_names, size=(30, 6), font=("Helvetica", 14), key='-TEACHER_LIST-')],
                    [sg.Text('Enter Teacher Name for This Subject: ', size=(35), font=("Helvetica", 14))], 
                    [sg.Input(key='teacher_name', size=(40,3), font=("Helvetica", 12))],
                    [sg.Text('For Which Day of the Week', size=(35), font=("Helvetica", 14))],
                    [[sg.Radio(day, "DAY", key=f"-{day}-", size=(35), font=("Helvetica", 14))] for day in days],
                    [sg.Button('Day OFF', bind_return_key=True), sg.Button('Cancel')]]
                window = sg.Window('Day off Selection', layout)
                event, values = window.read()
                if event in (None, 'Cancel'):
                    window.close()
                    return        
                window.close()
                teacher_name = values['teacher_name']
                dayOffOption = next(day for day in days if values[f"-{day}-"])
                if dayOffOption == 'Mon':
                    dayOff = days[1 - 1]
                elif dayOffOption == 'Tue':
                    dayOff = days[2 - 1]
                elif dayOffOption == 'Wed':
                    dayOff = days[3 - 1]
                elif dayOffOption == 'Thu':
                    dayOff = days[4 - 1]
                elif dayOffOption == 'Fri':
                    dayOff = days[5 - 1]

                if teacher_name not in teacher_dict:
                    sg.popup('Invalid Teacher Name. Please Select a Valid Name.')
                subjTeacherOption = teacher_dict[teacher_name]
                subjTeacher = teachers[subjTeacherOption - 1]
                for slots in range(8):
                    subjTeacher.timeSlots[dayOff][slots] = 'xxxx'
                sg.popup(dayOff, 'is Now an OFF Day for Lecturer', subjTeacher.name)
                break
            window.close()
            break
            
        elif values["2"]:
            sloting = []
            for i in range(8):
                sloting.append(dayTimings[i])
            layout = [
                [sg.Text('Available Teachers:', size=(35), font=("Helvetica", 14))],
                [sg.Listbox(values=teacher_names, size=(30, 6), font=("Helvetica", 14), key='-TEACHER_LIST-')],
                [sg.Text('Enter Teacher Name for This Subject: ', size=(35), font=("Helvetica", 14))], 
                [sg.Input(key='teacher_name', size=(40,3), font=("Helvetica", 12))],
                [sg.Text('For Which Day of the Week', size=(35), font=("Helvetica", 14))],
                [[sg.Radio(day, "DAY", key=f"-{day}-", size=(35), font=("Helvetica", 14))] for day in days],
                [sg.Text('Time-Slots:', size=(35), font=("Helvetica", 14))],
                [[sg.Radio(days, "Slots", key=f"-{days}-", size=(35), font=("Helvetica", 14))] for days in sloting],
                [sg.Button('Slot OFF', bind_return_key=True), sg.Button('Cancel')]]
            window = sg.Window('Slot off Selection', layout)
            event, values = window.read()
            if event in (None, 'Cancel'):
                window.close()
                return
            window.close()
            teacher_name = values['teacher_name']
            if teacher_name not in teacher_dict:
                sg.popup('Invalid Teacher Name. Please Select a Valid Name.')
            subjTeacherOption = teacher_dict[teacher_name]
            subjTeacher = teachers[subjTeacherOption - 1]
            dayOffOption = next(day for day in days if values[f"-{day}-"])
            if dayOffOption == 'Mon':
                dayOff = days[1 - 1]
            elif dayOffOption == 'Tue':
                dayOff = days[2 - 1]
            elif dayOffOption == 'Wed':
                dayOff = days[3 - 1]
            elif dayOffOption == 'Thu':
                dayOff = days[4 - 1]
            elif dayOffOption == 'Fri':
                dayOff = days[5 - 1]
            k = next(days for days in sloting if values[f"-{days}-"])
            if k == '8:00 - 8:50':
                offSlot = 1 - 1
            elif k == '9:00 - 9:50':
                offSlot = 2 - 1
            elif k == '10:00 - 10:50':
                offSlot = 3 - 1
            elif k == '11:00 - 11:50':
                offSlot = 4 - 1
            elif k == '12:00 - 12:50':
                offSlot = 5 - 1
            elif k == '01:00 - 01:50':
                offSlot = 6 - 1
            elif k == '02:00 - 02:50':
                offSlot = 7 - 1
            elif k == '03:00 - 03:50':
                offSlot = 8 - 1
            subjTeacher.timeSlots[dayOff][offSlot] = 'xxxx'
            window.close()
            sg.popup(subjTeacher.name + ' is now free on ' + dayOff + ' at ' + dayTimings[offSlot])
            break
        else:
            sg.pop("Type 1 or 2!")
        window.close()

# ----------------------------------------------------------
def Add_Batches(teachers,days,subjects,batches):
    subject_names = [subj.name for subj in subjects]
    subject_dict = {name: index for index, name in enumerate(subject_names, start=1)}
    layout = [
        [sg.Text("Enter Department, Batch, and Section: ", size=(35), font=("Helvetica", 14))],
        [sg.Input(key='name', size=(40,3), font=("Helvetica", 12))],
        [sg.Text("How many Subjects to add?", size=(35), font=("Helvetica", 14))],
        [sg.Input(key='m', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Add Batch', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window('ADD Batch', layout)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return
    m = int(values['m'])
    batchSection = values['name']
    batchDetails = batchSection.split('-')
    dept = batchDetails[0].upper()
    Batch = batchDetails[1]
    section = batchDetails[2].upper()
    isNewBatch = True
    while True:
        for i in range(len(batches)):
            if dept == batches[i].dept and Batch == batches[i].batch and section == batches[i].section:
                isNewBatch = False
                sg.popup('This Batch Already EXISTS, Please Enter Another.')
                break
        if isNewBatch:
            batches.append(batch(dept, Batch, section))
            break
    window.close()
        
    for i in range(m):
        layout2 = [
            [sg.Text('Subjects List:', size=(35), font=("Helvetica", 14))],
            [sg.Listbox(values=subject_names, size=(30, 6), font=("Helvetica", 14), key='Subject_LIST')],
            [sg.Text('Enter Subject Name To Add: ', size=(35), font=("Helvetica", 14))], 
            [sg.Input(key='subject_name', size=(40,3), font=("Helvetica", 12))],
            [sg.Button('Add Subject', bind_return_key=True), sg.Button('Cancel')]]
        window = sg.Window('ADD Subjects to Batch', layout2)
        event, values = window.read()
        if event in (None, 'Cancel'):
            window.close()
            return
        window.close()
        
        subjectName = values['subject_name']
        if subjectName not in subject_dict:
            sg.popup('Invalid Subject. Please Select a Valid Subject.')
        batches[-1].subjects.append(subjectName)
    window.close()

    if len(batches) != 0 and len(teachers) != 0 and len(subjects) != 0:
        scheduling(batches[-1])
        sg.popup('Time-Table Scheduling Successfull!')
    else:
        sg.popup("Scheduling Un-Successfull!!!")
    # --------------------SQL_Database------------------------

    xx = []
    xx.append(batches[-1].subjects)
    subject_list = ",".join(str(x) for x in xx)
    conn = sqlite3.connect('timetable.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO batches VALUES (?, ?, ?, ?)", (dept, Batch, section, subject_list))
    for day in days:
        cursor.execute("INSERT INTO batch_time_tables VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (dept, Batch, section, day, batches[-1].timeSlots[day][0], batches[-1].timeSlots[day][1], batches[-1].timeSlots[day][2], batches[-1].timeSlots[day][3], batches[-1].timeSlots[day][4], batches[-1].timeSlots[day][5],  batches[-1].timeSlots[day][6],  batches[-1].timeSlots[day][7]))
    conn.commit()
    cursor.close()
    conn.close()
    # --------------------------------------------------------
    add_another_batch = sg.popup_yes_no('Want to add Another Batch?', title='Add More?')
    if add_another_batch == 'No':
        window.close()
    else:
        Add_Batches(teachers,days,subjects,batches)
    window.close()
# ----------------------------------------------------------
def Move_Class(teachers,days,subjects,batches,dayTimings):
    layout = [
        [sg.Text('Batches:', size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values=[f"{b.dept}-{b.batch}-{b.section}" for b in batches], size=(30, 6), font=("Helvetica", 12), key='BATCHES')],
        [sg.Text('Enter Batch Name to Move Lectures:', size=(35), font=("Helvetica", 14))],
        [sg.Input(key='BATCH_NAME', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Select Batch', bind_return_key=True), sg.Button('Cancel')]
    ]
    window = sg.Window('Batch Select', layout)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return
    window.close() 

    batchSectionOption = values['BATCH_NAME'].upper()
    currBatch = None
    for i in batches:
        if i.dept + '-' + i.batch + '-' + i.section == batchSectionOption:
            currBatch = i
            break
    if currBatch is None:
        sg.popup('Invalid batch name.')

    displayBatchTimeTable(currBatch.timeSlots, currBatch.dept, currBatch.batch, currBatch.section)
    ####################
    
    layout2 = [
        [sg.Text('List of subjects being offered to: ' + currBatch.dept + currBatch.batch + currBatch.section, size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values=currBatch.subjects, size=(30, 6),font=("Helvetica", 14))],
        [sg.Text('Select Subject:', size=(35), font=("Helvetica", 14))],
        [sg.Input(key='abc', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Choose', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window('Subject Selection', layout2)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return

    window.close()
    
    subject_name = values['abc']
    subject = None
    for subj in subjects:
        if subj.name == subject_name:
            subject = subj  # Saves the OBJECT of the subject, not just the name

    if subject:
        currTeacher = None
        for teacher in teachers:
            if subject.name in teacher.subjects:
                currTeacher = teacher
                break

    ####################
    option = 1
    option_index_list = []
    L = []
    for i in range(5):
        if subject.name in currBatch.timeSlots[days[i]]:
            L.append(days[i])
            option_index_list.append((option, i))
            option += 1

    layout3 = [
        [sg.Text('Days of the Week ' + subject.name + ' Takes Place:', size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values= [day for day in L], size=(40, 6), font=("Helvetica", 12), key='days')],
        [sg.Text('Which week day to cancel the lecture From:', size=(35), font=("Helvetica", 14))],
        [sg.Input(key='DAY_NAME', size=(40,3), font=("Helvetica", 12))],
        [sg.Text('New Days of the Week:', size=(35), font=("Helvetica", 14))],
        [[sg.Radio(dayl, "DAY", key=f"-{dayl}-", size=(35), font=("Helvetica", 14))] for dayl in days],
        [sg.Button('Select Day', bind_return_key=True), sg.Button('Cancel')]]
    window = sg.Window('Day Selection - 1', layout3)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return
    window.close() 

    while True:
        dayCancelOption = values['DAY_NAME'].title()

        dayCancel = None
        for i in days:
            if i == dayCancelOption:
                dayCancel = i 
        break

    for slot in range(8):
        if currBatch.timeSlots[dayCancel][slot] == subject.name:
            slotCancel = slot
            break

    dayMoveOption = next(dayl for dayl in days if values[f"-{dayl}-"])
    dayMove = None
    for i in days:
        if i == dayMoveOption:
            dayMove = i 

    sloting = []
    for i in range(8):
        sloting.append(dayTimings[i])
    
    while True:
        if '----' in currBatch.timeSlots[dayMove]:
            values = [
                dayMove,
                currBatch.timeSlots[dayMove][0],
                currBatch.timeSlots[dayMove][1],
                currBatch.timeSlots[dayMove][2],
                currBatch.timeSlots[dayMove][3],
                currBatch.timeSlots[dayMove][4],
                currBatch.timeSlots[dayMove][5],
                currBatch.timeSlots[dayMove][6],
                currBatch.timeSlots[dayMove][7]]
            layout4 = [[sg.Table(values=[values],
                                headings=['Day   ', '8:00 - 8:50', '9:00 - 9:50','10:00 - 10:50', '11:00 - 11:50','12:00 - 12:50', '01:00 - 01:50','02:00 - 02:50','03:00 - 03:50'],
                                num_rows=5,
                                justification='left',
                                auto_size_columns=True,
                                font=('Helvetica', 14),
                                row_height=15)],
                        [sg.Text('Time-Slots in ' + dayMove + " :", size=(35), font=("Helvetica", 14))],
                        [[sg.Radio(day, "Slots", key=f"-{day}-", size=(35), font=("Helvetica", 14))] for day in sloting],
                        [sg.Button('Select Slot', bind_return_key=True), sg.Button('Cancel')]]
            window = sg.Window("Time Selection "+str(currBatch)+" :", resizable=True).Layout(layout4)
            event, values = window.read()
            if event in (None, 'Confirm'):
                window.close()
                return
            window.close()

            while True:
                k = next(day for day in sloting if values[f"-{day}-"])
                if k == '8:00 - 8:50':
                    slotMove = 1 - 1
                elif k == '9:00 - 9:50':
                    slotMove = 2 - 1
                elif k == '10:00 - 10:50':
                    slotMove = 3 - 1
                elif k == '11:00 - 11:50':
                    slotMove = 4 - 1
                elif k == '12:00 - 12:50':
                    slotMove = 5 - 1
                elif k == '01:00 - 01:50':
                    slotMove = 6 - 1
                elif k == '02:00 - 02:50':
                    slotMove = 7 - 1
                elif k == '03:00 - 03:50':
                    slotMove = 8 - 1

                if subject.slotsPerWeek == 1:
                    if currBatch.timeSlots[dayMove][slotMove] == '----':
                        currTeacher.timeSlots[dayCancel][slotCancel] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel] = '----'
                        currTeacher.timeSlots[dayMove][slotMove] = subject.name
                        currBatch.timeSlots[dayMove][slotMove] = subject.name
                        break
                    else:
                        sg.popup('\nCannot move class to this time-slot,\nPlease select a time-slot that is free.')

                elif subject.slotsPerWeek == 2:
                    if currBatch.timeSlots[dayMove][slotMove] == '----' and currBatch.timeSlots[dayMove][slotMove+1] == '----':
                        currTeacher.timeSlots[dayCancel][slotCancel] = '----'
                        currTeacher.timeSlots[dayCancel][slotCancel + 1] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel + 1] = '----'
                        currTeacher.timeSlots[dayMove][slotMove] = subject.name
                        currTeacher.timeSlots[dayMove][slotMove + 1] = subject.name
                        currBatch.timeSlots[dayMove][slotMove] = subject.name
                        currBatch.timeSlots[dayMove][slotMove + 1] = subject.name
                        break
                    else:
                        sg.popup('\nCannot move class to this time-slot, Please select a time-slot that is free.')

                elif subject.slotsPerWeek == 3:
                    if currBatch.timeSlots[dayMove][slotMove] == '----' and currBatch.timeSlots[dayMove][slotMove+1] == '----' and currBatch.timeSlots[dayMove][slotMove+2] == '----':
                        currTeacher.timeSlots[dayCancel][slotCancel] = '----'
                        currTeacher.timeSlots[dayCancel][slotCancel + 1] = '----'
                        currTeacher.timeSlots[dayCancel][slotCancel + 2] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel + 1] = '----'
                        currBatch.timeSlots[dayCancel][slotCancel + 2] = '----'
                        currTeacher.timeSlots[dayMove][slotMove] = subject.name
                        currTeacher.timeSlots[dayMove][slotMove + 1] = subject.name
                        currTeacher.timeSlots[dayMove][slotMove + 2] = subject.name
                        currBatch.timeSlots[dayMove][slotMove] = subject.name
                        currBatch.timeSlots[dayMove][slotMove + 1] = subject.name
                        currBatch.timeSlots[dayMove][slotMove + 2] = subject.name
                        break
                    else:
                        sg.popup('Cannot move class to this time-slot,\nPlease select a time-slot that is free.')
                else:
                    sg.popup("Not Possible to repeat back as the same!")
            break
        else:
            sg.popup('There is no free time-slot on this day,\nPlease choose another day which has a free time-slot.')
            break
    sg.popup('Class has been Moved to Chosen Day and Time-Slot!')
# ----------------------------------------------------------
def Makeup(teachers,days,subjects,batches):
    while True:
        layout = [
            [sg.Text('Batches List:', size=(35), font=("Helvetica", 14))],
            [sg.Listbox(values=[f"{b.dept}-{b.batch}-{b.section}" for b in batches], size=(30, 6), font=("Helvetica", 14), key='-BATCH-')],
            [sg.Text('Enter Batch Name to Scedule Makeup For: ', size=(35), font=("Helvetica", 14))], 
            [sg.Input(key='batch_name', size=(40,3), font=("Helvetica", 12))],
            [sg.Text('Subjects List:', size=(35), font=("Helvetica", 14))],
            [sg.Listbox(values=[subj.name for subj in subjects], size=(30, 6), font=("Helvetica", 14), key='-SUBJECT-')],
            [sg.Text('Enter Make up Subject: ', size=(35), font=("Helvetica", 14))], 
            [sg.Input(key='subject_name', size=(40,3), font=("Helvetica", 12))],
            [sg.Text('For Which Day of the Week', size=(35), font=("Helvetica", 14))],
            [[sg.Radio(day, "DAY", key=f"-{day}-", size=(35), font=("Helvetica", 14))] for day in days],
            [sg.Button('Schedule Makeup', bind_return_key=True), sg.Button('Cancel')]]
        window = sg.Window('Makeup Scheduler', layout)
        event, values = window.read()
        if event in (None, 'Cancel'):
            window.close()
            return
    
        batchSectionOption = values['batch_name'].upper()
        subjectName = values['subject_name']
        dayMakeup = next(day for day in days if values[f"-{day}-"])

        currBatch = None
        for i in batches:
                if i.dept + '-' + i.batch + '-' + i.section == batchSectionOption:
                    currBatch = i
                    break

        if currBatch is None:
                sg.popup('Invalid batch name. Please try again.')
                continue

        subject = next(subj for subj in subjects if subj.name == subjectName)
        if subject.name not in currBatch.subjects:
                sg.popup('This subject is not offered to the chosen Class/Batch.')

        for i in range(len(teachers)):
                if subject.name in teachers[i].subjects:
                    makeupLectureTeacher = teachers[i]

        makeupClassScheduling(currBatch, makeupLectureTeacher, subject, dayMakeup)
        break
    add_another = sg.popup_yes_no('Want to add Another Make-up?', title='Add More?')
    if add_another == 'No':
        window.close()
    else:
        Makeup(teachers,days,subjects,batches)
    window.close()
# ----------------------------------------------------------
def Display_Class(batches):
    while True:
        layout = [
        [sg.Text('Batches List:', size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values=[f"{b.dept}-{b.batch}-{b.section}" for b in batches], size=(30, 6), font=("Helvetica", 14), key='-BATCH-')],
        [sg.Text('Enter Batch Name To Display TimeTable For: ', size=(35), font=("Helvetica", 14))], 
        [sg.Input(key='batch_name', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Display', bind_return_key=True), sg.Button('Cancel')]]
        window = sg.Window('Batch Selection', layout)
        event, values = window.read()
        if event in (None, 'Cancel'):
            window.close()
            return

        batchSectionOption = values['batch_name'].upper()
        currBatch = None
        for i in batches:
                if i.dept + '-' + i.batch + '-' + i.section == batchSectionOption:
                    currBatch = i
                    break

        if currBatch is None:
            sg.popup('Invalid batch name. Please try again.')
            continue
        
        displayBatchTimeTable(currBatch.timeSlots, currBatch.dept, currBatch.batch, currBatch.section)
        break
    change = sg.popup_yes_no('Want to change it??', title='change')
    if change == 'Yes':
        window.close()
        Move_Class(teachers,days,subjects,batches,dayTimings)
        window.close()
    window.close()
# ----------------------------------------------------------        
def Display_Teacher(teachers):
    teacher_names = [teacher.name for teacher in teachers]
    teacher_dict = {name: index for index, name in enumerate(teacher_names, start=1)}
    while True:
        layout = [
        [sg.Text('Available Teachers:', size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values=teacher_names, size=(30, 6), font=("Helvetica", 14), key='-TEACHER_LIST-')],
        [sg.Text('Enter Teacher Name To Display TimeTable For: ', size=(35), font=("Helvetica", 14))], 
        [sg.Input(key='teacher_name', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Display', bind_return_key=True), sg.Button('Cancel')]]
        window = sg.Window('Teacher Selection', layout)
        event, values = window.read()
        if event in (None, 'Cancel'):
            window.close()
            return

        teacher_name = values['teacher_name']

        if teacher_name not in teacher_dict:
            sg.popup('Invalid Teacher Name. Please Select a Valid Name.')
            continue

        subjTeacherOption = teacher_dict[teacher_name]
        teacher = teachers[subjTeacherOption - 1]
        
        displayTeacherTimeTable(teacher.timeSlots, teacher.name)
        break
    change = sg.popup_yes_no('Want to change it??', title='change')
    if change == 'Yes':
        window.close()
        Move_Class(teachers,days,subjects,batches,dayTimings)
        window.close()
    window.close()
# ----------------------------------------------------------
def Delete_Specific(batches):
    layout = [
        [sg.Text('Batches:', size=(35), font=("Helvetica", 14))],
        [sg.Listbox(values=[f"{b.dept}-{b.batch}-{b.section}" for b in batches], size=(30, 6), font=("Helvetica", 12), key='BATCHES')],
        [sg.Text('Enter Batch Name to Delete its Time-Table:', size=(35), font=("Helvetica", 14))],
        [sg.Input(key='BATCH_NAME', size=(40,3), font=("Helvetica", 12))],
        [sg.Button('Delete', bind_return_key=True), sg.Button('Cancel')]
    ]
    window = sg.Window('Batch Delete', layout)
    event, values = window.read()
    if event in (None, 'Cancel'):
        window.close()
        return
        
    batch_name = values['BATCH_NAME'].upper()
    for i in range(len(batches)):
        if f"{batches[i].dept}-{batches[i].batch}-{batches[i].section}" == batch_name:
            #--------------------SQL_Database------------------------
            conn = sqlite3.connect('timetable.db')
            cursor = conn.cursor()
            cursor.execute("DELETE FROM batches WHERE dept = ? AND batch = ? AND section = ?", (batches[i].dept,batches[i].batch,batches[i].section))
            cursor.execute("DELETE FROM batch_time_tables WHERE dept = ? AND batch = ? AND section = ?", (batches[i].dept,batches[i].batch,batches[i].section))
            conn.commit()
            cursor.close()
            conn.close()
            #--------------------------------------------------------
            deleteSpecificBatch(batches[i])
            del batches[i]

            sg.popup("The Batch has been Deleted")
            break
    else:
        sg.popup("Batch Not Found.")
    window.close()
# ----------------------------------------------------------
def Reset_All(subjects,batches,teachers):
    subjects.clear()
    batches.clear()
    teachers.clear()
    os.remove('timetable.db')
    sg.popup('The Program Has been Factory data Reset!')
# ----------------------------------------------------------
def End_Display():
    sg.popup("GoodBye!\n\nThank-You For Choosing our Serivces!\nFor any Complains:\nContact us at: +923147800668, +923058969080, +923095258214\n\nProject Made By: Muhammad Shehzam, Sardar Abdul Aziz, Ammar Saqib\n\nFrom CS-02-A")
# ----------------------------------------------------------
# ------------------MAIN PROGRAM----------------------------
# ----------------------------------------------------------
teachers = []
days = [
    'Mon',
    'Tue',
    'Wed',
    'Thu',
    'Fri',
]
subjects = []
batches = []
dayTimings = [
    '8:00 - 8:50',
    '9:00 - 09:50',
    '10:00 - 10:50',
    '11:00 - 11:50',
    '12:00 - 12:50',
    '01:00 - 01:50',
    '02:00 - 02:50',
    '03:00 - 03:50']
a = passw()
# ----------------------------------------------------------
# ----------------------------------------------------------
# ----------------------------------------------------------
conn = sqlite3.connect('timetable.db')
cursor = conn.cursor()
# ----------------------------------------------------------
table_query = ('''
CREATE TABLE IF NOT EXISTS teachers (
        teacher_name TEXT PRIMARY KEY,
        subjects TEXT
    )
''')
cursor = conn.cursor()
cursor.execute(table_query)
cursor.execute('SELECT teacher_name, subjects FROM teachers')
rows = cursor.fetchall()
if rows is not None:
    for row in rows:
        teacher_name, subjs = row
        teachers.append(teacher(teacher_name))
        if subjs != None:
            subjs = subjs[1:-1].split(",")
            for i in range(len(subjs)):
                subjs[i] = subjs[i].strip()
                subjs[i] = subjs[i][1:-1]
        else:
            subjs = []
        teachers[-1].subjects.extend(subjs)
conn.commit()
# ----------------------------------------------------------
table_query = ('''
    CREATE TABLE IF NOT EXISTS teacher_time_tables (
        teacher_name TEXT,
        day TEXT,
        _0800_0850 TEXT,
        _0900_0950 TEXT,
        _1000_1050 TEXT,
        _1100_1150 TEXT,
        _1200_1250 TEXT,
        _0100_0150 TEXT,
        _0200_0250 TEXT,
        _0300_0350 TEXT
    )
''')
cursor = conn.cursor()
cursor.execute(table_query)
cursor.execute('SELECT teacher_name, day, _0800_0850, _0900_0950, _1000_1050, _1100_1150, _1200_1250, _0100_0150, _0200_0250, _0300_0350 FROM teacher_time_tables')
rows = cursor.fetchall()
if rows is not None:
    for teach in teachers:
        for row in rows:
            teacher_name, day, _0800_0850, _0900_0950, _1000_1050, _1100_1150, _1200_1250, _0100_0150, _0200_0250, _0300_0350 = row
            if teach.name == teacher_name:
                teach.timeSlots[day][0] = _0800_0850
                teach.timeSlots[day][1] = _0900_0950
                teach.timeSlots[day][2] = _1000_1050
                teach.timeSlots[day][3] = _1100_1150
                teach.timeSlots[day][4] = _1200_1250
                teach.timeSlots[day][5] = _0100_0150
                teach.timeSlots[day][6] = _0200_0250
                teach.timeSlots[day][7] = _0300_0350
        conn.commit()
# ----------------------------------------------------------
table_query = ('''
    CREATE TABLE IF NOT EXISTS batches (
        dept TEXT,
        batch TEXT,
        section TEXT,
        subjects TEXT
    )
''')
cursor = conn.cursor()
cursor.execute(table_query)
cursor.execute('SELECT dept, batch, section, subjects FROM batches')
rows = cursor.fetchall()
if rows is not None:
    for row in rows:
        dept, Batch, section, subjs = row
        batches.append(batch(dept, Batch, section))
        if subjs != None:
            subjs = subjs[1:-1].split(",")
            print(subjs, type(subjs))
        else:
            subjs = []
        #[batches[-1].subjects.extend(subjects) for subject in subjects if subject]
        batches[-1].subjects.extend(subjs)
        conn.commit()
# ----------------------------------------------------------
table_query = ('''
    CREATE TABLE IF NOT EXISTS batch_time_tables (
        dept TEXT,
        batch TEXT,
        section TEXT,
        day TEXT,
        _0800_0850 TEXT,
        _0900_0950 TEXT,
        _1000_1050 TEXT,
        _1100_1150 TEXT,
        _1200_1250 TEXT,
        _0100_0150 TEXT,
        _0200_0250 TEXT,
        _0300_0350 TEXT
    )
''')
cursor = conn.cursor()
cursor.execute(table_query)
cursor.execute('SELECT * FROM batch_time_tables')
rows = cursor.fetchall()
if rows is not None:
    for cls_batch in batches:
        for row in rows:
            dept, Batch, section, day, _0800_0850, _0900_0950, _1000_1050, _1100_1150, _1200_1250, _0100_0150, _0200_0250, _0300_0350 = row
            if cls_batch.dept == dept and cls_batch.batch == Batch and cls_batch.section == section:
                cls_batch.timeSlots[day][0] = _0800_0850
                cls_batch.timeSlots[day][1] = _0900_0950
                cls_batch.timeSlots[day][2] = _1000_1050
                cls_batch.timeSlots[day][3] = _1100_1150
                cls_batch.timeSlots[day][4] = _1200_1250
                cls_batch.timeSlots[day][5] = _0100_0150
                cls_batch.timeSlots[day][6] = _0200_0250
                cls_batch.timeSlots[day][7] = _0300_0350
            conn.commit()
# ----------------------------------------------------------
# subjects table
table_query = ('''
    CREATE TABLE IF NOT EXISTS subjects (
        subject_name TEXT,
        lectures_per_week INTEGER,
        slots_per_day INTEGER
    )
''')
cursor = conn.cursor()
cursor.execute(table_query)
cursor.execute('SELECT subject_name, lectures_per_week, slots_per_day FROM subjects')
rows = cursor.fetchall()
if rows is not None:
    for row in rows:
        subject_name, lectures_per_week, slots_per_day = row
        subjects.append(subject(subject_name, lectures_per_week, slots_per_day))
conn.commit()
conn.close()
# ----------------------------------------------------------
# ----------------------------------------------------------
#'---------------------------------------------------------------------------------------------------------------------------------------------'

sg.theme('Dark Grey 11')
layout = [[sg.Text("\t         Main - Menu:", size=(35,1), font=("Helvetica", 40))],
          [sg.Button("Add Teachers", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Add Subjects", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Set Teacher Off Days", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Add Batches", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Move Class", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Schedule a Make-up Lecture", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Display Time Table for a Class", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Display Time Table for a Teacher", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Delete Specific Class Table", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Reset All Data", size=(45,1.15), font=("Helvetica", 14))],
          [sg.Button("Exit", size=(45,1.15), font=("Helvetica", 14))]]
window = sg.Window("IST TIME-TABLE App", resizable=True, size = (1000,760), element_justification = ('center'), margins = (0,0)).Layout(layout)

if a.authority() == True:
    while a.check():
        event, values = window.Read()
        if event == "Add Teachers":
            Add_Teachers(teachers)
    # ----------------------------------------------------------
        elif event == "Add Subjects":
            Add_Subjects(subjects,teachers)
    # ----------------------------------------------------------
        elif event == "Set Teacher Off Days":
            Teachers_off(teachers,days,dayTimings)
    # ----------------------------------------------------------
        elif event == "Add Batches":
            Add_Batches(teachers,days,subjects,batches)
    # ----------------------------------------------------------
        elif event == "Move Class":
            Move_Class(teachers,days,subjects,batches,dayTimings)
    # ----------------------------------------------------------
        elif event == "Schedule a Make-up Lecture":
            Makeup(teachers,days,subjects,batches)
    # ----------------------------------------------------------
        elif event == "Display Time Table for a Class":
            Display_Class(batches)
    # ----------------------------------------------------------
        elif event == "Display Time Table for a Teacher":
            Display_Teacher(teachers)
    # ----------------------------------------------------------
        elif event == "Delete Specific Class Table":
            Delete_Specific(batches)
    # ----------------------------------------------------------
        elif event == "Reset All Data":
            Reset_All(subjects,batches,teachers)
    # ----------------------------------------------------------
        elif event == "Exit":
            window.Close()
            End_Display()
            break
        else:
            window.Close()
            break