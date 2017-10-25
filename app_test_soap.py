"""Module for Soap test"""

from zeep import Client


def main():
    """Soap test"""
    client = Client('http://localhost:8000?wsdl')
    result = client.service.insoap(
        'Привет')
    print(result)


if __name__ == '__main__':
    main()
