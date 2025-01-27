import requests
import json
from typing import Any, Dict, Optional

class HKSETM:
    """
    Lớp HKSETM cung cấp các phương thức để tương tác với API Email, bao gồm
    việc liệt kê các domain, tạo email mới, thay đổi email, xóa email, lấy danh sách
    tin nhắn, lấy chi tiết tin nhắn, xóa tin nhắn và tạo URL chứa token email.
    """

    BASE_URL = "http://huykaiser.lol/api"

    def __init__(self, api_key: str):
        """
        Khởi tạo đối tượng HKSETM với API Key.

        Args:
            api_key (str): API Key của bạn để xác thực các yêu cầu tới API Email.
        """
        self.api_key = api_key

    def list_domains(self) -> Optional[Dict[str, Any]]:
        """
        Lấy danh sách các domain có sẵn từ API.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON chứa danh sách các domain nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/domains/{self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error listing domains: {e}")
            return None

    def create_email(self) -> Optional[Dict[str, Any]]:
        """
        Tạo email mới thông qua API.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON chứa thông tin email mới nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/email/create/{self.api_key}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error creating email: {e}")
            return None

    def change_email(self, email_token: str, username: str, domain: str) -> Optional[Dict[str, Any]]:
        """
        Thay đổi email hiện tại bằng cách cung cấp token email cũ, tên người dùng mới và domain mới.

        Args:
            email_token (str): Token email cũ mà bạn muốn thay đổi.
            username (str): Tên người dùng hoặc ID email tùy chỉnh mới.
            domain (str): Domain tùy chỉnh mới.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON chứa thông tin email đã thay đổi nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/email/change/{email_token}/{username}/{domain}/{self.api_key}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error changing email: {e}")
            return None

    def delete_email(self, email_token: str) -> Optional[Dict[str, Any]]:
        """
        Xóa email hiện tại bằng token email và tạo email mới.

        Args:
            email_token (str): Token email mà bạn muốn xóa.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON xác nhận việc xóa email nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/email/delete/{email_token}/{self.api_key}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error deleting email: {e}")
            return None

    def fetch_messages(self, email_token: str) -> Optional[Dict[str, Any]]:
        """
        Lấy danh sách các tin nhắn của email dựa trên token email cung cấp.

        Args:
            email_token (str): Token email mà bạn muốn lấy tin nhắn.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON chứa danh sách tin nhắn nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/messages/{email_token}/{self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching messages: {e}")
            return None

    def fetch_message(self, message_id: str) -> Optional[Dict[str, Any]]:
        """
        Lấy chi tiết một tin nhắn cụ thể dựa trên ID tin nhắn.

        Args:
            message_id (str): ID của tin nhắn mà bạn muốn lấy chi tiết.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON chứa chi tiết tin nhắn nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/message/{message_id}/{self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching message: {e}")
            return None

    def delete_message(self, message_id: str) -> Optional[Dict[str, Any]]:
        """
        Xóa một tin nhắn cụ thể dựa trên ID tin nhắn.

        Args:
            message_id (str): ID của tin nhắn mà bạn muốn xóa.

        Returns:
            Optional[Dict[str, Any]]: Phản hồi JSON xác nhận việc xóa tin nhắn nếu thành công,
            hoặc `None` nếu có lỗi xảy ra.
        """
        url = f"{self.BASE_URL}/message/delete/{message_id}/{self.api_key}"
        try:
            response = requests.post(url)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error deleting message: {e}")
            return None

    def generate_token_url(self, email_token: str) -> str:
        """
        Tạo URL chứa token email để gửi cho người dùng.

        Args:
            email_token (str): Token email mà bạn muốn tạo URL.

        Returns:
            str: URL chứa token email.
        """
        return f"http://huykaiser.lol/token/{email_token}"
