"""
    根据建表工具，
"""
import pandas as pd
import sys
import decimal


def tableformat(field_type,value):
    value = str(value)
    if value.upper() == "NAN":
        value = ""
    else:
        if field_type.upper() == "DATE":
            value = value.split(" ")[0]
        elif "DOUBLE" in field_type.upper():
            value = "{:.6f}".format(decimal.Decimal(value))
    return str(value)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("ERROR:需要输入表名")
        sys.exit()

    df = pd.read_excel("建表工具.xlsx", sheet_name="insert", header=2)
    tableName = sys.argv[1]
    fields = df.columns
    insertSqls = []
    for row in range(1, df.shape[0]):
        rowValues = []
        template_sql = "insert into {} ({}) values ({})"
        for col in range(0,df.shape[1]):
            field_type = df.loc[0][col]
            cell = tableformat(field_type, df.loc[row][col])
            rowValues.append("'" + cell + "'")
        template_sql = template_sql.format(tableName, ",".join(fields), ", ".join(rowValues))
        insertSqls.append(template_sql)
    print("-" * 30)
    print(";\n".join(insertSqls))
    # 数据保存
    open("out.sql", 'w', encoding="utf-8").write(";\n".join(insertSqls))
