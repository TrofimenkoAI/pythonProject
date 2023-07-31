from PyQt6 import uic
from PyQt6.QtWidgets import *
from PyQt6.QtSql import *
from PyQt6.QtCore import *
from datetime import datetime
import math
import sqlite3
import sys

Form, Window = uic.loadUiType("MainForm.ui")
Form_add, Window_add = uic.loadUiType("add_form.ui")
Form_error_add1, Window_error_add1 = uic.loadUiType("error_form_add1.ui")
Form_error_add2, Window_error_add2 = uic.loadUiType("error_form_add2.ui")
Form_error_add3, Window_error_add3 = uic.loadUiType("error_form_add3.ui")
Form_error_add4, Window_error_add4 = uic.loadUiType("error_form_add4.ui")
Form_error_add5, Window_error_add5 = uic.loadUiType("error_form_add5.ui")
Form_error_add6, Window_error_add6 = uic.loadUiType("error_form_add6.ui")
Form_error_add7, Window_error_add7 = uic.loadUiType("error_form_add7.ui")
Form_filter, Window_filter = uic.loadUiType("filter_form.ui")
Form_error_filter1, Window_error_filter1 = uic.loadUiType("error_form_filter1.ui")
Form_error_filter2, Window_error_filter2 = uic.loadUiType("error_form_filter2.ui")
Form_error_filter3, Window_error_filter3 = uic.loadUiType("error_form_filter3.ui")
Form_error_filter4, Window_error_filter4 = uic.loadUiType("error_form_filter4.ui")
Form_error_filter5, Window_error_filter5 = uic.loadUiType("error_form_filter5.ui")
Form_error_filter6, Window_error_filter6 = uic.loadUiType("error_form_filter6.ui")
Form_error_filter7, Window_error_filter7 = uic.loadUiType("error_form_filter7.ui")
Form_Edit_Row, Window_Edit_Row = uic.loadUiType("edit_row_form.ui")
Form_error_edit1, Window_error_edit1 = uic.loadUiType("error_edit_form1.ui")
Form_error_edit2, Window_error_edit2 = uic.loadUiType("error_edit_form2.ui")
Form_error_edit3, Window_error_edit3 = uic.loadUiType("error_edit_form3.ui")
Form_error_edit4, Window_error_edit4 = uic.loadUiType("error_edit_form4.ui")
Form_stat, Window_stat = uic.loadUiType("statistics_form.ui")
Form_error_stat1, Window_error_stat1 = uic.loadUiType("error_form_stat1.ui")
Form_error_stat2, Window_error_stat2 = uic.loadUiType("error_form_stat2.ui")

db_name = 'databases/test_db.db'


def to_add_from_main():
    window.close()
    window_add.show()


def to_filter_from_main():
    window.close()
    window_filter.show()
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.select()
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.hideColumn(7)
    form_filter.tableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
    form_filter.tableView.setSortingEnabled(True)


def to_edit_from_filter():
    window_filter.close()
    window_edit_row.show()


def to_stat_from_filter():
    window_filter.close()
    window_stat.show()


def connect_db(db_name):
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName(db_name)
    if not db.open():
        print('NOT connected')
        return False
    return db


def show_f_zb():
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.select()
    form.tableView.setModel(f_zb_test)
    form.tableView.hideColumn(7)
    form.tableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
    form.tableView.setSortingEnabled(True)


def show_zb_table():
    zb_test = QSqlTableModel()
    zb_test.setTable('Zb_test')
    zb_test.select()
    form.tableView.setModel(zb_test)
    form.tableView.setSortingEnabled(True)


def get_names_combobox(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    temp = []
    temp = cur.execute("SELECT DISTINCT name FROM Zb_test").fetchall()
    cur.close()
    con.close()
    return temp


def populate_names_combobox_add():
    list = []
    temp = get_names_combobox(db_name)
    for x in temp:
        list.append(str(x)[2:-3])
    form_add.Name_Combo_Box_Add.addItems(list)


def populate_names_combobox_filter():
    list = []
    temp = get_names_combobox(db_name)
    for x in temp:
        list.append(str(x)[2:-3])
    form_filter.Name_Combo_Box_Filter.addItems(list)


def main_indicator():
    if form_filter.tableView.isColumnHidden(7):
        form_filter.tableView.showColumn(7)
    else:
        form_filter.tableView.hideColumn(7)

    con = sqlite3.connect(db_name)
    cur = con.cursor()
    temp = []
    temp = cur.execute("SELECT name, exec_date FROM Zb_test").fetchall()
    cur.close()
    con.close()
    #print(temp)
    format_bd = '%Y-%m-%d'
    for x in temp:
        f_zb_test = QSqlTableModel()
        f_zb_test.setTable('f_zb_test')
        #print(x[0])
        filter_for_indicator = """ name = '{}' """.format(x[0])
        f_zb_test.setFilter(filter_for_indicator)
        f_zb_test.setSort(0, Qt.SortOrder.AscendingOrder)
        f_zb_test.select()
        """f_zb_test.select()
        form_filter.tableView.setModel(f_zb_test)
        form_filter.tableView.setSortingEnabled(True)"""
        exec_date = x[1]
        for i in range(f_zb_test.rowCount()):
            Fk_2 = 0
            Fk = float(f_zb_test.index(i, 3).data())
            day_end = f_zb_test.index(i, 2).data()
            if f_zb_test.index(i - 1, 2).data() == None:
                xk = 0
            else:
                if f_zb_test.index(i - 2, 2).data() == None or not Fk:
                    xk = 0
                else:
                    Fk_2 = float(f_zb_test.index(i - 2, 3).data())
                    if not Fk_2:
                        xk = 0
                    else:
                        day_end_2 = f_zb_test.index(i - 2, 2).data()
                        deffe_date = datetime.strptime(exec_date, format_bd) - datetime.strptime(day_end, format_bd)
                        rk = math.log(abs(Fk / 100)) / abs((deffe_date.days + 1))
                        deffe_data_2 = datetime.strptime(exec_date, format_bd) - datetime.strptime(day_end_2, format_bd)
                        rk_2 = math.log(abs(Fk_2 / 100)) / abs((deffe_data_2.days + 1))
                        xk = round(abs(math.log(abs(rk / rk_2))), 6)
            record = f_zb_test.record(i)
            record.setValue('main_indicator', xk)
            f_zb_test.setRecord(i, record)
            f_zb_test.select()
            while f_zb_test.canFetchMore():
                f_zb_test.fetchMore()
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.select()
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.setSortingEnabled(True)
    if filtered:
        filter_data()


def filter_data():
    global filtered
    filtered = 1
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.select()
    # test = """ quotation < 60 AND quotation > 20 """
    # f_zb_test.setFilter(test)

    # torg_date_ot = str(form_filter.torg_date_ot_lineEdit.text()).strip()
    torg_date_ot = form_filter.torg_date_ot_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    # torg_date_do = str(form_filter.torg_date_do_lineEdit.text()).strip()
    torg_date_do = form_filter.torg_date_do_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    name_filter = str(form_filter.Name_Combo_Box_Filter.currentText()).strip()
    quot_ot = str(form_filter.quot_ot_lineEdit.text()).strip()
    quot_do = str(form_filter.quot_do_lineEdit.text()).strip()

    print(torg_date_ot, torg_date_do, name_filter, quot_ot, quot_do)

    if quot_ot == '' or quot_do == '':
        window_filter.close()
        window_error_filter4.show()
        return
    if torg_date_ot >= torg_date_do:
        window_filter.close()
        window_error_filter1.show()
        return

    list_of_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    quot_ot_list = list(quot_ot)
    quot_do_list = list(quot_do)
    for i in quot_ot_list:
        if i not in list_of_symbols:
            window_filter.close()
            window_error_filter3.show()
            return
    for i in quot_do_list:
        if i not in list_of_symbols:
            window_filter.close()
            window_error_filter3.show()
            return

    if float(quot_ot) > float(quot_do):
        window_filter.close()
        window_error_filter2.show()
        return

    filters = [torg_date_ot, torg_date_do, name_filter, quot_ot, quot_do]

    filter_temp = """torg_date >= '{tgot}' AND torg_date <= '{tgdo}' AND name = '{namecombobox}' AND quotation >= '{qot}' AND quotation <= '{qdo}'"""
    filter1 = filter_temp.format(tgot=filters[0], tgdo=filters[1], namecombobox=filters[2], qot=filters[3],
                                 qdo=filters[4])
    f_zb_test.setFilter(filter1)
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
    form_filter.tableView.setSortingEnabled(True)
    return filter1


def unfilter():
    global filtered
    filtered = 0
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.setFilter("")
    f_zb_test.select()
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.setSortingEnabled(True)


def get_input_data():
    torg_date = form_add.Torg_Date_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    name = str(form_add.Name_Combo_Box_Add.currentText()).strip()
    day_end = form_add.Day_End_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    quot = str(form_add.Quot_Line_Add.text()).strip()
    min_quot = str(form_add.Min_Quot_Line_Add.text()).strip()
    max_quot = str(form_add.Max_Quot_Line_Add.text()).strip()
    num_contr = str(form_add.Num_contr_Line_Add.text()).strip()

    if (torg_date == '') or (day_end == '') or (quot == '') or (min_quot == '') or (max_quot == '') or (num_contr == ''):
        window_add.close()
        window_error_add1.show()
        return

    list_of_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    list_of_symbols2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    quot_list = list(quot)
    quot_ot_list = list(min_quot)
    quot_do_list = list(max_quot)
    num_contr_list = list(num_contr)
    for i in quot_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_add6.show()
            return
    for i in quot_ot_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_add6.show()
            return
    for i in quot_do_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_add6.show()
            return
    for i in num_contr_list:
        if i not in list_of_symbols2:
            window_edit_row.close()
            window_error_add7.show()
            return

    if (torg_date >= day_end):
        window_add.close()
        window_error_add2.show()
        return
    if (float(min_quot) > float(quot)):
        window_add.close()
        window_error_add3.show()
        return
    if (float(max_quot) < float(quot)):
        window_add.close()
        window_error_add4.show()
        return

    primary_key_test = ''
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    primary_key = [name, torg_date]
    cur.execute("SELECT name, torg_date FROM f_zb_test WHERE name = ? AND torg_date = ?", primary_key)
    primary_key_test = cur.fetchall()
    cur.close()
    con.close()
    if primary_key_test != []:
        window_add.close()
        window_error_add5.show()
        return

    input_values = [torg_date, name, day_end, quot, min_quot, max_quot, num_contr]
    print(input_values)
    insert_into_db(input_values)
    window_add.close()
    window.show()


def insert_into_db(values):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    #print(values)
    cur.execute("INSERT INTO f_zb_test VALUES(?,?,?,?,?,?,?, NULL)", values)
    cur.fetchall()
    #print(values)
    con.commit()
    #print(values)
    cur.close()
    con.close()


def selected_row():
    global rows_to_remove, index_of_row, filtered
    rows_to_remove = []
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    f_zb_test.select()

    selected_indexes = form_filter.tableView.selectedIndexes()
    index_of_row = form_filter.tableView.selectedIndexes()
    if selected_indexes:
        rows_to_remove = list()
        for index in selected_indexes:
            row = index.row()
            if row not in rows_to_remove:
                rows_to_remove.append(row)
    rows = rows_to_remove
    rows_to_remove = []
    return rows


def deletion():
    global filtered
    rows = selected_row()
    if rows == []:
        window_filter.close()
        window_error_filter5.show()
        return
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    if filtered == 1:
        f_zb_test.setFilter(filter_data())
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.setSortingEnabled(True)
    for row in rows[::-1]:
        print(f_zb_test.record(row))
        f_zb_test.removeRow(row)
    f_zb_test.submitAll()
    while f_zb_test.canFetchMore():
        f_zb_test.fetchMore()
    f_zb_test.select()


def edit_row():
    global index_of_row
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    rows = selected_row()
    print(rows)
    if rows:
        if len(rows) > 1:
            window_filter.close()
            window_error_filter7.show()
            return 0
        else:
            row = rows[0]
            print(row)
    else:
        window_filter.close()
        window_error_filter6.show()
        return 0

    row_to_edit = []
    for idx in index_of_row:
        row_to_edit.append(idx.data())
    # print(row_to_edit)
    # print(index_of_row)
    # edited_row = row_to_edit
    to_edit_from_filter()
    return row_to_edit


def editing():
    global row_to_edit
    row_to_edit = edit_row()
    if not row_to_edit:
        return
    form_edit_row.Torg_Date_dateEdit.setText(str(row_to_edit[0]))
    form_edit_row.Name_Combo_Box_Edit.setText(str(row_to_edit[1]))
    form_edit_row.Day_End_dateEdit.setText(str(row_to_edit[2]))
    form_edit_row.Quot_Line_Edit.setText(str(row_to_edit[3]))
    form_edit_row.Min_Quot_Line_Edit.setText(str(row_to_edit[4]))
    form_edit_row.Max_Quot_Line_Edit.setText(str(row_to_edit[5]))
    form_edit_row.Num_contr_Line_Edit.setText(str(row_to_edit[6]))


def query_to_edit():
    global row_to_edit
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    edited_row = row_to_edit
    edited_row[3] = str(form_edit_row.Quot_Line_Edit.text()).strip()
    edited_row[4] = str(form_edit_row.Min_Quot_Line_Edit.text()).strip()
    edited_row[5] = str(form_edit_row.Max_Quot_Line_Edit.text()).strip()
    edited_row[6] = str(form_edit_row.Num_contr_Line_Edit.text()).strip()

    """ТУТ ДОЛЖНА БЫТЬ ПРОВЕРКА НА КОРРЕКТНОСТЬ ВВОДА"""
    if edited_row[3] == '' or edited_row[4] == '' or edited_row[5] == '' or edited_row[6] == '':
        window_edit_row.close()
        window_error_edit2.show()
        return
    list_of_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
    list_of_symbols2 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    quot_list = list(edited_row[3])
    quot_ot_list = list(edited_row[4])
    quot_do_list = list(edited_row[5])
    num_contr_list = list(edited_row[6])
    for i in quot_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_edit3.show()
            return
    for i in quot_ot_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_edit3.show()
            return
    for i in quot_do_list:
        if i not in list_of_symbols:
            window_edit_row.close()
            window_error_edit3.show()
            return
    for i in num_contr_list:
        if i not in list_of_symbols2:
            window_edit_row.close()
            window_error_edit4.show()
            return

    """ТУТ ДОЛЖНА БЫТЬ ПРОВЕРКА ЦЕЛОСТНОСТИ ДАННЫХ"""
    if float(edited_row[3]) < float(edited_row[4]) or float(edited_row[3]) > float(edited_row[5]):
        window_edit_row.close()
        window_error_edit1.show()
        return

    query = QSqlQuery()
    query.prepare("""UPDATE f_zb_test SET quotation = '{}', min_quot = '{}', max_quot = '{}', num_contr = '{}' WHERE torg_date = '{}' AND name = '{}'""".format(edited_row[3], edited_row[4], edited_row[5], edited_row[6], edited_row[0], edited_row[1]))
    query.exec()
    return_to_filter_from_edit()


def stat():
    date_ot = form_stat.torg_date_ot_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    date_do = form_stat.torg_date_do_dateEdit.date().toString(Qt.DateFormat.ISODateWithMs)
    if (date_ot >= date_do):
        window_stat.close()
        window_error_stat1.show()
        return

    names_in_torg_date_temp = check_date_for_stat(date_do)
    if names_in_torg_date_temp == 0:
        window_stat.close()
        window_error_stat2.show()
        return
    names_in_torg_date = []

    for kort in names_in_torg_date_temp:
        names_in_torg_date.append(kort[0])
    print(names_in_torg_date)

    list_of_names_with_main_indicator = name_for_stat(date_ot, date_do)
    print(list_of_names_with_main_indicator)

    names_with_main_indicator = []
    for kort1 in list_of_names_with_main_indicator:
        name = kort1[0]
        if name in names_in_torg_date:
            names_with_main_indicator.append(kort1)
            #names.append(name)
    #print(names)
    #print(names_with_main_indicator)

    means = []
    disps = []
    razmahi = []
    for name in names_in_torg_date:
        mean = 0
        count = 0
        for name_main_indicator in names_with_main_indicator:
            if name_main_indicator[0] == name:
                mean += name_main_indicator[1]
                count += 1
        means.append(round((mean/count), 5))

        D2 = 0
        for name_main_indicator in names_with_main_indicator:
            if name_main_indicator[0] == name:
                D2 += (name_main_indicator[1] - (mean/count))**2
        if D2 == 0:
            disps.append(0)
        else:
            disps.append(round((D2/(count - 1)), 5))

        max = 0
        min = 10000
        for name_main_indicator in names_with_main_indicator:
            if name_main_indicator[0] == name:
                if name_main_indicator[1] > max:
                    max = name_main_indicator[1]
                if name_main_indicator[1] < min:
                    min = name_main_indicator[1]
        razmah = max - min
        razmahi.append(round(razmah, 5))

    print(means)
    print(disps)
    print(razmahi)

    inserting_stats(names_in_torg_date, means, disps, razmahi)


def inserting_stats(names, means, disps, razmahi):
    form_stat.tableWidget.setRowCount(0)
    for i in range(len(names)):
        form_stat.tableWidget.insertRow(i)
        form_stat.tableWidget.setItem(i, 0, QTableWidgetItem(str(names[i])))
        form_stat.tableWidget.setItem(i, 1, QTableWidgetItem(str(means[i])))
        form_stat.tableWidget.setItem(i, 2, QTableWidgetItem(str(disps[i])))
        form_stat.tableWidget.setItem(i, 3, QTableWidgetItem(str(razmahi[i])))


def name_for_stat(date_ot, date_do):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    dates = [date_ot, date_do]
    temp = []
    temp = cur.execute("SELECT name, main_indicator FROM f_zb_test WHERE torg_date BETWEEN ? AND ? ORDER BY name, torg_date", dates).fetchall()
    cur.close()
    con.close()
    return temp


def check_date_for_stat(date_do):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    dates = [date_do]
    temp = []
    temp = cur.execute("SELECT name FROM f_zb_test WHERE torg_date = ?", dates).fetchall()
    cur.close()
    con.close()
    if temp == []:
        return 0
    else:
        return temp


def return_to_main_from_add():
    window_add.close()
    window.show()


def return_to_add_from_error1():
    window_error_add1.close()
    window_add.show()


def return_to_add_from_error2():
    window_error_add2.close()
    window_add.show()


def return_to_add_from_error3():
    window_error_add3.close()
    window_add.show()


def return_to_add_from_error4():
    window_error_add4.close()
    window_add.show()


def return_to_add_from_error5():
    window_error_add5.close()
    window_add.show()


def return_to_add_from_error6():
    window_error_add6.close()
    window_add.show()


def return_to_add_from_error7():
    window_error_add7.close()
    window_add.show()


def return_to_filter_from_error1():
    window_error_filter1.close()
    window_filter.show()


def return_to_filter_from_error2():
    window_error_filter2.close()
    window_filter.show()


def return_to_filter_from_error3():
    window_error_filter3.close()
    window_filter.show()


def return_to_filter_from_error4():
    window_error_filter4.close()
    window_filter.show()


def return_to_filter_from_error5():
    window_error_filter5.close()
    window_filter.show()


def return_to_filter_from_error6():
    window_error_filter6.close()
    window_filter.show()


def return_to_filter_from_error7():
    window_error_filter7.close()
    window_filter.show()


def return_to_main_from_filter():
    global filtered
    filtered = 0
    window_filter.close()
    window.show()


def return_to_filter_from_edit():
    global filtered
    window_edit_row.close()
    window_filter.show()
    f_zb_test = QSqlTableModel()
    f_zb_test.setTable('f_zb_test')
    if filtered:
        filter_data()
    f_zb_test.select()
    form_filter.tableView.setModel(f_zb_test)
    form_filter.tableView.sortByColumn(0, Qt.SortOrder.AscendingOrder)
    form_filter.tableView.setSortingEnabled(True)


def return_to_edit_from_error1():
    window_error_edit1.close()
    window_edit_row.show()


def return_to_edit_from_error2():
    window_error_edit2.close()
    window_edit_row.show()


def return_to_edit_from_error3():
    window_error_edit3.close()
    window_edit_row.show()


def return_to_edit_from_error4():
    window_error_edit4.close()
    window_edit_row.show()


def return_to_filter_from_stat():
    window_stat.close()
    window_filter.show()


def return_to_stat_from_error1():
    window_error_stat1.close()
    window_stat.show()


def return_to_stat_from_error2():
    window_error_stat2.close()
    window_stat.show()



if not connect_db(db_name):
    sys.exit(-1)
else:
    print('Connected')

"""main"""
app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)

form.AddDataButton.clicked.connect(to_add_from_main)
form.FilterDataButton.clicked.connect(to_filter_from_main)
form.show_f_zb_Button.clicked.connect(show_f_zb)
form.show_zb_Button.clicked.connect(show_zb_table)

"""add"""
window_add = Window_add()
form_add = Form_add()
form_add.setupUi(window_add)

form.AddDataButton.clicked.connect(populate_names_combobox_add)
form_add.ReturnToMainButton.clicked.connect(return_to_main_from_add)
form_add.AddDataButton.clicked.connect(get_input_data)

"""add_error1"""
window_error_add1 = Window_error_add1()
form_error_add1 = Form_error_add1()
form_error_add1.setupUi(window_error_add1)

form_error_add1.Ok_Button.clicked.connect(return_to_add_from_error1)

"""add_error2"""
window_error_add2 = Window_error_add2()
form_error_add2 = Form_error_add2()
form_error_add2.setupUi(window_error_add2)

form_error_add2.Ok_Button.clicked.connect(return_to_add_from_error2)

"""add_error3"""
window_error_add3 = Window_error_add3()
form_error_add3 = Form_error_add3()
form_error_add3.setupUi(window_error_add3)

form_error_add3.Ok_Button.clicked.connect(return_to_add_from_error3)

"""add_error4"""
window_error_add4 = Window_error_add4()
form_error_add4 = Form_error_add4()
form_error_add4.setupUi(window_error_add4)

form_error_add4.Ok_Button.clicked.connect(return_to_add_from_error4)

"""add_error5"""
window_error_add5 = Window_error_add5()
form_error_add5 = Form_error_add5()
form_error_add5.setupUi(window_error_add5)

form_error_add5.Ok_Button.clicked.connect(return_to_add_from_error5)

"""add_error6"""
window_error_add6 = Window_error_add6()
form_error_add6 = Form_error_add6()
form_error_add6.setupUi(window_error_add6)

form_error_add6.Ok_Button.clicked.connect(return_to_add_from_error6)

"""add_error7"""
window_error_add7 = Window_error_add7()
form_error_add7 = Form_error_add7()
form_error_add7.setupUi(window_error_add7)

form_error_add7.Ok_Button.clicked.connect(return_to_add_from_error7)

"""filter"""
window_filter = Window_filter()
form_filter = Form_filter()
form_filter.setupUi(window_filter)

filtered = 0
form_filter.Edit_Button.clicked.connect(editing)
form_filter.Main_Button.clicked.connect(main_indicator)
form_filter.Delete_Button.clicked.connect(deletion)
form.FilterDataButton.clicked.connect(populate_names_combobox_filter)
form_filter.To_main_menu.clicked.connect(return_to_main_from_filter)
form_filter.Filter_Button.clicked.connect(filter_data)
form_filter.Stat_Button.clicked.connect(to_stat_from_filter)
form_filter.UnFilter_Button.clicked.connect(unfilter)

"""filter_error1"""
window_error_filter1 = Window_error_filter1()
form_error_filter1 = Form_error_filter1()
form_error_filter1.setupUi(window_error_filter1)

form_error_filter1.Ok_Button.clicked.connect(return_to_filter_from_error1)

"""filter_error2"""
window_error_filter2 = Window_error_filter2()
form_error_filter2 = Form_error_filter2()
form_error_filter2.setupUi(window_error_filter2)

form_error_filter2.Ok_Button.clicked.connect(return_to_filter_from_error2)

"""filter_error3"""
window_error_filter3 = Window_error_filter3()
form_error_filter3 = Form_error_filter3()
form_error_filter3.setupUi(window_error_filter3)

form_error_filter3.Ok_Button.clicked.connect(return_to_filter_from_error3)

"""filter_error4"""
window_error_filter4 = Window_error_filter4()
form_error_filter4 = Form_error_filter4()
form_error_filter4.setupUi(window_error_filter4)

form_error_filter4.Ok_Button.clicked.connect(return_to_filter_from_error4)

"""filter_error5"""
window_error_filter5 = Window_error_filter5()
form_error_filter5 = Form_error_filter5()
form_error_filter5.setupUi(window_error_filter5)

form_error_filter5.Ok_Button.clicked.connect(return_to_filter_from_error5)

"""filter_error6"""
window_error_filter6 = Window_error_filter6()
form_error_filter6 = Form_error_filter6()
form_error_filter6.setupUi(window_error_filter6)

form_error_filter6.Ok_Button.clicked.connect(return_to_filter_from_error6)

"""filter_error7"""
window_error_filter7 = Window_error_filter7()
form_error_filter7 = Form_error_filter7()
form_error_filter7.setupUi(window_error_filter7)

form_error_filter7.Ok_Button.clicked.connect(return_to_filter_from_error7)

"""edit_row"""
window_edit_row = Window_Edit_Row()
form_edit_row = Form_Edit_Row()
form_edit_row.setupUi(window_edit_row)

form_edit_row.CloseEditButton.clicked.connect(return_to_filter_from_edit)
form_edit_row.EditDataButton.clicked.connect(query_to_edit)

"""edit_error1"""
window_error_edit1 = Window_error_edit1()
form_error_edit1 = Form_error_edit1()
form_error_edit1.setupUi(window_error_edit1)

form_error_edit1.Ok_Button.clicked.connect(return_to_edit_from_error1)

"""edit_error2"""
window_error_edit2 = Window_error_edit2()
form_error_edit2 = Form_error_edit2()
form_error_edit2.setupUi(window_error_edit2)

form_error_edit2.Ok_Button.clicked.connect(return_to_edit_from_error2)

"""edit_error3"""
window_error_edit3 = Window_error_edit3()
form_error_edit3 = Form_error_edit3()
form_error_edit3.setupUi(window_error_edit3)

form_error_edit3.Ok_Button.clicked.connect(return_to_edit_from_error3)

"""edit_error4"""
window_error_edit4 = Window_error_edit4()
form_error_edit4 = Form_error_edit4()
form_error_edit4.setupUi(window_error_edit4)

form_error_edit4.Ok_Button.clicked.connect(return_to_edit_from_error4)

"""statistics"""
window_stat = Window_stat()
form_stat = Form_stat()
form_stat.setupUi(window_stat)

form_stat.To_Filter.clicked.connect(return_to_filter_from_stat)
form_stat.Stat_Button.clicked.connect(stat)

"""stat_error1"""
window_error_stat1 = Window_error_stat1()
form_error_stat1 = Form_error_stat1()
form_error_stat1.setupUi(window_error_stat1)

form_error_stat1.Ok_Button.clicked.connect(return_to_stat_from_error1)

"""stat_error2"""
window_error_stat2 = Window_error_stat2()
form_error_stat2 = Form_error_stat2()
form_error_stat2.setupUi(window_error_stat2)

form_error_stat2.Ok_Button.clicked.connect(return_to_stat_from_error2)




window.show()
app.exec()
