# 对于学生信息表student进行删除和插入时，触发器会自动更新班级表class和专业表major的学生人数
use ssms;
delimiter //
drop trigger if exists add_stu_num;
create trigger add_stu_num
after insert on student
for each row
begin
    update class set class_stu_num = class_stu_num + 1 where class_id = new.stu_class_id;
    update major set major_stu_num = major_stu_num + 1 where major_id = (select class_major_id from class where class_id = new.stu_class_id);
end //
delimiter ;

delimiter //
drop trigger if exists sub_stu_num;
create trigger sub_stu_num
after delete on student
for each row
begin
    update class set class_stu_num = class_stu_num - 1 where class_id = old.stu_class_id;
    update major set major_stu_num = major_stu_num - 1 where major_id = (select class_major_id from class where class_id = old.stu_class_id);
end //
delimiter ;

delimiter //
drop trigger if exists change_stu_num;
create trigger change_stu_num
after update on student
for each row
begin
    update class set class_stu_num = class_stu_num - 1 where class_id = old.stu_class_id;
    update major set major_stu_num = major_stu_num - 1 where major_id = (select class_major_id from class where class_id = old.stu_class_id);
    update class set class_stu_num = class_stu_num + 1 where class_id = new.stu_class_id;
    update major set major_stu_num = major_stu_num + 1 where major_id = (select class_major_id from class where class_id = new.stu_class_id);
end //