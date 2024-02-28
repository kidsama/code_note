from celery_task import send_email, send_msg
result1 = send_email.delay("张三")
print(result1.id)
result2 = send_email.delay("李四")
print(result2.id)
result3 = send_email.delay("王五")
print(result3.id)
result4 = send_email.delay("赵六")
print(result4.id)