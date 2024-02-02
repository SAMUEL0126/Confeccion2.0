import os
import sys 
import sqlite3
from sqlite3 import Error
from PySide2.QtWidgets import QTableWidgetItem

class AppFunctions():

    def __init__(self, arg):
        super(AppFunctions, self).__init__()
        self.arg = arg
        
###############"""Juanfe: Genero la conexión con la base de datos de prueba (SQLITE)"""###################

    def create_connection(db_file):
        conn = None 
        try: 
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)    

        return conn
    
###################################################################################################    
   
#########################"""Juanfe: función que crea la tabla"""########################################

    def create_table(conn,create_table_sql):
        try:
            c = conn.cursor()
            c.execute(create_table_sql)
        except Error as e:
            print(e)

#####################################################################################################

######################"""Función principal"""########################################

    def main(dbFolder):
        create_user_table = """CREATE TABLE IF NOT EXISTS marcaciones (
                                        USER_ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                        USER_NAME TEXT,
                                        USER_MACHINE TEXT,
                                        USER_MODULE TEXT,
                                        USER_TURN TEXT
                                        );"""
        conn = AppFunctions.create_connection(dbFolder)

        if conn is not None:
            AppFunctions.create_table(conn,create_user_table)
        else:
            print("Error! No se ha podido conectar con la base de datos")
#########################################################################################################

# Funcion para Obtener todos los usuarios 

    def getAllUsers(dbFolder):
        conn= AppFunctions.create_connection(dbFolder)
        
        get_all_users= """
                        SELECT * FROM marcaciones;
                        """
        try:
            c = conn.cursor()
            c.execute(get_all_users)

            return c
        except Error as e:
            print(e)
            
##################################################################################################

# Funcion para agregar las personas a la base de datos

    def addUser(self,dbFolder):
        conn = AppFunctions.create_connection(dbFolder)
        userID = self.ui.userID.text()
        userMaq = self.ui.userMaq.text()
        userMod = self.ui.userMod.text()
        userTurn = self.ui.userTurn.text()

        insert_person_data_sql = f""" INSERT INTO marcaciones (USER_NAME,USER_MACHINE,USER_MODULE,USER_TURN) VALUES
                                        ('{userID}','{userMaq}','{userMod}','{userTurn}');"""
        
        if not conn.cursor().execute(insert_person_data_sql):
            print('ERROR EN LA INSERCIÓN')
        else:
            conn.commit()

            #Limpiar el formulario

            self.ui.UserID.setText("")
            self.ui.Usermaq.setText("")
            self.ui.userMod.setText("")
            self.ui.userTurn.setText("")

            AppFunctions.displayUsers(self, AppFunctions.getAllUsers(dbFolder))

##################################################################################################

# Funcion para Mostrar los usuarios
 
    def displayUsers(self,rows):
        for row in rows:
            rowPosition = self.ui.tableWidget.rowCunt()

            if rowPosition + 1 > row[0]:
                continue
            itemCount = 0

            self.ui.tableWidget.setRowCount(rowPosition+1)
            qtablewidgetitem = QTableWidgetItem()
            self.ui.tableWidget.setVerticalHeaderItem(rowPosition,qtablewidgetitem)

            for item in row:
                self.qtablewidgetitem = QTableWidgetItem()
                self.ui.tableWidget.setItem(rowPosition, itemCount, self.qtablewidgetitem)
                self.qtablewidgetitem = self.ui.tableWidget.item(rowPosition,itemCount)
                self.qtablewidgetitem.setText(str(item))

                itemCount = itemCount + 1
                rowPosition = rowPosition + 1


