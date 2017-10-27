select * from user;

insert into user VALUES (1001,'peter','peter@email.com');
insert into user VALUES (1002,'master','master@email.com');
insert into user VALUES (1003,'administrator','administrator@email.com');
insert into user VALUES (1004,'ethan','ethan@email.com');


select * from post;

insert into post VALUES (10001,'2015年2月23日，Red Hat产品安全团队发布了一个Samba服务端smbd的漏洞公告 [1]，该漏洞编号为CVE-2015-0240，几乎影响所有版本。','2017-10-26 09:00:00',1001);
insert into post VALUES (10002,'该漏洞的触发并不需要通过Samba服务器的账号认证，而smbd服务端通常以root权限运行，如果漏洞能够被用来实现任意代码执行，则攻击者可以远程获取系统root权限，危害极其严重','2017-10-26 09:00:00',1002);
insert into post VALUES (10003,'该漏洞的基本原理是栈上未初始化的指针被传入TALLOC_FREE()函数。','2017-10-26 09:00:00',1003);
insert into post VALUES (10004,'想要利用这个漏洞，首先需要控制栈上未初始化的数据，这和编译生成的二进制文件中栈的布局有关。','2017-10-26 09:00:00',1004);
