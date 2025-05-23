drop table invest;
create table invest(
	vest_id int auto_increment comment '投资ID',
	prd_channel char(20) comment '产品购买渠道',
	prd_name char(80) comment '产品名称',
	prd_rate float(10,2) comment '产品预期收益',
	prd_status char(1) comment '产品状态（到期可赎回1、封闭期0）',
	buy_amt float(10,2) comment '购买金额',
	buy_date date comment '购买日',
	due_date date comment '赎回日',
	ac_date date comment '会计日',
	current_amt float(10,2) comment '记账日总金额',
	profit float(10,2) comment '当前收益金额',
	days int comment '相差天数',
	real_rate float comment '真实年化',
	ts timestamp comment '时间戳',
	primary key (vest_id)
)ENGINE=InnoDB  DEFAULT CHARSET=utf8 comment = '投资信息表';
insert into invest (prd_channel, prd_name, prd_status, buy_date, due_date, ac_date, days, real_rate) values ('JNQLWQzpB0', 'XH3s', '1', '6067-07-10', '4799-03-02', '2196-11-10', 2920, 609);
insert into invest (prd_channel, prd_name, prd_status, buy_date, due_date, ac_date, days, real_rate) values ('g', 'zNluHO1I', '1', '2984-03-21', '2949-02-19', '4366-02-01', 6425, 9411);
insert into invest (prd_channel, prd_name, prd_status, buy_date, due_date, ac_date, days, real_rate) values ('i', 'FQ5yDzOxVu', '1', '8583-02-19', '2883-03-23', '3256-01-24', 5862, 4111);
insert into invest (prd_channel, prd_name, prd_status, buy_date, due_date, ac_date, days, real_rate) values ('zQe', 'ACMNrJ6H', '0', '2485-02-26', '7920-10-03', '7525-02-10', 9657, 7138);
insert into invest (prd_channel, prd_name, prd_status, buy_date, due_date, ac_date, days, real_rate) values ('CLwvTdm', '1SSWB7R', '0', '4261-03-01', '1399-10-14', '8574-06-20', 4513, 2544);
select * from invest;
