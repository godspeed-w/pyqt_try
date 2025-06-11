# pyqt_try
pyqt练习

## 环境要求
python3 、 pyqt5=5.15

## 实现功能
> 项目自动转换格式
> > 使用python bin\autoSwitch.py 即可进行扫描转换

* 项目框架搭建完成

## 记账本项目
```sql
-- 数据库book_keeping
drop table invest;
create table invest(
	vest_id int auto_increment comment '投资ID',
	prd_channel char(20) comment '产品购买渠道',
	prd_name char(80) comment '产品名称',
	prd_rate float(10,2) comment '产品预期收益',
	prd_status char(1) comment '产品状态（未赎回N,已赎回Y）',
	buy_amt float(10,2) comment '购买金额',
	buy_date date comment '购买日',
	ma_date date comment '到期日',
	ac_date date comment '会计日',
	current_amt float(10,2) comment '记账日总金额',
	profit float(10,2) comment '当前收益金额',
	days int comment '相差天数',
	real_rate float comment '真实年化',
	isnew char(1) comment '是否最新记录（Y,N）',
	remark text comment '备注',
	ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP comment '时间戳',
	primary key (vest_id)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8 comment = '投资信息表';

-- 数据库备份
mysqldump -u root -p book_keeping > book_keeping_backup.sql
-- 表备份
mysqldump -u root -p book_keeping invest > invest_backup.sql

-- 数据库导入
mysql -u root -p book_keeping < book_keeping_backup.sql
-- 表导入
mysql -u root -p book_keeping < invest_backup.sql
source invest_backup.sql
```

## 打包命令
```shell
pyinstaller -F -w -i logo.png main.py --noconsole

pyinstaller -F -i logo.png calcReturn.py --noconsole
```