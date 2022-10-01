import requests

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }

    def get_files_list(self):
        files_url = 'https://cloud-api.yandex.net/disk/resources/files'
        headers = self.get_headers()
        response = requests.get(files_url, headers=headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href_json = self._get_upload_link(disk_file_path=disk_file_path)
        href = href_json['href']
        response = requests.put(href, data=open(filename, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")
        else:
            print('Failet')


if __name__ == '__main__':
    disk_file_path = '/disk.txt'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload_file_to_disk(disk_file_path, 'file.txt')

    print(result)