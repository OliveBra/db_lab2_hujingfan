use ssms;


# 专业表
create table major(
    major_id int not null,
    major_name varchar(50) not null,
    major_stu_num int not null default 0,# 专业人数

    constraint pk_major_id primary key(major_id)
);


# 班级表
create table class(
    class_id int not null,
    class_name varchar(50) not null,
    class_major_id int not null,# 班级所属专业id
    class_grade varchar(50) not null default '大一',# 班级所属年级
    class_stu_num int not null default 0,# 班级人数

    constraint pk_class_id primary key(class_id),
    constraint fk_class_major_id foreign key(class_major_id) references major(major_id)
);

# 学生表
create table student(
    stu_id int not null,
    stu_name varchar(50) not null,
    stu_birth date,
    stu_sex varchar(50) default '男',
    stu_political_status varchar(50) default '群众',
    stu_ethnic varchar(50) default '汉族',
    stu_iden_num varchar(50), # 身份证号 
    stu_telephone varchar(50),
    stu_academic int default 4,# 学制
    stu_class_id int not null,# 班级
    stu_photo_address varchar(50) default '.\\stu_photo\\1.jpg' ,# 照片地址

    constraint pk_stu_id primary key(stu_id),
    constraint fk_stu_class_id foreign key(stu_class_id) references class(class_id)
);

# 课程表
create table course(
    course_id int not null,
    course_name varchar(50) not null,
    course_if_compulsory varchar(50),#课程必修情况
    course_major_id int not null,# 课程所属专业
    course_credit int not null,# 学分
    course_status int default 0,# 课程状态,0表示未开课，1表示已开课，2表示已结课
    course_semester varchar(50) not null,# 开设学期,例如2024_1表示2024年第一学期

    constraint pk_course_id primary key(course_id),
    constraint fk_course_major_id foreign key(course_major_id) references major(major_id)
);

# 学生选课表
create table student_course(
    sc_stu_id int not null,
    sc_course_id int not null,
    
    constraint pk_sc_stu_id_sc_course_id primary key(sc_stu_id,sc_course_id),
    constraint fk_sc_stu_id foreign key(sc_stu_id) references student(stu_id),
    constraint fk_sc_course_id foreign key(sc_course_id) references course(course_id)
);

# 成绩表
create table score(
    score_stu_id int not null,
    score_course_id int not null,   
    score_num int not null,# 成绩
    score_if_modify int default 0,# 是否修改过成绩，0表示未修改，1表示修改过

    constraint pk_score_stu_id_score_course_id primary key(score_stu_id,score_course_id),
    constraint fk_score_stu_id foreign key(score_stu_id) references student(stu_id),
    constraint fk_score_course_id foreign key(score_course_id) references course(course_id)
);
