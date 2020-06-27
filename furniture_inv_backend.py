import sqlite3
# Backend of Sushil Furniture

def FurnData():
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS furniture (id INTEGER PRIMARY KEY, \
                Manufacturer text, Item_Name text, Price text, Color text, \
                Dimension text, Weight text, Item_Model_No text, Quantity text, \
                Assemby_Req text, Pri_Material text, Capacity text, Warranty text)")
    con.commit()
    con.close()

def addNewItem(Manufacturer, Item_Name, Price, Color, Dimension, Weight, Item_Model_No, Quantity, Assemby_Req, Pri_Material, Capacity, Warranty):
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("INSERT INTO furniture VALUES (NULL,?,?,?,?,?,?,?,?,?,?,?,?)", (Manufacturer, Item_Name, Price, Color, Dimension, Weight, Item_Model_No, Quantity, Assemby_Req, Pri_Material, Capacity, Warranty))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM furniture")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("DELETE FROM furniture WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(Manufacturer="", Item_Name="", Price="", Color="", Dimension="", Weight="", Item_Model_No="", Quantity="", Assemby_Req="", Pri_Material="", Capacity="", Warranty=""):
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM furniture WHERE Manufacturer=? OR Item_Name=? OR Price=? OR Color=? OR Dimension=? OR Weight=? OR Item_Model_No=? OR Quantity=? OR Assemby_Req=? OR Pri_Material=? OR Capacity=? OR Warranty=?", (Manufacturer, Item_Name, Price, Color, Dimension, Weight, Item_Model_No, Assemby_Req, Pri_Material, Capacity, Warranty))
    rows = cur.fetchall()
    con.close()
    return rows

def updateData(Manufacturer="", Item_Name="", Price="", Color="", Dimension="", Weight="", Item_Model_No="", Quantity="", Assemby_Req="", Pri_Material="", Capacity="", Warranty=""):
    con = sqlite3.connect("furniture.db")
    cur = con.cursor()
    cur.execute("UPDATE furniture SET Manufacturer=?, Item_Name=?, Price=?, Color=?, Dimension=?, Weight=?, Item_Model_No=?, Quantity=?, Assemby_Req=?, Pri_Material=?, Capacity=?, Warranty=?", (Manufacturer, Item_Name, Price, Color, Dimension, Weight, Item_Model_No, Assemby_Req, Pri_Material, Capacity, Warranty, id))
    con.commit()
    con.close()

FurnData()