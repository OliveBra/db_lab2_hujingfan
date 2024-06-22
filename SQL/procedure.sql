# 创建一个存储过程，用于删除一个学生的信息,删除之前必须先删除学生的成绩信息，选课信息，奖惩信息
use ssms;
delimiter //
drop procedure if exists delete_student;
create procedure delete_student(in stu_id int)  
begin
    delete from score where score_stu_id = stu_id;
    delete from student_course where sc_stu_id = stu_id;
end //
delimiter ;