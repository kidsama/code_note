-- 关联修改
update terminal_user set home_dir = CONCAT('/home/', uid) where ds_name='KCM';