from send_email import send_email

import asyncio

async def test_send_email():
    标题 = "测试邮件"
    内容 = "这是一封测试邮件,用于验证send_email函数是否正常工作。"
    
    try:
        await send_email(标题, 内容)
        print("邮件发送成功!")
    except Exception as e:
        print(f"邮件发送失败: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_send_email())
