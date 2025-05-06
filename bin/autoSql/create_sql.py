import random
import re
import string
import pandas as pd

df = pd.read_excel("建表工具.xlsx", sheet_name="Sheet1", header=None)

# 定义全局数据结构
myTable = {
    "tableName": "",
    "tableNameZH":"",
    "primaryKey": [],
    "fields": []
}

# 数据赋值
myTable["tableName"] = df.loc[2][0]
myTable["tableNameZH"] = df.loc[3][0]
for row in range(2, df.shape[0]):
    itemField = {"field": "", "type": "", "comment": ""}
    itemField["field"] = df.loc[row][2]
    itemField["type"] = df.loc[row][3]
    if df.loc[row][1] == "是":
        myTable["primaryKey"].append(itemField["field"])
    if not pd.isna(df.loc[row][4]):
        itemField["comment"] = df.loc[row][4]
    print(itemField)
    myTable["fields"].append(itemField)
print("-"*30)

# 建表语句生成
createTableSql = "drop table {};\ncreate table {}(\n".format(
    myTable["tableName"], myTable["tableName"])
for i in myTable["fields"]:
    if i["comment"] != "":
        createTableSql += "\t{} {} comment '{}',\n".format(
            i["field"], i["type"], i["comment"])
    else:
        createTableSql += "\t{} {} {},\n".format(
            i["field"], i["type"], i["comment"])
if len(myTable["primaryKey"]) != 0:
    createTableSql += "\tprimary key ({})\n)".format(
        ",".join(myTable["primaryKey"]))
else:
    createTableSql = createTableSql[:-2] + "\n)"
# 指定编码格式与引擎
createTableSql += "ENGINE=InnoDB  DEFAULT CHARSET=utf8"
if not pd.isna(myTable["tableNameZH"]):
    createTableSql += " comment = '{}';".format(myTable["tableNameZH"])
else:
    createTableSql +=";"
print(createTableSql)
print("-"*30)


# 模拟插入数据语句生成,myRandStr
def mrs(sType='char', charLen=10):
    retStr = ""
    if sType == "num":
        retStr = str(random.randint(1, 10000))
    elif sType == "y":
        retStr = str(random.randint(1000, 9999))
    elif sType == "M":
        retStr = str(random.randint(1, 12)).zfill(2)
    elif sType == "d":
        retStr = str(random.randint(1, 28)).zfill(2)
    elif sType == "h":
        retStr = str(random.randint(0, 24)).zfill(2)
    elif sType == "m" or sType == "s":
        retStr = str(random.randint(0, 59)).zfill(2)
    elif sType == "s":
        retStr = str(random.randint(0, 59)).zfill(2)
    else:
        retStr = "".join(random.choice(string.ascii_letters + string.digits)
                         for _ in range(random.randint(1, charLen)))
    return retStr


def insertSqlCreate(iter=5):
    insertSqls = []
    for i in range(iter):
        fields, values = [], []
        for i in myTable["fields"]:
            upType = i["type"].upper()
            random_val = ""
            if "CHAR" in upType:
                # charLen = int(re.compile(r'\d+').findall(i["type"])[0])
                random_val = "'{}'".format(mrs())
            elif "DATE" == upType:
                random_val = "'{}-{}-{}'".format(mrs("y"), mrs("M"), mrs("d"))
            elif "TIME" == upType:
                random_val = "'{}:{}:{}'".format(mrs("h"), mrs("m"), mrs("s"))
            elif "DATETIME" == upType:
                random_val = "'{}-{}-{} {}:{}:{}'".format(
                    mrs("y"), mrs("M"), mrs("d"), mrs("h"), mrs("m"), mrs("s"))
            elif upType in ["INT", "FLOAT", "DOUBLE"]:
                random_val = mrs("num")
            else:
                pass
            if random_val != "":
                values.append(random_val)
                fields.append(i["field"])
        insertSql = "insert into {} ({}) values ({});".format(
            myTable["tableName"], ", ".join(fields), ", ".join(values))
        insertSqls.append(insertSql)
    return insertSqls


print("\n".join(insertSqlCreate()))
print("-"*30)

# 查询语句
searchSql = "select * from {};".format(myTable["tableName"])
print(searchSql)
print("-"*30)

# 数据保存
sql = "{}\n{}\n{}\n".format(
    createTableSql, "\n".join(insertSqlCreate()), searchSql)
open("out.sql", 'w', encoding="utf-8").write(sql)
