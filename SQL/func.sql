use ssms;
# 函数，获取当前学生id的最大值
# 返回值：int
delimiter //
drop function if exists get_max_id;
create function get_max_id() returns int
DETERMINISTIC READS SQL DATA
begin
    declare num int;
    select max(stu_id) into num from student;
    return num;
end //
delimiter ;