'''

关系型数据库
二维表，由行和列组成，行是记录，列是字段

用root登陆
mysql -u root -p

数据库导入
mysql -u root -p < FILE
或者进入到mysql中source一下文件

赋权限
grant all on *.* to 'USER'@'192%' identified by 'PASSWD'

解权
REVOKE ALL ON *.* FROM <USER>

候选键，可以唯一的确定一行，可以用来做主键
主键从候选中选出，一般是自增
主键不能为null，必须唯一，一般用整型作为主键

外键
当本表的某字段依赖其他表的候选键时称为外键

!!!!!约束!!!!!：
必须有值约束，不能为null
域约束，限定取值范围
实体完整性约束：不能为null，必须唯一
唯一键约束：可以null，但是有值的必须唯一

外键约束：
插入：
  主表增加记录无影响
  从表增加记录的外键需要看主表中是否存在
删除：
  从表删除记录无影响
  主表删除记录：
    cascade删除(删除主表会连同删除从表记录)
    set null: 主表记录删除，从表记录变成null，几乎不用
    restrict/no action: 如果主表删除记录，从表不允许主表删除，除非从表先删除
更新（和删除类似）：
  主表更新记录：
    cascade及联，主表更改从表也会更改
    set null，主表记录修改，从表为null，几乎不用
    restrict，主表修改从表不允许主表修改，除非从表先修改
  从表更新记录：随便改，主表不影响

一般不要cascade删除，可以设置一个deleted字段，而不真正删除数据

实体和实体之间有相同的属性，实体之间就是有关联
1：1，一个员工可以多个部门，一个部门多个员工
1：N，一个员工属于一个部门，一个部门多个员工，员工表中建外键
N：N，一个员工属于多个部门，一个部门多个员工，需要第三个表，第三张表使用2张表的主键联合做主键


SQL

查
insert into <table> (name,...) values ('name',...)

更新，必须有条件，否则全部改!
update <table> set field=value where id=x;

删除，最好用update语句而不是真删除
delete from <table> where id=x;

查询
select * from <table>
select <Field> from <table>

字符串相加，在dml中是concat()

分页
如果字段太多了使用limit可以限制查询的个数
设置offset来表示从哪个位置开始查询

如果数据很多，建议用limit和offset，避免磁盘IO太高
select <Field> from <table> where id > n limit <num> offset <num>

模糊匹配
<Field> like '*%'

order by <Field> desc，降序，默认升序

select distinct表示去重

聚合
count(*)，统计个数
sum()，求和
max()，求最大值
min()，求最小
avg()，求平均

group by是分组，结合聚合函数用，否则没有意义
having，后计算用的，因为select语句有加载顺序

多个表查询
select * from <table1> <alias1> join <table2> <alias2> where alias1.Field1 = alias2.Field2 and alias1.Field > n


'''