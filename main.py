from api import HKSETM

def main():
    api_key = "APIKEY Inbox @huykaiserOwO"
    email_api = HKSETM(api_key)

    # Liệt kê các domain
    print("Liệt kê các domain:")
    domains_response = email_api.list_domains()
    print(domains_response)
    print("-" * 50)

    # Tạo email mới
    print("Tạo email mới:")
    create_response = email_api.create_email()
    print(create_response)
    print("-" * 50)

    if create_response and create_response.get("status") == "success":
        email_token = create_response["data"]["email_token"]
        email = create_response["data"]["email"]

        # Thay đổi email
        print("Thay đổi email:")
        new_username = "newuser"
        new_domain = "site2.com"
        change_response = email_api.change_email(email_token, new_username, new_domain)
        print(change_response)
        print("-" * 50)

        # Lấy danh sách tin nhắn
        print("Lấy danh sách tin nhắn:")
        messages_response = email_api.fetch_messages(email_token)
        print(messages_response)
        print("-" * 50)

        if messages_response and messages_response.get("status") == "success":
            messages = messages_response["data"]["messages"]
            if messages:
                first_message_id = messages[0]["id"]

                # Lấy chi tiết một tin nhắn cụ thể
                print("Lấy chi tiết tin nhắn:")
                single_message = email_api.fetch_message(first_message_id)
                print(single_message)
                print("-" * 50)

                # Xóa một tin nhắn cụ thể
                print("Xóa tin nhắn:")
                delete_message_response = email_api.delete_message(first_message_id)
                print(delete_message_response)
                print("-" * 50)

        # Xóa email
        print("Xóa email:")
        delete_email_response = email_api.delete_email(email_token)
        print(delete_email_response)
        print("-" * 50)

        # Tạo URL chứa token email
        print("Tạo URL chứa token email:")
        token_url = email_api.generate_token_url(email_token)
        print(token_url)
        print("-" * 50)
    else:
        print("Không thể tạo email.")

if __name__ == "__main__":
    main()




#  DATA RESPONSE API JSON LOAD HSK TEMP MAIL DEMO
# --------------------------------------------------
# Liệt kê các domain:
# {'status': 'success', 'data': {'domains': {'1': 'site1.com', '2': 'site2.com', '3': 'site3.com'}}}
# --------------------------------------------------
# Tạo email mới:
# {'status': 'success', 'data': {'email': 'email@domain.com', 'email_token': 'eyJpdiI6IlB...', 'deleted_in': '2022-12-02 20:38:13'}}
# --------------------------------------------------
# Thay đổi email:
# {'status': 'success', 'data': {'email': 'newuser@site2.com', 'email_token': 'eyJpdiI6IlB...', 'deleted_in': '2022-12-02 20:38:13'}}
# --------------------------------------------------
# Lấy danh sách tin nhắn:
# {'status': 'success', 'data': {'mailbox': 'qsirrsr8460@site.com', 'messages': [...]}}
# --------------------------------------------------
# Lấy chi tiết tin nhắn:
# {'status': 'success', 'data': [...]}
# --------------------------------------------------
# Xóa tin nhắn:
# {'status': 'success', 'message': 'the message has been deleted'}
# --------------------------------------------------
# Xóa email:
# {'status': 'success', 'message': 'the email has been deleted'}
# --------------------------------------------------
# Tạo URL chứa token email:
# http://localhost/token/eyJpdiI6IlB...

# --------------------------------------------------
