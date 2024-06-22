use ssms;
# 存储过程中有事务，用于学生选课，一门课程只能选一次，一门课程最多20人选
delimiter //
drop procedure if exists select_course;
create procedure select_course(in stu_id int, in cou_id int)
begin
    declare if_select int;
    declare cou_num int;

    start transaction;
    select count(*) into if_select from student_course where sc_stu_id = stu_id and sc_course_id = cou_id;
    select count(*) into cou_num from student_course where sc_course_id = cou_id;
    if if_select = 0 and cou_num <= 20 then
        set @result = 1;
        insert into student_course(sc_stu_id,sc_course_id) values(stu_id,cou_id);
        commit;
    else
        set @result = 0;
        rollback;
    end if;
end //

